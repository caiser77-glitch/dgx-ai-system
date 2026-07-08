#!/usr/bin/env python3
"""로컬 임시 디렉터리에서 005 협업 파이프라인 전체 흐름을 검증한다."""

import importlib.util
import json
import shutil
import sys
import tempfile
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    sys.dont_write_bytecode = True
    pipeline_engine = load_module("pipeline_engine", SCRIPT_DIR / "pipeline_engine.py")
    tracker = load_module("track_pipeline_status", SCRIPT_DIR / "track_pipeline_status.py")
    aurum_deployer = load_module("aurum_deployer", SCRIPT_DIR / "aurum_deployer.py")

    root = Path(tempfile.mkdtemp(prefix="pipeline005_e2e_"))
    try:
        tracker.ensure_stages(root)
        raw = root / tracker.STAGES["raw"]
        job_id = "TEST-PIPELINE-005"
        (raw / f"{job_id}.summary.md").write_text(
            "---\nstatus: raw_analyzed\nassigned_agent: Mohave\nyear_vendor: 2026 LH\nproject_name: 경인사업\nclass_name: 양서파충류\n---\n\n1차 요약",
            encoding="utf-8",
        )
        (raw / f"{job_id}.result.json").write_text(
            json.dumps(
                {
                    "metadata": {"job_id": job_id, "timestamp": "2026-07-08T15:00:00+09:00"},
                    "payload": {
                        "metrics": {"species_count": 3, "survey_points": 2},
                        "spatial_observations": [
                            {"lat": 37.1, "lon": 127.2, "count": 5, "note": "정상"}
                        ],
                    },
                },
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )

        engine = pipeline_engine.PipelineEngine(str(raw))
        engine.process_job(f"{job_id}.summary.md")

        drafting_draft = root / tracker.STAGES["drafting"] / f"{job_id}.draft.md"
        tracker.update_frontmatter(drafting_draft, {"status": "review_pending", "assigned_agent": "Aurum"})
        moved = tracker.scan_once(root)
        assert moved == [job_id], moved

        deployer = aurum_deployer.AurumDeployer(
            str(root / tracker.STAGES["review"]),
            str(root / "NAS_Distribution"),
        )
        deployer.process_review_pending(f"{job_id}.draft.md")

        assert (root / "NAS_Distribution" / f"{job_id}.hwp").exists()
        assert (root / "NAS_Distribution" / f"{job_id}.pdf").exists()
        published_draft = root / tracker.STAGES["published"] / f"{job_id}.draft.md"
        assert published_draft.exists()
        assert "status: published" in published_draft.read_text(encoding="utf-8")
        print("E2E OK", root)
    finally:
        shutil.rmtree(root)


if __name__ == "__main__":
    main()
