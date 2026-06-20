#!/usr/bin/env bash
set -euo pipefail

if [[ "${EUID}" -ne 0 ]]; then
  echo "Run as root: sudo bash $0" >&2
  exit 1
fi

APP_DIR="/opt/atom-watcher"
WATCHER="${APP_DIR}/watcher.py"
SERVICE="/etc/systemd/system/atom-watcher.service"
CONFIG_DIR="/etc/atom-watcher"
CONFIG="${CONFIG_DIR}/config.yaml"
ENV_FILE="${CONFIG_DIR}/atom-watcher.env"
STAMP="$(date +%Y%m%d-%H%M%S)"

for path in "$WATCHER" "$SERVICE" "$CONFIG"; do
  if [[ ! -e "$path" ]]; then
    echo "Missing required file: $path" >&2
    exit 1
  fi
done

cp -a "$WATCHER" "${WATCHER}.bak.${STAMP}"
cp -a "$SERVICE" "${SERVICE}.bak.${STAMP}"
cp -a "$CONFIG" "${CONFIG}.bak.${STAMP}"

python3 - "$CONFIG" "$ENV_FILE" <<'PY'
import os
import shlex
import stat
import sys
from getpass import getpass
from pathlib import Path

import yaml

config_path = Path(sys.argv[1])
env_path = Path(sys.argv[2])

cfg = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
notifier = cfg.setdefault("notifier", {})

token = os.environ.get("ATOM_WATCHER_BOT_TOKEN") or notifier.get("bot_token")
chat_id = os.environ.get("ATOM_WATCHER_CHAT_ID") or notifier.get("chat_id")

if not token or str(token).startswith("REPLACE_WITH"):
    token = getpass("Telegram bot token: ").strip()
if not chat_id or str(chat_id).startswith("REPLACE_WITH"):
    chat_id = input("Telegram chat id: ").strip()

if not token or not chat_id:
    raise SystemExit("Missing Telegram bot token or chat id")

env_path.write_text(
    "ATOM_WATCHER_BOT_TOKEN=" + shlex.quote(str(token)) + "\n"
    "ATOM_WATCHER_CHAT_ID=" + shlex.quote(str(chat_id)) + "\n",
    encoding="utf-8",
)
os.chmod(env_path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP)

notifier["bot_token"] = "${ATOM_WATCHER_BOT_TOKEN}"
notifier["chat_id"] = "${ATOM_WATCHER_CHAT_ID}"
config_path.write_text(
    yaml.safe_dump(cfg, allow_unicode=True, sort_keys=False),
    encoding="utf-8",
)
PY

chown root:atom "$ENV_FILE" "$CONFIG"
chmod 0640 "$ENV_FILE" "$CONFIG"

python3 - "$WATCHER" <<'PY'
import sys
from pathlib import Path

path = Path(sys.argv[1])
text = path.read_text(encoding="utf-8")

if "def expand_env_values(" not in text:
    marker = "\n\n# ─────────────────────────────────────────────────────────────\n# 디바운서"
    helper = r'''

def expand_env_values(value):
    """Recursively expand ${VAR} placeholders from the process environment."""
    if isinstance(value, str):
        return os.path.expandvars(value)
    if isinstance(value, list):
        return [expand_env_values(item) for item in value]
    if isinstance(value, dict):
        return {key: expand_env_values(item) for key, item in value.items()}
    return value
'''
    text = text.replace(marker, helper + marker, 1)

old = '''    with open(args.config, encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
'''
new = '''    with open(args.config, encoding="utf-8") as f:
        cfg = expand_env_values(yaml.safe_load(f))
'''
if old in text and new not in text:
    text = text.replace(old, new, 1)

path.write_text(text, encoding="utf-8")
PY

chown atom:atom "$WATCHER"
chmod 0700 "$WATCHER"

if ! grep -q '^EnvironmentFile=-/etc/atom-watcher/atom-watcher.env$' "$SERVICE"; then
  python3 - "$SERVICE" <<'PY'
import sys
from pathlib import Path

path = Path(sys.argv[1])
text = path.read_text(encoding="utf-8")
needle = "Group=atom\n"
insert = "Group=atom\nEnvironmentFile=-/etc/atom-watcher/atom-watcher.env\n"
text = text.replace(needle, insert, 1)
path.write_text(text, encoding="utf-8")
PY
fi

systemctl daemon-reload
systemctl restart atom-watcher
systemctl --no-pager --full status atom-watcher

echo
echo "Done. Token is now stored in ${ENV_FILE}, and config.yaml uses environment placeholders."
echo "Backups have suffix: .bak.${STAMP}"
