#!/usr/bin/env python3
"""Slack notification helper for the local AI server project."""
import json
import os
from pathlib import Path
import urllib.error
import urllib.request

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATHS = [BASE_DIR / ".env", Path(__file__).resolve().parent / ".env"]
for env_path in ENV_PATHS:
    if env_path.exists():
        load_dotenv(env_path)

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")
SLACK_CHANNEL = os.getenv("SLACK_CHANNEL")


def slack_enabled() -> bool:
    return bool(SLACK_WEBHOOK_URL)


def send_slack_message(text: str) -> bool:
    if not slack_enabled():
        return False

    payload = {"text": text}
    if SLACK_CHANNEL:
        payload["channel"] = SLACK_CHANNEL

    request = urllib.request.Request(
        SLACK_WEBHOOK_URL,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            return 200 <= response.status < 300
    except (urllib.error.URLError, TimeoutError):
        return False
