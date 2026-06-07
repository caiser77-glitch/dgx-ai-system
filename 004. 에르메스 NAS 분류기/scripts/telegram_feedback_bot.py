# -*- coding: utf-8 -*-
"""
아우룸생태연구소 에르메스 NAS 분류기 사용자 피드백 수집 및 자가학습 텔레그램 봇
"""

import os
import sys
import re
import sqlite3
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, CommandHandler, filters

# 로깅 설정
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger("TelegramFeedbackBot")

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
ALLOWED_USER_ID = int(os.environ.get("ALLOWED_USER_ID", "0"))
DB_PATH = "/home/caiser77/dgx_workspace/004. 에르메스 NAS 분류기/data/aurum_nas_rules.db"


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

    class_match = re.search(r"-\s*분류군:\s*(.*)", text)
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
    # 답장(Reply) 대상 메시지가 존재하는지 확인
    if not message.reply_to_message:
        await message.reply_text(
            "💡 **안내**: 피드백을 반영하려면 에르메스가 발송한 **[분류 모호성 감지]** 알림 메시지에 **답장(Reply)**으로 의견을 작성해 주세요."
        )
        return

    reply_text = message.reply_to_message.text
    # 올바른 모호성 감지 메시지인지 판별
    if "분류 모호성 감지" not in reply_text:
        await message.reply_text("💡 **안내**: 답장하신 메시지가 올바른 모호성 알림 메시지가 아닙니다.")
        return

    # 알림 메시지에서 데이터 파싱
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
