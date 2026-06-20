# -*- coding: utf-8 -*-
"""
아우룸생태연구소 에르메스 NAS 분류기 사용자 피드백 수집 및 자가학습 텔레그램 봇
"""

import os
import sys
import re
import sqlite3
import logging
import subprocess
import json
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, CommandHandler, filters

# 로깅 설정
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger("TelegramFeedbackBot")
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("telegram").setLevel(logging.WARNING)

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
ALLOWED_USER_ID = int(os.environ.get("ALLOWED_USER_ID", "0"))
DB_PATH = "/home/caiser77/dgx_workspace/004. 에르메스 NAS 분류기/data/aurum_nas_rules.db"


PENDING_QUEUE_PATH = "/home/caiser77/dgx_workspace/004. 에르메스 NAS 분류기/data/pending_queue.jsonl"
LAST_PENDING_PATH = "/home/caiser77/dgx_workspace/004. 에르메스 NAS 분류기/data/last_pending.json"


def is_pending_briefing_request(user_text: str) -> bool:
    """월요일 처리용 분류 대기 목록 요청인지 판별합니다."""
    normalized = user_text.replace(" ", "").lower()
    return any(kw in normalized for kw in ["브리핑", "월요일", "대기", "보류", "목록", "리스트", "pending"])


def load_pending_items(limit: int = 10) -> list[dict]:
    """분류 피드백 대기 큐를 최신순으로 읽습니다."""
    items_by_path = {}
    if os.path.exists(PENDING_QUEUE_PATH):
        with open(PENDING_QUEUE_PATH, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    item = json.loads(line)
                except json.JSONDecodeError:
                    continue
                key = item.get("original_path") or item.get("source_name")
                if not key:
                    continue
                items_by_path[key] = item

    pending = [item for item in items_by_path.values() if item.get("status", "pending") == "pending"]
    pending.sort(key=lambda item: item.get("created_at", ""), reverse=True)

    if not pending and os.path.exists(LAST_PENDING_PATH):
        try:
            with open(LAST_PENDING_PATH, "r", encoding="utf-8") as f:
                pending = [json.load(f)]
        except Exception as e:
            logger.error(f"Failed to read last_pending.json: {e}")

    return pending[:limit]


def build_pending_briefing(limit: int = 10) -> str:
    items = load_pending_items(limit=limit)
    if not items:
        return (
            "✅ **월요일 처리 대기 중인 분류 모호성 항목이 없습니다.**\n\n"
            "새 모호성 감지부터는 대기 큐에 누적 저장됩니다."
        )

    lines = [f"📌 **월요일 처리 필요 항목: {len(items)}건**"]
    for idx, item in enumerate(items, 1):
        source_name = item.get("source_name", "이름 없음")
        project_name = item.get("project_name", "미정")
        inferred_class = item.get("inferred_class", item.get("class_name", "미정"))
        question = item.get("question") or "분류 승인 또는 정정이 필요합니다."
        original_path = item.get("original_path", "경로 없음")
        preview = (item.get("preview") or "").strip()
        if len(preview) > 220:
            preview = preview[:220].rstrip() + "..."
        lines.extend([
            "",
            f"{idx}. **{source_name}**",
            f"- 사업명: {project_name}",
            f"- 추론 분류군: {inferred_class}",
            f"- 확인 필요: {question}",
            f"- NAS 경로: {original_path}",
        ])
        if preview:
            lines.append(f"- 근거: {preview}")

    lines.extend([
        "",
        "처리하려면 해당 ⚠️ **[분류 모호성 감지]** 메시지나 **[피드백 대기 알림]**에 답장으로 '승인. 조류로 분류해'처럼 보내주세요.",
    ])
    return "\n".join(lines)


def mark_pending_resolved(original_path: str) -> None:
    if not original_path or not os.path.exists(PENDING_QUEUE_PATH):
        return
    try:
        items = []
        with open(PENDING_QUEUE_PATH, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    item = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if item.get("original_path") == original_path:
                    item["status"] = "resolved"
                items.append(item)
        with open(PENDING_QUEUE_PATH, "w", encoding="utf-8") as f:
            for item in items:
                f.write(json.dumps(item, ensure_ascii=False) + "\n")
    except Exception as e:
        logger.error(f"Failed to mark pending item resolved: {e}")


def run_rag_query(query: str) -> str:
    """아톰 서버의 rag_query.py를 구동하여 RAG 답변을 가져옵니다."""
    script_path = "/home/caiser77/dgx_workspace/002. 회사 NAS 분석/scripts/rag_query.py"
    index_dir = os.environ.get("AURUM_RAG_INDEX_DIR", "/home/caiser77/dgx_workspace/data/indexes/faiss")
    model = "Qwen/Qwen2.5-72B-Instruct-AWQ"
    endpoint = "http://localhost:8088/v1/chat/completions"
    
    cmd = [
        "/home/caiser77/dgx_workspace/venv/bin/python",
        script_path,
        "--query", query,
        "--index-dir", index_dir,
        "--model", model,
        "--llm-endpoint", endpoint
    ]
    try:
        logger.info(f"Running RAG query via subprocess: {query}")
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        if result.returncode != 0:
            logger.error(f"rag_query.py failed: {result.stderr}")
            return f"⚠️ 아톰 RAG 엔진 구동 실패 (에러 코드: {result.returncode})\n`{result.stderr.strip()}`"
        
        output_data = json.loads(result.stdout)
        answer = output_data.get("answer")
        if answer:
            # 참조 문서 목록 추가
            refs = output_data.get("references", [])
            ref_texts = []
            for r in refs[:3]:  # 상위 3개 문서만 표시
                ref_texts.append(f"- {r.get('source_name')} (유사도: {r.get('score'):.4f})")
            
            ref_section = "\n\n📚 **참조 문서:**\n" + "\n".join(ref_texts) if ref_texts else ""
            return f"🤖 **아톰 RAG 브리핑 답변**\n\n{answer}{ref_section}"
        else:
            return "⚠️ 아톰 서버 문서 검색에 실패했거나 LLM 응답이 비어 있습니다."
    except Exception as e:
        logger.error(f"RAG query execution error: {e}")
        return f"⚠️ 아톰 RAG 질문 처리 중 에러 발생: {e}"


def insert_feedback_rule(source_name: str, original_path: str, inferred_class: str, user_approved_class: str, user_instruction: str) -> bool:
    """사용자가 제공한 피드백을 SQLite DB 및 FTS5 테이블에 저장합니다."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # 1. 일반 테이블 삽입
        cursor.execute("""
            INSERT INTO aurum_nas_rules (source_name, original_path, inferred_class, user_approved_class, user_instruction)
            VALUES (?, ?, ?, ?, ?)
        """, (source_name, original_path, inferred_class, user_approved_class, user_instruction))
        rule_id = cursor.lastrowid

        # 2. FTS5 가상 테이블 연동 (FTS5 활성화되어 있을 시)
        try:
            cursor.execute("""
                INSERT INTO aurum_nas_rules_fts (rowid, user_instruction, original_path)
                VALUES (?, ?, ?)
            """, (rule_id, user_instruction, original_path))
        except sqlite3.OperationalError:
            pass # FTS5 미지원 시 패스

        conn.commit()
        conn.close()
        logger.info(f"Successfully saved feedback rule for path: {original_path}")
        return True
    except Exception as e:
        logger.error(f"Failed to insert rule to SQLite: {e}")
        return False


def parse_original_message(text: str) -> dict:
    """모호성 감지 알림 메시지 본문에서 파일명, NAS 경로, 분류군을 파싱합니다."""
    info = {"source_name": "", "original_path": "", "inferred_class": ""}

    file_name_match = re.search(r"\* 파일명:\s*(.*)", text)
    if file_name_match:
        info["source_name"] = file_name_match.group(1).strip()

    path_match = re.search(r"\* NAS 경로:\s*(.*)", text)
    if path_match:
        info["original_path"] = path_match.group(1).strip()

    class_match = re.search(r"[-*]\s*분류군:\s*(.*)", text)
    if class_match:
        info["inferred_class"] = class_match.group(1).strip()

    return info


def extract_approved_class(user_text: str) -> str:
    """사용자 텍스트에서 정정하고자 하는 생물 분류군 키워드를 추출합니다."""
    classes = ["양서파충류", "조류", "포유류", "어류", "식물상", "육상곤충", "해충", "담수조류"]
    for cls in classes:
        if cls in user_text:
            return cls
    return "기타"


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """웰컴 메시지"""
    if update.effective_user.id != ALLOWED_USER_ID:
        await update.message.reply_text("❌ 권한 오류: 허용되지 않은 사용자입니다.")
        return

    welcome = (
        "🤖 **에르메스 NAS 분류기 피드백 봇**이 실행 중입니다.\n\n"
        "이 봇은 자동 분류 도중 모호성이 감지된 파일 알림을 전달하며,\n"
        "해당 알림 메시지에 **답장(Reply)**하여 수정을 지시할 수 있습니다.\n\n"
        "💡 **예시:**\n"
        "모호성 알림 메시지에 답장으로 다음과 같이 보내주세요:\n"
        "- `조류로 분류하고, 경인 물새 모니터링 건이야`\n\n"
        "피드백은 에르메스의 SQLite 장기 기억 DB에 즉시 축적되어 학습됩니다."
    )
    await update.message.reply_text(welcome, parse_mode="Markdown")


async def handle_feedback_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """사용자가 알림 메시지에 보낸 답장을 처리하여 DB에 반영합니다."""
    user_id = update.effective_user.id
    if user_id != ALLOWED_USER_ID:
        await update.message.reply_text("❌ 권한 오류: 피드백 권한이 없습니다.")
        return

    message = update.message
    
    # 1. 답장(Reply) 대상 메시지가 존재하지 않는 경우 (일반 대화 시도)
    if not message.reply_to_message:
        user_text = message.text.strip()
        
        # 월요일 처리용 보류/대기/브리핑 요청은 RAG가 아니라 분류 대기 큐로 응답
        if is_pending_briefing_request(user_text):
            await message.reply_text(build_pending_briefing(), parse_mode="Markdown")
            return

        # 사용자가 가이드나 알려달라는 텍스트를 보낸 경우
        if any(kw in user_text for kw in ["방법", "안내", "피드백법", "help", "시작"]):
            guide_msg = (
                "🤖 **에르메스 NAS 분류기 피드백 가이드**\n\n"
                "1. 에르메스가 발송했던 ⚠️ **[분류 모호성 감지]** 알림 메시지를 찾습니다.\n"
                "2. 해당 알림 메시지를 꾹 누르거나 우클릭하여 **'답장(Reply)'**을 선택합니다.\n"
                "3. 변경하고 싶은 분류군과 지시 사항을 적어 답장 메시지를 전송합니다.\n"
                "   *(예: `조류로 분류하고, 경인 물새 건이야`)*\n\n"
                "💡 **알림**: `브리핑`, `월요일`, `대기 목록`이라고 보내시면 처리 대기 중인 분류 모호성 항목을 보여드립니다."
            )
            await message.reply_text(guide_msg, parse_mode="Markdown")
            return
            
        elif any(kw in user_text for kw in ["알려줘", "목록", "리스트"]):
            # 대기 중인 파일이 있다면 리마인더를 쏘는 로직
            pending_file = "/home/caiser77/dgx_workspace/004. 에르메스 NAS 분류기/data/last_pending.json"
            if os.path.exists(pending_file):
                try:
                    with open(pending_file, "r", encoding="utf-8") as f:
                        p_data = json.load(f)
                    
                    remind_msg = (
                        "⚠️ **[분류 모호성 감지 - 피드백 대기 알림]**\n"
                        f"* 파일명: {p_data.get('source_name')}\n"
                        f"* NAS 경로: {p_data.get('original_path')}\n"
                        f"* 분류군: {p_data.get('inferred_class', '미정')}\n\n"
                        "💡 **가이드**: 이 메시지에 바로 **'답장(Reply)'**을 하신 뒤 지시 사항을 전송해주시면 피드백이 즉시 반영됩니다!"
                    )
                    await message.reply_text(remind_msg, parse_mode="Markdown")
                    return
                except Exception as e:
                    logger.error(f"Failed to read last_pending.json: {e}")

        # 일반 질문은 RAG 조회를 수행하지 않고, 아우룸봇의 역할에 맞춰 안내를 전송합니다.
        info_msg = (
            "💰 **에르메스_인베스트먼트 (아우룸봇)**\n\n"
            "안녕하세요! 저는 사내 보고서 검수 및 최종 배포를 제어하는 아우룸봇입니다.\n"
            "이 대화방은 분류 대기 보류 건에 대한 **피드백 수집 및 알림 채널**로 사용됩니다.\n\n"
            "💡 **사용 가능 명령:**\n"
            "- ⚠️ **[분류 모호성 감지]** 알림 메시지에 **답장(Reply)**하여 수정 지시\n"
            "- `브리핑` 또는 `월요일` 또는 `대기 목록`: 현재 보류된 검수 대기 파일 목록 확인\n"
            "- `안내` 또는 `방법`: 피드백 가이드 리포트 발송\n\n"
            "📚 **RAG 지식 검색 및 일반 질문**은 **에르메스 아톰 (아톰봇)** 또는 **에르메스_리서치 (모하비봇)** 채널을 이용해 주시기 바랍니다."
        )
        await message.reply_text(info_msg, parse_mode="Markdown")
        return

    reply_text = message.reply_to_message.text
    
    # 2. 답장 대상이 봇 자신의 "피드백 대기 알림(리마인더)" 인 경우는 정상 처리로 우회
    is_reminder = "피드백 대기 알림" in reply_text
    
    # 3. 답장 대상이 봇의 일반 안내 가이드 메시지인 경우 차단
    if not is_reminder and any(kw in reply_text for kw in ["피드백을 반영하려면", "에르메스가 발송한", "피드백 가이드", "답장(Reply)"]):
        await message.reply_text(
            "⚠️ **주의**: 제가 보낸 '안내 가이드 메시지'에 답장하시면 피드백을 처리할 수 없습니다.\n\n"
            "이전에 제가 전송해 드린 ⚠️ **[분류 모호성 감지]** 알림 메시지나 **[피드백 대기 알림]** 메시지에 대고 **'답장'**을 작성해 주세요!"
        )
        return

    # 4. 올바른 모호성 감지 메시지인지 판별
    if "분류 모호성 감지" not in reply_text:
        await message.reply_text(
            "💡 **안내**: 답장하신 메시지가 올바른 모호성 알림 메시지가 아닙니다.\n"
            "반드시 ⚠️ **[분류 모호성 감지]** 제목으로 시작하는 메시지에 답장해 주셔야 합니다."
        )
        return

    # 5. 알림 메시지에서 데이터 파싱
    info = parse_original_message(reply_text)
    if not info["original_path"]:
        await message.reply_text("❌ 오류: 답장 대상 메시지에서 NAS 파일 경로를 추출하지 못했습니다.")
        return

    user_text = message.text
    user_approved = extract_approved_class(user_text)

    # DB에 저장
    success = insert_feedback_rule(
        source_name=info["source_name"],
        original_path=info["original_path"],
        inferred_class=info["inferred_class"],
        user_approved_class=user_approved,
        user_instruction=user_text
    )

    if success:
        mark_pending_resolved(info["original_path"])
        reply_back = (
            "✅ **사용자 피드백이 자가 학습 DB에 저장되었습니다!**\n"
            f"• 원본 파일: `{info['source_name']}`\n"
            f"• 정정된 분류군: `{user_approved}`\n"
            f"• 지시 내용: `{user_text}`\n\n"
            "에르메스가 해당 경로 계층에 맞춰 이 지침을 장기 기억으로 학습하여 다음 처리 시 자동으로 반영합니다."
        )
        await message.reply_text(reply_back, parse_mode="Markdown")
    else:
        await message.reply_text("❌ 오류: 피드백 반영 도중 데이터베이스 쓰기 오류가 발생했습니다.")


if __name__ == "__main__":
    if not TOKEN or not ALLOWED_USER_ID:
        logger.error("TELEGRAM_BOT_TOKEN and ALLOWED_USER_ID must be set.")
        sys.exit(1)

    if not os.path.exists(os.path.dirname(DB_PATH)):
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

    logger.info("Starting Telegram Feedback Bot...")
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", start_command))
    # 답장 또는 일반 메시지를 처리하는 핸들러
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_feedback_reply))

    logger.info("Bot is polling for messages...")
    app.run_polling()
