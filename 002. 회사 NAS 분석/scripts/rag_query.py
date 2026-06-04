#!/usr/bin/env python3
"""Search the local FAISS index and optionally send context to a local LLM."""
import argparse
import json
import os
from pathlib import Path
import sys
import urllib.error
import urllib.request


def load_index(index_dir: Path):
    try:
        import faiss
        from sentence_transformers import SentenceTransformer
    except ImportError as exc:
        raise RuntimeError(f"rag dependency missing: {exc}") from exc

    mapping_path = index_dir / "mapping.json"
    faiss_path = index_dir / "index.faiss"
    if not mapping_path.exists() or not faiss_path.exists():
        raise RuntimeError(f"index files missing in {index_dir}")

    mapping = json.loads(mapping_path.read_text(encoding="utf-8"))
    index = faiss.read_index(str(faiss_path))
    model = SentenceTransformer(mapping["model_name"])
    return index, mapping, model


def search(query: str, index, mapping: dict, model, top_k: int) -> list[dict]:
    embedding = model.encode(
        [query],
        convert_to_numpy=True,
        normalize_embeddings=True,
        show_progress_bar=False,
    ).astype("float32")
    scores, indices = index.search(embedding, top_k)
    documents = mapping.get("documents", [])
    results = []
    for score, idx in zip(scores[0], indices[0]):
        if idx < 0 or idx >= len(documents):
            continue
        document = dict(documents[idx])
        document["score"] = float(score)
        results.append(document)
    return results


def build_prompt(query: str, results: list[dict]) -> str:
    context_blocks = []
    for idx, result in enumerate(results, 1):
        context_blocks.append(
            "\n".join(
                [
                    f"[{idx}] source: {result.get('source_name')}",
                    f"path: {result.get('source_path') or result.get('text_path')}",
                    result.get("text", ""),
                ]
            )
        )
    return (
        "다음 내부 문서 컨텍스트만 근거로 한국어로 답변하십시오. "
        "근거가 부족하면 부족하다고 말하십시오.\n\n"
        f"질문: {query}\n\n"
        "컨텍스트:\n"
        + "\n\n".join(context_blocks)
    )


def call_llm(prompt: str, model: str, endpoint: str) -> dict:
    is_openai_compat = "/v1/" in endpoint
    
    if is_openai_compat:
        data_dict = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.2,
            "max_tokens": 80,
            "stream": False,
        }
    else:
        data_dict = {
            "model": model,
            "prompt": prompt,
            "stream": False,
        }

    payload = json.dumps(data_dict).encode("utf-8")
    request = urllib.request.Request(
        endpoint,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        # 대용량 모델 구동 시간 및 연산 지연을 위해 타임아웃 300초 적용
        with urllib.request.urlopen(request, timeout=300) as response:
            resp_data = json.loads(response.read().decode("utf-8"))
            if is_openai_compat:
                choices = resp_data.get("choices", [])
                if choices:
                    content = choices[0].get("message", {}).get("content")
                    return {"response": content}
                return {"response": None}
            return resp_data
    except urllib.error.URLError as exc:
        raise RuntimeError(str(exc)) from exc


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", required=True, help="검색 또는 RAG 질의")
    parser.add_argument("--index-dir", default="data/indexes/faiss", help="FAISS 인덱스 경로")
    parser.add_argument("--top-k", type=int, default=5, help="검색 결과 수")
    parser.add_argument("--model", default=os.getenv("OLLAMA_MODEL"), help="Ollama 또는 vLLM 모델명")
    parser.add_argument(
        "--llm-endpoint",
        dest="llm_endpoint",
        default=os.getenv("LLM_ENDPOINT", os.getenv("OLLAMA_ENDPOINT", "http://localhost:11434/api/generate")),
        help="Ollama 또는 vLLM API 엔드포인트 (v1/chat/completions 포함 시 OpenAI 호환)",
    )
    parser.add_argument("--ollama-endpoint", help=argparse.SUPPRESS)
    args = parser.parse_args()

    # Legacy endpoint parameter fallback
    endpoint = args.llm_endpoint
    if args.ollama_endpoint:
        endpoint = args.ollama_endpoint

    index_dir = Path(args.index_dir).expanduser()
    if not index_dir.is_absolute():
        index_dir = Path.cwd() / index_dir

    try:
        index, mapping, embedding_model = load_index(index_dir)
        results = search(args.query, index, mapping, embedding_model, args.top_k)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    prompt = build_prompt(args.query, results)
    response = {
        "query": args.query,
        "model": args.model,
        "answer": None,
        "model_error": None,
        "references": [
            {
                "source_name": result.get("source_name"),
                "source_path": result.get("source_path"),
                "text_path": result.get("text_path"),
                "score": result.get("score"),
                "device_name": result.get("device_name"),
                "processed_at": result.get("processed_at"),
            }
            for result in results
        ],
        "retrieved_context": results,
    }

    if args.model:
        try:
            llm_response = call_llm(prompt, args.model, endpoint)
            response["answer"] = llm_response.get("response")
        except RuntimeError as exc:
            response["model_error"] = str(exc)

    print(json.dumps(response, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
