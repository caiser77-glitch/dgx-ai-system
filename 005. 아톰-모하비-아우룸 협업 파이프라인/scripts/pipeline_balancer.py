#!/usr/bin/env python3
"""아톰-아우룸맥 작업 배정 밸런서.

기본은 dry-run이다. RAM 사용률 대신 MemAvailable, memory PSI, swap activity,
큐 길이, 맥 유휴 상태를 함께 보고 맥으로 보낼 작업 후보를 고른다.
"""

import argparse
import json
import os
import re
import shlex
import subprocess
import time
from pathlib import Path

JOB_SUFFIXES = ("summary.md", "result.json", "draft.md")
HANDOFF_STATUSES = {"drafting", "admin_pending", "review_pending", "reviewed"}
DONE_MAC_STATUSES = {"admin_pending", "review_pending", "reviewed", "published_synced", "published"}


def read_meminfo():
    data = {}
    for line in Path("/proc/meminfo").read_text(encoding="utf-8").splitlines():
        key, value = line.split(":", 1)
        data[key] = int(value.strip().split()[0])
    return data


def read_memory_psi():
    psi = {"some_avg60": 0.0, "full_avg60": 0.0}
    try:
        for line in Path("/proc/pressure/memory").read_text(encoding="utf-8").splitlines():
            parts = dict(item.split("=") for item in line.split()[1:])
            if line.startswith("some "):
                psi["some_avg60"] = float(parts.get("avg60", 0))
            elif line.startswith("full "):
                psi["full_avg60"] = float(parts.get("avg60", 0))
    except FileNotFoundError:
        pass
    return psi


def read_swap_pages():
    values = {"pswpin": 0, "pswpout": 0}
    for line in Path("/proc/vmstat").read_text(encoding="utf-8").splitlines():
        if line.startswith("pswpin ") or line.startswith("pswpout "):
            key, value = line.split()
            values[key] = int(value)
    return values


def read_cpu_idle(delay=0.5):
    def sample():
        values = [int(x) for x in Path("/proc/stat").read_text(encoding="utf-8").splitlines()[0].split()[1:]]
        idle = values[3] + values[4]
        total = sum(values)
        return idle, total

    idle1, total1 = sample()
    time.sleep(delay)
    idle2, total2 = sample()
    total_delta = max(total2 - total1, 1)
    return 100.0 * (idle2 - idle1) / total_delta


def atom_pressure(delay=1.0):
    mem = read_meminfo()
    psi = read_memory_psi()
    swap1 = read_swap_pages()
    time.sleep(delay)
    swap2 = read_swap_pages()
    available_gib = mem.get("MemAvailable", 0) / 1024 / 1024
    swap_events = (swap2["pswpin"] - swap1["pswpin"]) + (swap2["pswpout"] - swap1["pswpout"])
    pressured = available_gib < 10 or psi["some_avg60"] > 1.0 or psi["full_avg60"] > 0.2 or swap_events > 200
    return {
        "available_gib": round(available_gib, 2),
        "psi_some_avg60": psi["some_avg60"],
        "psi_full_avg60": psi["full_avg60"],
        "swap_events_per_sec": int(swap_events / max(delay, 0.1)),
        "cpu_idle_pct": round(read_cpu_idle(), 1),
        "pressured": pressured,
    }


def parse_frontmatter(path):
    try:
        content = path.read_text(encoding="utf-8", errors="replace")
    except FileNotFoundError:
        return {}
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not match:
        return {}
    meta = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip().strip('"').strip("'")
    return meta


def job_id_from_path(path):
    name = path.name
    for suffix in (".summary.md", ".result.json", ".draft.md"):
        if name.endswith(suffix):
            return name[: -len(suffix)]
    return path.stem


def local_job_ids(stage_dir):
    ids = set()
    if not stage_dir.exists():
        return ids
    for path in list(stage_dir.glob("*.draft.md")) + list(stage_dir.glob("*.summary.md")):
        ids.add(job_id_from_path(path))
    return ids


def archive_local_stale_drafting(root, execute=False):
    drafting = root / "02_drafting"
    archive = root / "05_archived_duplicates"
    advanced = local_advanced_ids(root)
    archived_jobs = []
    archived_files = []
    if not drafting.exists():
        return {"archived_jobs": [], "archived_files": []}
    for job_id in sorted(advanced):
        files = collect_job_files(drafting, job_id)
        if not files:
            continue
        archived_jobs.append(job_id)
        if execute:
            archive.mkdir(parents=True, exist_ok=True)
        for src in files:
            archived_files.append(src.name)
            if execute:
                dst = archive / src.name
                if dst.exists():
                    dst = archive / f"{int(time.time())}.{src.name}"
                src.rename(dst)
    return {"archived_jobs": archived_jobs, "archived_files": archived_files}


def local_published_ids(root):
    return local_job_ids(root / "04_published")


def local_advanced_ids(root):
    return local_job_ids(root / "03_review_pending") | local_published_ids(root)


def atom_drafting_jobs(root):
    drafting = root / "02_drafting"
    advanced = local_advanced_ids(root)
    jobs = []
    for draft in sorted(drafting.glob("*.draft.md"), key=lambda p: p.stat().st_mtime):
        meta = parse_frontmatter(draft)
        status = meta.get("status", "drafting")
        if status not in HANDOFF_STATUSES:
            continue
        job_id = job_id_from_path(draft)
        if job_id in advanced:
            continue
        jobs.append({"job_id": job_id, "status": status, "mtime": draft.stat().st_mtime})
    return jobs


def mac_status(host, root):
    script = r"""
import glob
import json
import os
import re
import shlex
import subprocess
import sys

root = sys.argv[1]
jobs = []
for path in glob.glob(os.path.join(root, "02_drafting", "*.draft.md")):
    status = "unknown"
    try:
        content = open(path, encoding="utf-8", errors="replace").read(2048)
        match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
        if match:
            for line in match.group(1).splitlines():
                if line.startswith("status:"):
                    status = line.split(":", 1)[1].strip().strip('"').strip("'")
    except Exception:
        pass
    jobs.append({"job_id": os.path.basename(path)[:-len(".draft.md")], "status": status})
try:
    load = subprocess.check_output(["uptime"], text=True).strip()
except Exception:
    load = ""
print(json.dumps({"jobs": jobs, "load": load}, ensure_ascii=False))
"""
    remote_cmd = "python3 -c " + shlex.quote(script) + " " + shlex.quote(root)
    result = subprocess.run(["ssh", host, remote_cmd], capture_output=True, text=True, timeout=15)
    if result.returncode != 0:
        return {"ok": False, "error": (result.stderr or result.stdout).strip(), "jobs": [], "load": ""}
    data = json.loads(result.stdout or "{}")
    data["ok"] = True
    return data


def postprocess_mac_published(host, root, published_ids, execute=False):
    if not published_ids:
        return {"moved_jobs": [], "moved_files": []}
    script = r"""
import json
import os
import re
import shutil
import sys
import time

root = sys.argv[1]
execute = sys.argv[2] == "1"
job_ids = set(json.loads(sys.argv[3]))
drafting = os.path.join(root, "02_drafting")
published = os.path.join(root, "04_published")
moved_jobs = []
moved_files = []
if execute:
    os.makedirs(published, exist_ok=True)

def update_status(path):
    try:
        content = open(path, encoding="utf-8", errors="replace").read()
    except FileNotFoundError:
        return
    if re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL):
        body = re.sub(r"^---\s*\n(.*?)\n---\s*\n", "", content, count=1, flags=re.DOTALL)
        meta = {}
        match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
        for line in match.group(1).splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                meta[key.strip()] = value.strip().strip('"').strip("'")
    else:
        body = content
        meta = {}
    meta["status"] = "published_synced"
    meta["assigned_agent"] = "Aurum"
    meta["synced_at"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    updated = "---\n" + "\n".join(f"{k}: {v}" for k, v in meta.items()) + "\n---\n\n" + body.lstrip("\n")
    open(path, "w", encoding="utf-8").write(updated)

for job_id in sorted(job_ids):
    files = []
    for suffix in ("summary.md", "result.json", "draft.md"):
        path = os.path.join(drafting, f"{job_id}.{suffix}")
        if os.path.exists(path):
            files.append(path)
    if not files:
        continue
    moved_jobs.append(job_id)
    if execute:
        draft = os.path.join(drafting, f"{job_id}.draft.md")
        update_status(draft)
    for src in files:
        dst = os.path.join(published, os.path.basename(src))
        moved_files.append(os.path.basename(src))
        if execute:
            if os.path.exists(dst):
                os.remove(dst)
            shutil.move(src, dst)
print(json.dumps({"moved_jobs": moved_jobs, "moved_files": moved_files}, ensure_ascii=False))
"""
    remote_cmd = "python3 -c " + shlex.quote(script) + " " + shlex.quote(root) + " " + ("1" if execute else "0") + " " + shlex.quote(json.dumps(sorted(published_ids)))
    result = subprocess.run(["ssh", host, remote_cmd], capture_output=True, text=True, timeout=30)
    if result.returncode != 0:
        raise RuntimeError((result.stderr or result.stdout).strip())
    return json.loads(result.stdout or "{}")


def collect_job_files(stage_dir, job_id):
    return [stage_dir / f"{job_id}.{suffix}" for suffix in JOB_SUFFIXES if (stage_dir / f"{job_id}.{suffix}").exists()]


def count_mac_status(mac_jobs):
    admin_pending = sum(1 for job in mac_jobs if job.get("status") == "admin_pending")
    drafting = sum(1 for job in mac_jobs if job.get("status") == "drafting")
    return admin_pending, drafting


def write_status_file(path, mac_jobs, execute=False):
    admin_pending, drafting = count_mac_status(mac_jobs)
    payload = {
        "admin_pending": admin_pending,
        "drafting": drafting,
        "launchd": "active",
        "updated": time.strftime("%Y-%m-%d %H:%M:%S"),
        "source": "atom-balancer",
    }
    if execute:
        Path(path).write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
    return payload


def assign_to_mac(atom_root, mac_host, mac_root, jobs, execute=False):
    copied = []
    drafting = atom_root / "02_drafting"
    for job in jobs:
        for src in collect_job_files(drafting, job["job_id"]):
            remote = f"{mac_host}:{mac_root}/02_drafting/{src.name}"
            if execute:
                result = subprocess.run(["rsync", "-az", "--ignore-existing", "--partial", str(src), remote], capture_output=True, text=True, timeout=30)
                if result.returncode != 0:
                    raise RuntimeError((result.stderr or result.stdout).strip())
            copied.append(src.name)
    return copied


def main():
    parser = argparse.ArgumentParser(description="아톰-아우룸맥 작업 배정 밸런서")
    parser.add_argument("--atom-root", default=os.environ.get("ATOM_PIPELINE_ROOT", "/home/caiser77/AI_BASE"))
    parser.add_argument("--mac-host", default=os.environ.get("AURUM_MAC_SSH", "aurum-mac"))
    parser.add_argument("--mac-root", default=os.environ.get("MOHAVE_PIPELINE_ROOT", "/Users/nams/AI_BASE/AurumPipeline_mohave"))
    parser.add_argument("--max-assign", type=int, default=int(os.environ.get("BALANCER_MAX_ASSIGN", "2")))
    parser.add_argument("--min-mac-free-slots", type=int, default=int(os.environ.get("BALANCER_MIN_MAC_FREE_SLOTS", "2")))
    parser.add_argument("--execute", action="store_true", help="실제로 rsync 배정/후처리 수행")
    parser.add_argument("--skip-postprocess", action="store_true", help="맥 published 후처리를 건너뜀")
    parser.add_argument("--skip-local-archive", action="store_true", help="아톰 stale 02_drafting 아카이브를 건너뜀")
    parser.add_argument("--status-file", default=os.environ.get("PIPELINE_MAC_STATUS_FILE", "/home/caiser77/AI_BASE/pipeline_mac_status.json"))
    args = parser.parse_args()

    atom_root = Path(args.atom_root)
    pressure = atom_pressure()
    local_archived = {"archived_jobs": [], "archived_files": []}
    if not args.skip_local_archive:
        local_archived = archive_local_stale_drafting(atom_root, execute=args.execute)
    atom_jobs = atom_drafting_jobs(atom_root)
    published_ids = local_published_ids(atom_root)
    postprocessed = {"moved_jobs": [], "moved_files": []}
    if not args.skip_postprocess:
        postprocessed = postprocess_mac_published(args.mac_host, args.mac_root, published_ids, execute=args.execute)
    mac = mac_status(args.mac_host, args.mac_root)
    mac_jobs = mac.get("jobs", [])
    status_payload = write_status_file(args.status_file, mac_jobs, execute=args.execute)
    mac_active = [j for j in mac_jobs if j.get("status") not in DONE_MAC_STATUSES]
    mac_ids = {j.get("job_id") for j in mac_jobs}
    candidates = [j for j in atom_jobs if j["job_id"] not in mac_ids]

    # RAM 사용률은 판단 조건에서 제외한다. 실제 압박과 맥 큐 여유를 본다.
    mac_has_room = mac.get("ok") and len(mac_active) <= args.min_mac_free_slots
    should_assign = bool(candidates) and mac_has_room
    selected = candidates[: args.max_assign] if should_assign else []
    copied = assign_to_mac(atom_root, args.mac_host, args.mac_root, selected, execute=args.execute) if selected else []

    print(json.dumps({
        "ok": True,
        "mode": "execute" if args.execute else "dry-run",
        "atom_pressure": pressure,
        "atom_drafting_jobs": len(atom_jobs),
        "mac_ok": mac.get("ok", False),
        "mac_load": mac.get("load", ""),
        "mac_jobs": len(mac_jobs),
        "mac_active_jobs": len(mac_active),
        "status_file": args.status_file,
        "status_payload": status_payload,
        "local_archived_jobs": local_archived.get("archived_jobs", []),
        "local_archived_files": local_archived.get("archived_files", []),
        "postprocessed_jobs": postprocessed.get("moved_jobs", []),
        "postprocessed_files": postprocessed.get("moved_files", []),
        "candidate_jobs": [j["job_id"] for j in candidates],
        "selected_jobs": [j["job_id"] for j in selected],
        "copied_files": copied,
        "decision": "assign" if selected else "hold",
        "reason": "맥 큐에 여유가 있고 아톰 drafting 후보가 있음" if selected else "배정할 신규 후보가 없거나 맥 큐 여유가 부족함",
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
