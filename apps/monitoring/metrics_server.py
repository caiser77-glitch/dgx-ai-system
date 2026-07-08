#!/usr/bin/env python3
# Created: 2026-07-05 by Antigravity AI
# Purpose: Micro responsive live web dashboard server for Aurum Live Monitoring (No Blinking, Low Memory)

import os
import sys
import json
import time
import glob
import subprocess
import threading
from pathlib import Path
from http.server import HTTPServer, BaseHTTPRequestHandler

# 경로 바인딩
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
METADATA_DIR = PROCESSED_DIR / "metadata"
NAS_SCAN_ROOT = "/mnt"
TARGET_EXTENSIONS = [".pdf", ".docx", ".txt", ".pptx", ".xlsx", ".csv", ".hwp", ".hwpx", ".xls"]

# 전수조사 대상 총량 추정치 (하드코딩 대신 백그라운드에서 주기적으로 재계산)
total_files_estimate = 94513
total_files_lock = threading.Lock()

def get_gpu_status():
    try:
        res = subprocess.check_output(
            ["/usr/bin/nvidia-smi", "--query-gpu=utilization.gpu,memory.used,memory.total,temperature.gpu", "--format=csv,noheader,nounits"],
            encoding="utf-8"
        )
        parts = res.strip().split("\n")[0].split(", ")
        gpu_util = parts[0]
        mem_used = parts[1]
        mem_total = parts[2]
        temp = parts[3]

        vram_str = "N/A"
        try:
            vram_str = f"{float(mem_used)/1024:.1f} GB / {float(mem_total)/1024:.1f} GB"
        except Exception:
            vram_str = f"{mem_used} / {mem_total}"

        return {
            "util": f"{gpu_util}%" if gpu_util != "[N/A]" else "N/A",
            "vram": vram_str,
            "temp": f"{temp}°C" if temp != "[N/A]" else "N/A"
        }
    except Exception:
        return {"util": "Offline", "vram": "Offline", "temp": "Offline"}

def get_cpu_temp():
    try:
        temps = []
        for path in glob.glob("/sys/class/thermal/thermal_zone*/temp"):
            with open(path, "r") as f:
                val = int(f.read().strip())
                temps.append(val / 1000.0)
        if temps:
            return f"{max(temps):.1f}°C"
        return "N/A"
    except Exception:
        return "N/A"

def get_cpu_ram_status():
    try:
        import psutil
        cpu = f"{psutil.cpu_percent()}%"
        ram = f"{psutil.virtual_memory().percent}%"
        return cpu, ram
    except Exception:
        return "N/A", "N/A"

def get_mac_status():
    metrics_path = PROCESSED_DIR / "metrics_mac.json"
    if metrics_path.exists():
        try:
            mtime = os.path.getmtime(metrics_path)
            if (time.time() - mtime) < 60:
                with open(metrics_path, "r", encoding="utf-8") as f:
                    return json.load(f)
        except Exception:
            pass
    return {
        "cpu": "Offline",
        "ram": "Offline",
        "gpu": "Offline",
        "temp": "Offline",
        "ollama_status": "Offline",
        "workers": 0,
        "status": "Sleeping"
    }

# 파일별 status 판정 캐시: path -> (mtime, is_success 또는 None(처리중/손상))
# 매 5초마다 전체를 다시 json.load 하면 파일이 20만개 넘는 시점에 감당이 안 되므로
# mtime이 바뀌지 않은 파일은 캐시된 판정을 재사용한다.
_status_cache = {}

def _resolve_status(path, size, mtime):
    cached = _status_cache.get(path)
    if cached is not None and cached[0] == mtime:
        return cached[1]

    if size < 64:
        # 아직 쓰는 중이거나 비정상적으로 작은 파일 -> 완료도 실패도 아닌 "처리중"으로 취급
        _status_cache[path] = (mtime, None)
        return None

    try:
        with open(path, "r", encoding="utf-8") as f:
            meta = json.load(f)
        is_success = meta.get("status") == "success"
    except Exception:
        is_success = None

    _status_cache[path] = (mtime, is_success)
    return is_success

def collect_metrics():
    success_count = 0
    failed_count = 0
    recent_files_mac = []
    recent_files_atom = []

    if METADATA_DIR.exists():
        file_entries = []
        try:
            for entry in os.scandir(METADATA_DIR):
                if entry.is_file() and entry.name.endswith(".metadata.json"):
                    try:
                        stat = entry.stat()
                        file_entries.append((entry.path, entry.name, stat.st_size, stat.st_mtime))
                    except Exception:
                        pass
        except Exception:
            pass

        current_paths = set()
        for path, _, size, mtime in file_entries:
            current_paths.add(path)
            is_success = _resolve_status(path, size, mtime)
            if is_success is True:
                success_count += 1
            elif is_success is False:
                failed_count += 1
            # None(처리중/손상)은 성공도 실패도 아니므로 어느 쪽에도 집계하지 않는다

        # 삭제/이동된 파일의 캐시 항목 정리 (무한 증가 방지)
        for stale_path in (set(_status_cache) - current_paths):
            del _status_cache[stale_path]

        file_entries.sort(key=lambda x: x[3], reverse=True)
        for path, name, _, mtime in file_entries[:150]:
            if len(recent_files_mac) >= 10 and len(recent_files_atom) >= 10:
                break
            try:
                with open(path, "r", encoding="utf-8") as file:
                    meta = json.load(file)
                status = meta.get("status", "success")
                source_path = meta.get("source_path", "")
                outputs = meta.get("outputs", {})
                meta_path_str = outputs.get("metadata", "")
                
                item = {
                    "filename": meta.get("filename", name.replace(".metadata.json", "")),
                    "category": meta.get("ai_summary", {}).get("category", meta.get("category", "미정")),
                    "status": "성공" if status == "success" else "실패",
                    "time": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))
                }
                
                # 경로 명세를 기반으로 로컬 맥북 가공 여부 필터링
                if "/Users/nams" in source_path or "/Users/nams" in meta_path_str:
                    if len(recent_files_mac) < 10:
                        recent_files_mac.append(item)
                else:
                    if len(recent_files_atom) < 10:
                        recent_files_atom.append(item)
            except Exception:
                pass

    processed_count = success_count + failed_count
    with total_files_lock:
        # 스캔 추정치가 실제 처리량보다 뒤처져도(NAS 재스캔 지연 등) 210%처럼 100%를 넘겨 보이지 않도록 하한을 처리량으로 고정
        total_files = max(total_files_estimate, processed_count)
    progress_percent = (processed_count / total_files) * 100 if total_files > 0 else 0
    remaining_count = max(total_files - processed_count, 0)

    cpu_val, ram_val = get_cpu_ram_status()
    gpu_info = get_gpu_status()
    mac_data = get_mac_status()

    return {
        "success_count": success_count,
        "failed_count": failed_count,
        "processed_count": processed_count,
        "progress_percent": round(progress_percent, 2),
        "remaining_count": remaining_count,
        "total_files": total_files,
        "atom": {
            "cpu": cpu_val,
            "ram": ram_val,
            "temp": get_cpu_temp(),
            "gpu_util": gpu_info["util"],
            "gpu_vram": gpu_info["vram"],
            "gpu_temp": gpu_info["temp"]
        },
        "mac": {
            "cpu": mac_data.get("cpu", "Offline"),
            "ram": mac_data.get("ram", "Offline"),
            "gpu": mac_data.get("gpu", "Offline"),
            "temp": mac_data.get("temp", "Offline"),
            "status": mac_data.get("status", "Offline"),
            "ollama": mac_data.get("ollama_status", "Offline"),
            "workers": mac_data.get("workers", 0)
        },
        "recent_files_mac": recent_files_mac,
        "recent_files_atom": recent_files_atom
    }

# 전역 캐시 딕셔너리
cached_data = {
    "success_count": 0, "failed_count": 0, "processed_count": 0, "progress_percent": 0.0, "remaining_count": 0, "total_files": total_files_estimate,
    "atom": {"cpu": "N/A", "ram": "N/A", "temp": "N/A", "gpu_util": "N/A", "gpu_vram": "N/A", "gpu_temp": "N/A"},
    "mac": {"cpu": "Offline", "ram": "Offline", "gpu": "Offline", "temp": "Offline", "status": "Offline", "ollama": "Offline", "workers": 0},
    "recent_files": []
}

def total_files_updater_loop():
    """전수조사 대상 총량(/mnt 내 확장자 매칭 파일 수)을 무겁지 않게 주기적으로 재계산.
    NAS 트리 전체를 find로 훑는 건 느릴 수 있어 5초짜리 메트릭 루프와 분리하고,
    타임아웃 시 이전 추정치를 그대로 유지한다."""
    global total_files_estimate
    find_args = ["find", NAS_SCAN_ROOT, "-type", "f", "("]
    for i, ext in enumerate(TARGET_EXTENSIONS):
        if i > 0:
            find_args.append("-o")
        find_args += ["-iname", f"*{ext}"]
    find_args.append(")")

    while True:
        try:
            result = subprocess.run(find_args, capture_output=True, text=True, timeout=1800)
            count = sum(1 for line in result.stdout.splitlines() if line.strip())
            if count > 0:
                with total_files_lock:
                    total_files_estimate = count
                print(f"[Total Files Updater] /mnt 대상 파일 재계산: {count}개", flush=True)
        except Exception as e:
            print(f"[Total Files Updater Error] {e}", file=sys.stderr, flush=True)
        time.sleep(7200)  # 2시간마다 재계산 (NAS I/O 부하 고려)

def cache_updater_loop():
    global cached_data
    print("[Cache Daemon Started] Background metrics collector running...", flush=True)
    while True:
        try:
            # 5초마다 넌블로킹 백그라운드 스캔 및 리소스 수집
            latest = collect_metrics()
            cached_data = latest
        except Exception as e:
            print(f"[Cache Daemon Error] {e}", file=sys.stderr, flush=True)
        time.sleep(5)

class LiveMonitorHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass # 로그 출력 억제하여 디스크 I/O 절약

    def do_GET(self):
        if self.path == "/api/metrics":
            try:
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(json.dumps(cached_data, ensure_ascii=False).encode("utf-8"))
            except (ConnectionError, BrokenPipeError):
                pass # 브라우저 중도 이탈로 인한 BrokenPipeError 예방 (서버 멈춤 완전 차단)
            except Exception as e:
                print(f"[API Response Error] {e}", file=sys.stderr)
        elif self.path == "/" or self.path == "/index.html":
            try:
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(HTML_TEMPLATE.encode("utf-8"))
            except (ConnectionError, BrokenPipeError):
                pass
            except Exception as e:
                print(f"[API HTML Error] {e}", file=sys.stderr)
        else:
            try:
                self.send_error(404)
            except Exception:
                pass

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aurum Live Dashboard</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&family=Noto+Sans+KR:wght@300;400;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-color: #0b0f19;
            --card-bg: rgba(30, 41, 59, 0.45);
            --border-color: rgba(255, 255, 255, 0.08);
            --accent-blue: #38bdf8;
            --accent-green: #4ade80;
            --accent-red: #f87171;
            --text-main: #f8fafc;
            --text-sub: #94a3b8;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Outfit', 'Noto Sans KR', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-main);
            padding: 30px;
            overflow-x: hidden;
            background-image: radial-gradient(circle at 10% 20%, rgba(56, 189, 248, 0.05) 0%, transparent 40%),
                              radial-gradient(circle at 90% 80%, rgba(74, 222, 128, 0.03) 0%, transparent 40%);
            background-attachment: fixed;
        }

        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 30px;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 20px;
        }

        .header-title h1 {
            font-size: 1.8rem;
            font-weight: 700;
            letter-spacing: -0.02em;
            background: linear-gradient(to right, #38bdf8, #4ade80);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .header-title p {
            font-size: 0.9rem;
            color: var(--text-sub);
            margin-top: 5px;
        }

        .live-badge {
            background: rgba(74, 222, 128, 0.15);
            color: var(--accent-green);
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 6px;
            border: 1px solid rgba(74, 222, 128, 0.25);
        }

        .live-dot {
            width: 8px;
            height: 8px;
            background-color: var(--accent-green);
            border-radius: 50%;
            animation: pulse 1.5s infinite;
        }

        @keyframes pulse {
            0% { transform: scale(0.9); opacity: 0.5; }
            50% { transform: scale(1.2); opacity: 1; }
            100% { transform: scale(0.9); opacity: 0.5; }
        }

        .metric-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            margin-bottom: 30px;
        }

        .metric-card {
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            padding: 24px;
            text-align: center;
            backdrop-filter: blur(12px);
            transition: transform 0.2s, border-color 0.2s;
        }

        .metric-card:hover {
            border-color: rgba(56, 189, 248, 0.2);
            transform: translateY(-2px);
        }

        .metric-value {
            font-size: 2.2rem;
            font-weight: 700;
            color: var(--accent-blue);
            margin-bottom: 8px;
            transition: color 0.3s;
        }

        .metric-label {
            font-size: 0.85rem;
            color: var(--text-sub);
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        .progress-section {
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            padding: 24px;
            margin-bottom: 30px;
            backdrop-filter: blur(12px);
        }

        .progress-info {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
        }

        .progress-title {
            font-weight: 600;
            font-size: 1rem;
        }

        .progress-percentage {
            font-weight: 700;
            color: var(--accent-blue);
            font-size: 1.1rem;
        }

        .progress-bar-bg {
            background: rgba(255, 255, 255, 0.05);
            height: 12px;
            border-radius: 6px;
            overflow: hidden;
            border: 1px solid var(--border-color);
        }

        .progress-bar-fill {
            background: linear-gradient(to right, #38bdf8, #4ade80);
            height: 100%;
            width: 0%;
            border-radius: 6px;
            transition: width 0.8s cubic-bezier(0.4, 0, 0.2, 1);
        }

        .content-layout {
            display: grid;
            grid-template-columns: 1fr 1.3fr 1.3fr;
            gap: 25px;
        }

        .panel-title {
            font-size: 1.1rem;
            font-weight: 600;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 8px;
            border-left: 3px solid var(--accent-blue);
            padding-left: 10px;
        }

        .hw-section {
            display: flex;
            flex-direction: column;
            gap: 24px;
        }

        .hw-card {
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            padding: 24px;
            backdrop-filter: blur(12px);
        }

        .hw-card-header {
            font-weight: 700;
            font-size: 0.95rem;
            margin-bottom: 16px;
            color: var(--text-main);
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 10px;
            display: flex;
            justify-content: space-between;
        }

        .hw-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 15px;
        }

        .hw-metric {
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.03);
            border-radius: 10px;
            padding: 12px;
            text-align: center;
        }

        .hw-metric-value {
            font-size: 1.1rem;
            font-weight: 600;
            color: var(--text-main);
            margin-top: 4px;
        }

        .hw-metric-label {
            font-size: 0.75rem;
            color: var(--text-sub);
        }

        .history-section {
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            padding: 24px;
            backdrop-filter: blur(12px);
            display: flex;
            flex-direction: column;
            height: 100%;
        }

        .table-container {
            flex-grow: 1;
            overflow-y: auto;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            text-align: left;
            font-size: 0.85rem;
        }

        th {
            color: var(--text-sub);
            font-weight: 600;
            padding: 12px;
            border-bottom: 1px solid var(--border-color);
        }

        td {
            padding: 12px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.03);
            color: #cbd5e1;
        }

        tr:hover td {
            background: rgba(255, 255, 255, 0.01);
            color: var(--text-main);
        }

        .badge {
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 0.75rem;
            font-weight: 600;
        }

        .badge-success {
            background: rgba(74, 222, 128, 0.12);
            color: var(--accent-green);
        }

        .badge-fail {
            background: rgba(248, 113, 113, 0.12);
            color: var(--accent-red);
        }
    </style>
</head>
<body>
    <!-- 하이테크 실시간 별무리 파티클 배경 -->
    <canvas id="particle-canvas" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none; opacity: 0.35;"></canvas>

    <div class="header">
        <div class="header-title">
            <h1>⚕ 아우룸 AI 실시간 관제 시스템 (Aurum Live Monitor)</h1>
            <p>1차 전수조사 진행률 및 시스템 자원 실시간 모니터링 (No Blinking, Low Memory)</p>
        </div>
        <div class="live-badge">
            <div class="live-dot"></div>
            <span>LIVE (2s Refresh)</span>
        </div>
    </div>

    <!-- 진행 지표 카드 그리드 -->
    <div class="metric-grid">
        <div class="metric-card">
            <div class="metric-value" id="val-processed">0</div>
            <div class="metric-label">총 가공 처리 파일</div>
        </div>
        <div class="metric-card">
            <div class="metric-value" style="color: var(--accent-green);" id="val-success">0</div>
            <div class="metric-label">가공 성공 파일</div>
        </div>
        <div class="metric-card">
            <div class="metric-value" style="color: var(--accent-red);" id="val-failed">0</div>
            <div class="metric-label">가공 실패 파일</div>
        </div>
        <div class="metric-card">
            <div class="metric-value" style="color: #cbd5e1;" id="val-remaining">0</div>
            <div class="metric-label">남은 대기 파일</div>
        </div>
    </div>

    <!-- 진행 바 세션 -->
    <div class="progress-section">
        <div class="progress-info">
            <div class="progress-title">전수 조사 진행률</div>
            <div class="progress-percentage" id="progress-text">0%</div>
        </div>
        <div class="progress-bar-bg">
            <div class="progress-bar-fill" id="progress-bar"></div>
        </div>
    </div>

    <!-- 하드웨어 자원 및 이력 분할 레이아웃 -->
    <div class="content-layout">
        <!-- 좌측: 하드웨어 리소스 -->
        <div class="hw-section">
            <h2 class="panel-title">⚙️ 실시간 하드웨어 리소스</h2>

            <!-- ATOM SERVER -->
            <div class="hw-card">
                <div class="hw-card-header">
                    <span>🤖 ATOM SERVER (아톰 서버 - 8 Workers)</span>
                    <span style="color: var(--accent-blue)">Online</span>
                </div>
                <div class="hw-grid">
                    <div class="hw-metric">
                        <div class="hw-metric-label">CPU 사용량</div>
                        <div class="hw-metric-value" id="atom-cpu">-</div>
                    </div>
                    <div class="hw-metric">
                        <div class="hw-metric-label">RAM 사용량</div>
                        <div class="hw-metric-value" id="atom-ram">-</div>
                    </div>
                    <div class="hw-metric">
                        <div class="hw-metric-label">CPU 최고온도</div>
                        <div class="hw-metric-value" id="atom-temp">-</div>
                    </div>
                    <div class="hw-metric">
                        <div class="hw-metric-label">GPU 로드율</div>
                        <div class="hw-metric-value" id="atom-gpu-util">-</div>
                    </div>
                    <div class="hw-metric">
                        <div class="hw-metric-label">GPU 온도</div>
                        <div class="hw-metric-value" id="atom-gpu-temp">-</div>
                    </div>
                    <div class="hw-metric">
                        <div class="hw-metric-label">VRAM 점유율</div>
                        <div class="hw-metric-value" id="atom-gpu-vram">-</div>
                    </div>
                </div>
            </div>

            <!-- AURUM MACBOOK -->
            <div class="hw-card">
                <div class="hw-card-header">
                    <span>💻 AURUM MACBOOK (아우룸 맥북)</span>
                    <span style="color: var(--accent-green)" id="mac-title-status">Online</span>
                </div>
                <div class="hw-grid">
                    <div class="hw-metric">
                        <div class="hw-metric-label">맥북 CPU 사용량</div>
                        <div class="hw-metric-value" id="mac-cpu">-</div>
                    </div>
                    <div class="hw-metric">
                        <div class="hw-metric-label">맥북 RAM 사용량</div>
                        <div class="hw-metric-value" id="mac-ram">-</div>
                    </div>
                    <div class="hw-metric">
                        <div class="hw-metric-label">맥북 내부온도</div>
                        <div class="hw-metric-value" id="mac-temp">-</div>
                    </div>
                    <div class="hw-metric">
                        <div class="hw-metric-label">맥북 GPU 사용량</div>
                        <div class="hw-metric-value" id="mac-gpu">-</div>
                    </div>
                    <div class="hw-metric">
                        <div class="hw-metric-label">가공 상태</div>
                        <div class="hw-metric-value" style="font-size: 0.9rem;" id="mac-status">-</div>
                    </div>
                    <div class="hw-metric">
                        <div class="hw-metric-label">Ollama 상태</div>
                        <div class="hw-metric-value" style="font-size: 0.8rem; overflow: hidden; text-overflow: ellipsis;" id="mac-ollama">-</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- 가운데: 아우룸 맥북 가공 파일 이력 -->
        <div class="history-section">
            <h2 class="panel-title">💻 AURUM MACBOOK 가공 이력</h2>
            <div class="table-container">
                <table>
                    <thead>
                        <tr>
                            <th>파일명</th>
                            <th>분류군</th>
                            <th>상태</th>
                            <th>시각</th>
                        </tr>
                    </thead>
                    <tbody id="mac-history-table-body">
                        <!-- Javascript 가 실시간 삽입 -->
                    </tbody>
                </table>
            </div>
        </div>

        <!-- 우측: 아톰 서버 가공 파일 이력 -->
        <div class="history-section">
            <h2 class="panel-title">🤖 ATOM SERVER 가공 이력</h2>
            <div class="table-container">
                <table>
                    <thead>
                        <tr>
                            <th>파일명</th>
                            <th>분류군</th>
                            <th>상태</th>
                            <th>시각</th>
                        </tr>
                    </thead>
                    <tbody id="atom-history-table-body">
                        <!-- Javascript 가 실시간 삽입 -->
                    </tbody>
                </table>
            </div>
        </div>
    </div>

    <script>
        async function fetchMetrics() {
            try {
                const response = await fetch('/api/metrics');
                if (!response.ok) throw new Error('API Response Error');
                const data = await response.json();

                // 1. 최상단 지표 갱신
                document.getElementById('val-processed').innerText = data.processed_count.toLocaleString();
                document.getElementById('val-success').innerText = data.success_count.toLocaleString();
                document.getElementById('val-failed').innerText = data.failed_count.toLocaleString();
                document.getElementById('val-remaining').innerText = data.remaining_count.toLocaleString();

                // 2. 진행률 바 갱신
                document.getElementById('progress-text').innerText = data.progress_percent + '%';
                document.getElementById('progress-bar').style.width = data.progress_percent + '%';

                // 3. 아톰 리소스 갱신
                document.getElementById('atom-cpu').innerText = data.atom.cpu;
                document.getElementById('atom-ram').innerText = data.atom.ram;
                document.getElementById('atom-temp').innerText = data.atom.temp;
                document.getElementById('atom-gpu-util').innerText = data.atom.gpu_util;
                document.getElementById('atom-gpu-temp').innerText = data.atom.gpu_temp;
                document.getElementById('atom-gpu-vram').innerText = data.atom.gpu_vram;

                // 4. 맥북 리소스 갱신
                document.getElementById('mac-cpu').innerText = data.mac.cpu;
                document.getElementById('mac-ram').innerText = data.mac.ram;
                document.getElementById('mac-temp').innerText = data.mac.temp;
                document.getElementById('mac-gpu').innerText = data.mac.gpu;
                document.getElementById('mac-status').innerText = data.mac.status;
                document.getElementById('mac-ollama').innerText = data.mac.ollama;

                const macTitle = `💻 AURUM MACBOOK (아우룸 맥북 - ${data.mac.workers} Workers)`;
                document.getElementById('mac-title-status').previousElementSibling.innerText = macTitle;
                document.getElementById('mac-title-status').innerText = data.mac.cpu === 'Offline' ? 'Offline' : 'Online';
                document.getElementById('mac-title-status').style.color = data.mac.cpu === 'Offline' ? 'var(--accent-red)' : 'var(--accent-green)';

                // 5. 가공 이력 테이블 갱신 (부드럽게 각각 덮어쓰기)
                const buildTableRows = (files) => {
                    let html = '';
                    if (files && files.length > 0) {
                        files.forEach(file => {
                            const badgeClass = file.status === '성공' ? 'badge-success' : 'badge-fail';
                            html += `
                                <tr>
                                    <td>${file.filename}</td>
                                    <td>${file.category}</td>
                                    <td><span class="badge ${badgeClass}">${file.status}</span></td>
                                    <td>${file.time}</td>
                                </tr>
                            `;
                        });
                    } else {
                        html = '<tr><td colspan="4" style="text-align: center; color: var(--text-sub);">실시간 대기 중...</td></tr>';
                    }
                    return html;
                };

                document.getElementById('mac-history-table-body').innerHTML = buildTableRows(data.recent_files_mac);
                document.getElementById('atom-history-table-body').innerHTML = buildTableRows(data.recent_files_atom);

            } catch (error) {
                console.error("Failed to sync metrics:", error);
            }
        }

        // 초기 로드 후 2초마다 깜빡임 없이 데이터만 리액티브 갱신
        fetchMetrics();
        setInterval(fetchMetrics, 2000);

        // --- 실시간 별무리 파티클 유영 효과 ---
        const canvas = document.getElementById('particle-canvas');
        const ctx = canvas.getContext('2d');
        let width = canvas.width = window.innerWidth;
        let height = canvas.height = window.innerHeight;

        window.addEventListener('resize', () => {
            width = canvas.width = window.innerWidth;
            height = canvas.height = window.innerHeight;
        });

        const particles = [];
        // 작은 점들 45개 생성
        for (let i = 0; i < 45; i++) {
            particles.push({
                x: Math.random() * width,
                y: Math.random() * height,
                vx: (Math.random() - 0.5) * 0.35,
                vy: (Math.random() - 0.5) * 0.35,
                r: Math.random() * 2 + 1
            });
        }

        function animate() {
            ctx.clearRect(0, 0, width, height);
            ctx.fillStyle = 'rgba(56, 189, 248, 0.45)';
            ctx.strokeStyle = 'rgba(56, 189, 248, 0.05)';

            particles.forEach(p => {
                p.x += p.vx;
                p.y += p.vy;

                if (p.x < 0 || p.x > width) p.vx *= -1;
                if (p.y < 0 || p.y > height) p.vy *= -1;

                ctx.beginPath();
                ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
                ctx.fill();
            });

            for (let i = 0; i < particles.length; i++) {
                for (let j = i + 1; j < particles.length; j++) {
                    const dist = Math.hypot(particles[i].x - particles[j].x, particles[i].y - particles[j].y);
                    if (dist < 130) {
                        ctx.beginPath();
                        ctx.moveTo(particles[i].x, particles[i].y);
                        ctx.lineTo(particles[j].x, particles[j].y);
                        ctx.stroke();
                    }
                }
            }
            requestAnimationFrame(animate);
        }
        animate();
    </script>
</body>
</html>
"""

def run(server_class=HTTPServer, handler_class=LiveMonitorHandler, port=8502):
    # 백그라운드 캐시 수집 데몬 활성화
    t = threading.Thread(target=cache_updater_loop, daemon=True)
    t.start()

    # 전수조사 대상 총량 백그라운드 재계산 데몬 활성화
    t2 = threading.Thread(target=total_files_updater_loop, daemon=True)
    t2.start()

    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"[Live Server Started] Serving Live Dashboard on port {port}...", flush=True)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()
        print("[Live Server Stopped]")

if __name__ == '__main__':
    run()
