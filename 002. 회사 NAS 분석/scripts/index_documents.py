#!/usr/bin/env python3
"""Build a FAISS index from processed text artifacts."""
import argparse
from datetime import datetime, timezone, timedelta
import json
from pathlib import Path
import sys
from typing import Iterable


DEFAULT_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_STATE = BASE_DIR / "data" / "processed" / "state.json"

try:
    from slack_notify import send_slack_message, slack_enabled
except Exception:
    def send_slack_message(*args, **kwargs):
        return False

    def slack_enabled() -> bool:
        return False


def now_iso() -> str:
    kst = timezone(timedelta(hours=9))
    return datetime.now(kst).isoformat(timespec="seconds")


def update_state(state_path: Path, event: dict) -> None:
    state_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        state = json.loads(state_path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        state = {"watchers": {}, "recent_events": []}

    event = {"timestamp": now_iso(), **event}
    state["index"] = {
        "last_event": event.get("type"),
        "last_event_at": event["timestamp"],
        "last_status": event.get("status"),
        "index_dir": event.get("index_dir"),
        "document_count": event.get("document_count"),
        "model_name": event.get("model_name"),
        "error": event.get("error"),
    }
    state.setdefault("recent_events", []).insert(0, event)
    state["recent_events"] = state["recent_events"][:50]
    state["updated_at"] = event["timestamp"]
    tmp_path = state_path.with_suffix(state_path.suffix + ".tmp")
    tmp_path.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp_path.replace(state_path)


def iter_text_files(processed_dir: Path) -> Iterable[Path]:
    text_dir = processed_dir / "text"
    if not text_dir.exists():
        return []
    return sorted(path for path in text_dir.glob("*.txt") if path.is_file())


def chunk_text(text: str, max_chars: int) -> list[str]:
    cleaned = "\n".join(line.strip() for line in text.splitlines() if line.strip())
    if not cleaned:
        return []
    return [cleaned[i : i + max_chars] for i in range(0, len(cleaned), max_chars)]


def load_metadata(processed_dir: Path) -> dict[str, dict]:
    metadata_dir = processed_dir / "metadata"
    metadata_by_text = {}
    if not metadata_dir.exists():
        return metadata_by_text

    for metadata_path in metadata_dir.glob("*.metadata.json"):
        try:
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        text_output = metadata.get("outputs", {}).get("text")
        if text_output:
            metadata_by_text[str(Path(text_output).resolve())] = metadata
    return metadata_by_text


def build_documents(processed_dir: Path, chunk_chars: int) -> list[dict]:
    metadata_by_text = load_metadata(processed_dir)
    documents = []
    for text_path in iter_text_files(processed_dir):
        text = text_path.read_text(encoding="utf-8", errors="replace")
        chunks = chunk_text(text, chunk_chars)
        metadata = metadata_by_text.get(str(text_path.resolve()), {})
        for chunk_index, chunk in enumerate(chunks):
            documents.append(
                {
                    "id": f"{text_path.stem}:{chunk_index}",
                    "text_path": str(text_path),
                    "chunk_index": chunk_index,
                    "text": chunk,
                    "source_path": metadata.get("source_path"),
                    "source_name": metadata.get("source_name", text_path.name),
                    "device_name": metadata.get("device_name"),
                    "processed_at": metadata.get("processed_at"),
                }
            )
    return documents


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--processed-dir", default="data/processed", help="추출 결과 루트")
    parser.add_argument("--index-dir", default="data/indexes/faiss", help="FAISS 인덱스 저장 경로")
    parser.add_argument("--model-name", default=DEFAULT_MODEL, help="임베딩 모델명")
    parser.add_argument("--chunk-chars", type=int, default=1200, help="텍스트 청크 최대 길이")
    parser.add_argument("--state-file", default=str(DEFAULT_STATE), help="Dashboard가 읽을 파이프라인 상태 JSON 경로")
    args = parser.parse_args()
    state_file = Path(args.state_file).expanduser()
    if not state_file.is_absolute():
        state_file = Path.cwd() / state_file

    try:
        import faiss
        import numpy as np
        from sentence_transformers import SentenceTransformer
    except ImportError as exc:
        error = f"index dependency missing: {exc}"
        update_state(state_file, {"type": "index_failed", "status": "failed", "error": error})
        if slack_enabled():
            send_slack_message(f"색인 실패: {error}")
        print(error, file=sys.stderr)
        return 1

    processed_dir = Path(args.processed_dir).expanduser().resolve()
    index_dir = Path(args.index_dir).expanduser()
    if not index_dir.is_absolute():
        index_dir = Path.cwd() / index_dir
    index_dir.mkdir(parents=True, exist_ok=True)

    documents = build_documents(processed_dir, args.chunk_chars)
    if not documents:
        error = f"no processed text documents found in {processed_dir}"
        update_state(
            state_file,
            {
                "type": "index_failed",
                "status": "failed",
                "index_dir": str(index_dir),
                "model_name": args.model_name,
                "document_count": 0,
                "error": error,
            },
        )
        if slack_enabled():
            send_slack_message(f"색인 실패: {error}")
        print(error, file=sys.stderr)
        return 1

    model = SentenceTransformer(args.model_name, device='cpu')
    embeddings = model.encode(
        [document["text"] for document in documents],
        convert_to_numpy=True,
        normalize_embeddings=True,
        show_progress_bar=False,
    )
    embeddings = np.asarray(embeddings, dtype="float32")

    index = faiss.IndexFlatIP(embeddings.shape[1])
    index.add(embeddings)
    faiss.write_index(index, str(index_dir / "index.faiss"))

    mapping = {
        "model_name": args.model_name,
        "metric": "inner_product_normalized",
        "document_count": len(documents),
        "documents": documents,
    }
    (index_dir / "mapping.json").write_text(
        json.dumps(mapping, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    update_state(
        state_file,
        {
            "type": "index_completed",
            "status": "success",
            "index_dir": str(index_dir),
            "model_name": args.model_name,
            "document_count": len(documents),
        },
    )
    if slack_enabled():
        send_slack_message(f"색인 완료: {len(documents)}개 문서, {index_dir}")
    print(f"indexed_documents={len(documents)} index_dir={index_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
