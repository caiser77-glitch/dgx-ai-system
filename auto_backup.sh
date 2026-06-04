#!/bin/bash

set -e

DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_ROOT="/home/caiser77/backup"
BACKUP_DIR="$BACKUP_ROOT/aurum_$DATE"
ARCHIVE_FILE="$BACKUP_ROOT/aurum_backup_$DATE.tar.gz"

mkdir -p "$BACKUP_DIR"

echo "백업 시작: $DATE"

if [ -f "/home/caiser77/dgx_workspace/data/taxa.db" ]; then
  mkdir -p "$BACKUP_DIR/data"
  cp "/home/caiser77/dgx_workspace/data/taxa.db" "$BACKUP_DIR/data/"
  echo "taxa.db 백업 완료"
else
  echo "경고: taxa.db 없음"
fi

if [ -d "/home/caiser77/aurum/rag/api" ]; then
  mkdir -p "$BACKUP_DIR/rag"
  cp -r "/home/caiser77/aurum/rag/api" "$BACKUP_DIR/rag/"
  echo "RAG API 백업 완료"
else
  echo "경고: RAG API 폴더 없음"
fi

if [ -d "/home/caiser77/aurum/rag/db" ]; then
  mkdir -p "$BACKUP_DIR/rag"
  cp -r "/home/caiser77/aurum/rag/db" "$BACKUP_DIR/rag/"
  echo "ChromaDB 백업 완료"
else
  echo "경고: ChromaDB 폴더 없음"
fi

if [ -d "/home/caiser77/aurum_v2/frontend/src" ]; then
  mkdir -p "$BACKUP_DIR/frontend"
  cp -r "/home/caiser77/aurum_v2/frontend/src" "$BACKUP_DIR/frontend/"
  echo "Frontend src 백업 완료"
else
  echo "경고: frontend/src 폴더 없음"
fi

if [ -f "/home/caiser77/aurum_v2/frontend/package.json" ]; then
  mkdir -p "$BACKUP_DIR/frontend"
  cp "/home/caiser77/aurum_v2/frontend/package.json" "$BACKUP_DIR/frontend/"
  echo "package.json 백업 완료"
fi

cd "$BACKUP_ROOT"
tar -czf "$ARCHIVE_FILE" "aurum_$DATE"

rm -rf "$BACKUP_DIR"

echo "백업 압축 완료:"
echo "$ARCHIVE_FILE"

echo "최근 백업 목록:"
ls -lh "$BACKUP_ROOT"/aurum_backup_*.tar.gz | tail -5
