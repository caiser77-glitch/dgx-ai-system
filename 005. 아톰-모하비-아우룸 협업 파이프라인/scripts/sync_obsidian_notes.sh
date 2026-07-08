#!/usr/bin/env bash
set -euo pipefail

# 아톰-모하비-아우룸 협업 파이프라인 동기화 유틸리티.
# 환경변수로 경로를 주입한다.
#   ATOM_PIPELINE_ROOT      기본: $HOME/AI_BASE
#   MOHAVE_PIPELINE_ROOT    예: user@mac:/Users/user/Obsidian/AurumPipeline
#   AURUM_PIPELINE_ROOT     예: user@aurum:/srv/aurum-pipeline
#   AURUM_RULES_DB          기본: /home/caiser77/dgx_workspace/004. 에르메스 NAS 분류기/data/aurum_nas_rules.db
#   DRY_RUN=1               rsync --dry-run

ATOM_PIPELINE_ROOT="${ATOM_PIPELINE_ROOT:-$HOME/AI_BASE}"
MOHAVE_PIPELINE_ROOT="${MOHAVE_PIPELINE_ROOT:-}"
AURUM_PIPELINE_ROOT="${AURUM_PIPELINE_ROOT:-}"
AURUM_RULES_DB="${AURUM_RULES_DB:-/home/caiser77/dgx_workspace/004. 에르메스 NAS 분류기/data/aurum_nas_rules.db}"
DRY_RUN="${DRY_RUN:-0}"
RSYNC_BIN="${RSYNC_BIN:-rsync}"

rsync_flags=(-az --update --partial --protect-args)
if [[ "$DRY_RUN" == "1" ]]; then
  rsync_flags+=(--dry-run)
fi

# Linux -> macOS 경로 전송 시 사용자가 필요하면 RSYNC_ICONV=utf-8,utf-8-mac 처럼 지정한다.
if [[ -n "${RSYNC_ICONV:-}" ]]; then
  rsync_flags+=("--iconv=${RSYNC_ICONV}")
fi

usage() {
  cat <<'EOF'
Usage: sync_obsidian_notes.sh <command>

Commands:
  atom-to-mohave     01_raw_analyzed, 02_drafting, feedback DB를 모하비로 전송
  mohave-to-atom     모하비의 02_drafting, 03_review_pending을 아톰으로 회수
  atom-to-aurum      03_review_pending을 아우룸으로 전송
  aurum-to-atom      04_published, 00_error_failed를 아톰으로 회수
  all                위 순서를 모두 실행 가능한 대상에 대해 수행

Required env for remote sync:
  MOHAVE_PIPELINE_ROOT, AURUM_PIPELINE_ROOT
EOF
}

require_target() {
  local name="$1"
  local value="$2"
  if [[ -z "$value" ]]; then
    echo "ERROR: $name is not set" >&2
    exit 2
  fi
}

ensure_local_dirs() {
  mkdir -p \
    "$ATOM_PIPELINE_ROOT/00_error_failed" \
    "$ATOM_PIPELINE_ROOT/01_raw_analyzed" \
    "$ATOM_PIPELINE_ROOT/02_drafting" \
    "$ATOM_PIPELINE_ROOT/03_review_pending" \
    "$ATOM_PIPELINE_ROOT/04_published" \
    "$ATOM_PIPELINE_ROOT/feedback"
}

sync_dir() {
  local src="$1"
  local dst="$2"
  echo "SYNC $src -> $dst"
  "$RSYNC_BIN" "${rsync_flags[@]}" "$src" "$dst"
}

sync_file_if_exists() {
  local src="$1"
  local dst="$2"
  if [[ -f "$src" ]]; then
    echo "SYNC $src -> $dst"
    "$RSYNC_BIN" "${rsync_flags[@]}" "$src" "$dst"
  else
    echo "SKIP missing file: $src"
  fi
}

atom_to_mohave() {
  require_target MOHAVE_PIPELINE_ROOT "$MOHAVE_PIPELINE_ROOT"
  ensure_local_dirs
  sync_dir "$ATOM_PIPELINE_ROOT/01_raw_analyzed/" "$MOHAVE_PIPELINE_ROOT/01_raw_analyzed/"
  sync_dir "$ATOM_PIPELINE_ROOT/02_drafting/" "$MOHAVE_PIPELINE_ROOT/02_drafting/"
  sync_file_if_exists "$AURUM_RULES_DB" "$MOHAVE_PIPELINE_ROOT/feedback/aurum_nas_rules.db"
}

mohave_to_atom() {
  require_target MOHAVE_PIPELINE_ROOT "$MOHAVE_PIPELINE_ROOT"
  ensure_local_dirs
  sync_dir "$MOHAVE_PIPELINE_ROOT/02_drafting/" "$ATOM_PIPELINE_ROOT/02_drafting/"
  sync_dir "$MOHAVE_PIPELINE_ROOT/03_review_pending/" "$ATOM_PIPELINE_ROOT/03_review_pending/"
}

atom_to_aurum() {
  require_target AURUM_PIPELINE_ROOT "$AURUM_PIPELINE_ROOT"
  ensure_local_dirs
  sync_dir "$ATOM_PIPELINE_ROOT/03_review_pending/" "$AURUM_PIPELINE_ROOT/03_review_pending/"
  sync_file_if_exists "$AURUM_RULES_DB" "$AURUM_PIPELINE_ROOT/feedback/aurum_nas_rules.db"
}

aurum_to_atom() {
  require_target AURUM_PIPELINE_ROOT "$AURUM_PIPELINE_ROOT"
  ensure_local_dirs
  sync_dir "$AURUM_PIPELINE_ROOT/04_published/" "$ATOM_PIPELINE_ROOT/04_published/"
  sync_dir "$AURUM_PIPELINE_ROOT/00_error_failed/" "$ATOM_PIPELINE_ROOT/00_error_failed/"
}

cmd="${1:-}"
case "$cmd" in
  atom-to-mohave) atom_to_mohave ;;
  mohave-to-atom) mohave_to_atom ;;
  atom-to-aurum) atom_to_aurum ;;
  aurum-to-atom) aurum_to_atom ;;
  all)
    [[ -n "$MOHAVE_PIPELINE_ROOT" ]] && atom_to_mohave && mohave_to_atom || true
    [[ -n "$AURUM_PIPELINE_ROOT" ]] && atom_to_aurum && aurum_to_atom || true
    ;;
  -h|--help|help|"") usage ;;
  *) echo "ERROR: unknown command: $cmd" >&2; usage; exit 2 ;;
esac
