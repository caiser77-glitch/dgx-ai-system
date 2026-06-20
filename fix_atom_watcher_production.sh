#!/usr/bin/env bash
set -euo pipefail

if [[ "${EUID}" -ne 0 ]]; then
  echo "ERROR: run as root: sudo bash $0" >&2
  exit 1
fi

APP_DIR="/opt/atom-watcher"
WATCHER="${APP_DIR}/watcher.py"
SERVICE="/etc/systemd/system/atom-watcher.service"
CONFIG="/etc/atom-watcher/config.yaml"
STAMP="$(date +%Y%m%d-%H%M%S)"

for path in "$WATCHER" "$SERVICE" "$CONFIG"; do
  if [[ ! -e "$path" ]]; then
    echo "ERROR: missing required file: $path" >&2
    exit 1
  fi
done

echo "== backup =="
cp -a "$WATCHER" "${WATCHER}.bak.${STAMP}"
cp -a "$SERVICE" "${SERVICE}.bak.${STAMP}"
cp -a "$CONFIG" "${CONFIG}.bak.${STAMP}"

echo "== patch watcher: use PollingObserver for SMB/CIFS mounts =="
python3 - "$WATCHER" <<'PY'
from pathlib import Path
import sys

path = Path(sys.argv[1])
text = path.read_text(encoding="utf-8")

replacements = {
    "from watchdog.observers import Observer": (
        "from watchdog.observers.polling import PollingObserver as Observer"
    ),
    "from watchdog.observers.inotify import InotifyObserver as Observer": (
        "from watchdog.observers.polling import PollingObserver as Observer"
    ),
}

changed = False
for old, new in replacements.items():
    if old in text:
        text = text.replace(old, new, 1)
        changed = True

if "PollingObserver as Observer" not in text:
    raise SystemExit("ERROR: could not patch watcher observer import safely")

if "polling observer enabled for SMB/CIFS reliability" not in text:
    marker = "observer = Observer()"
    if marker in text:
        text = text.replace(
            marker,
            'log.info("polling observer enabled for SMB/CIFS reliability")\n        observer = Observer()',
            1,
        )
        changed = True

if changed:
    path.write_text(text, encoding="utf-8")
PY

echo "== patch systemd ReadOnlyPaths =="
python3 - "$SERVICE" <<'PY'
from pathlib import Path
import sys

path = Path(sys.argv[1])
text = path.read_text(encoding="utf-8")
old = "ReadOnlyPaths=/mnt/nas /etc/atom-watcher"
new = "ReadOnlyPaths=/mnt /etc/atom-watcher"
if old in text:
    text = text.replace(old, new, 1)
elif "ReadOnlyPaths=/mnt /etc/atom-watcher" not in text:
    lines = text.splitlines()
    for idx, line in enumerate(lines):
        if line.startswith("ReadOnlyPaths="):
            lines[idx] = new
            break
    else:
        lines.append(new)
    text = "\n".join(lines) + "\n"
path.write_text(text, encoding="utf-8")
PY

echo "== permissions =="
chown atom:atom "$WATCHER"
chmod 0700 "$WATCHER"
chgrp atom /etc/atom-watcher "$CONFIG"
chmod 0750 /etc/atom-watcher
chmod 0640 "$CONFIG"

echo "== syntax check =="
/opt/atom-watcher/.venv/bin/python -m py_compile "$WATCHER"

echo "== restart service =="
systemctl daemon-reload
systemctl reset-failed atom-watcher || true
systemctl restart atom-watcher
sleep 3
systemctl --no-pager --full status atom-watcher

echo "== probe =="
PROBE_DIR="/mnt/nas2026/_AURUM_AI_INBOX"
if [[ ! -d "$PROBE_DIR" ]]; then
  echo "ERROR: probe dir missing: $PROBE_DIR" >&2
  exit 2
fi

PROBE="${PROBE_DIR}/atom_watcher_production_probe_${STAMP}.txt"
touch "$PROBE"
echo "created probe: $PROBE"
sleep 20

echo "== recent logs =="
journalctl -u atom-watcher --since "2 minutes ago" --no-pager

rm -f "$PROBE"
echo "removed probe: $PROBE"
echo "DONE: atom-watcher production patch attempted. Check the recent logs above for event/notify output."
