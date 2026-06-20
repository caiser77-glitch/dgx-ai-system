#!/usr/bin/env bash
set -euo pipefail

if [[ "${EUID}" -ne 0 ]]; then
  echo "ERROR: run as root: sudo bash $0" >&2
  exit 1
fi

WATCHER="/opt/atom-watcher/watcher.py"
STAMP="$(date +%Y%m%d-%H%M%S)"

if [[ ! -f "$WATCHER" ]]; then
  echo "ERROR: missing watcher: $WATCHER" >&2
  exit 1
fi

cp -a "$WATCHER" "${WATCHER}.bak.observability.${STAMP}"

python3 - "$WATCHER" <<'PY'
from pathlib import Path
import sys

path = Path(sys.argv[1])
text = path.read_text(encoding="utf-8")

if "raw_event=%s path=%s" not in text:
    marker = "    def _emit(self, abspath: str, event_type: str) -> None:\n"
    replacement = marker + '        log.info("raw_event=%s path=%s", event_type, abspath)\n'
    if marker not in text:
        raise SystemExit("ERROR: _emit marker not found")
    text = text.replace(marker, replacement, 1)

if "skip non-matching path: %s" in text and 'log.info("skip non-matching path: %s", rel)' not in text:
    text = text.replace(
        'log.debug("skip non-matching path: %s", rel)',
        'log.info("skip non-matching path: %s", rel)',
    )

path.write_text(text, encoding="utf-8")
PY

chown atom:atom "$WATCHER"
chmod 0700 "$WATCHER"
/opt/atom-watcher/.venv/bin/python -m py_compile "$WATCHER"

systemctl restart atom-watcher
sleep 3
systemctl --no-pager --full status atom-watcher

PROBE_DIR="/mnt/nas2026/_AURUM_AI_INBOX"
PROBE="${PROBE_DIR}/atom_watcher_raw_event_probe_${STAMP}.txt"
touch "$PROBE"
echo "created probe: $PROBE"
sleep 90

echo "== recent logs =="
journalctl -u atom-watcher --since "2 minutes ago" --no-pager

rm -f "$PROBE"
echo "removed probe: $PROBE"
