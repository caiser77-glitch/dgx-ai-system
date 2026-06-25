#!/usr/bin/env python3
"""Shared ignore rules for Atom NAS baseline and event classification."""

from __future__ import annotations

from pathlib import Path

IGNORED_DIR_NAMES = {
    "#recycle",
    "@eadir",
    "@eaDir",
    "_AURUM_AI_PROCESSED",
    ".@__thumb",
    ".snapshot",
    "@recycle",
}

IGNORED_FILE_NAMES = {
    ".DS_Store",
    "Thumbs.db",
    "thumbs.db",
    "desktop.ini",
    "Desktop.ini",
}

IGNORED_FILE_PREFIXES = (
    "._",
    "~$",
)

IGNORED_SUFFIXES = (
    ".tmp",
    ".part",
    ".crdownload",
)


def path_parts(path: Path | str) -> tuple[str, ...]:
    return tuple(Path(path).parts)


def should_exclude_name(name: str, *, is_dir: bool = False) -> bool:
    if is_dir and name in IGNORED_DIR_NAMES:
        return True
    if name in IGNORED_FILE_NAMES:
        return True
    if any(name.startswith(prefix) for prefix in IGNORED_FILE_PREFIXES):
        return True
    lower_name = name.lower()
    if any(lower_name.endswith(suffix) for suffix in IGNORED_SUFFIXES):
        return True
    return False


def should_exclude_path(path: Path | str, *, is_dir: bool = False) -> bool:
    p = Path(path)
    parts = p.parts
    for part in parts:
        if part in IGNORED_DIR_NAMES:
            return True
    return should_exclude_name(p.name, is_dir=is_dir)
