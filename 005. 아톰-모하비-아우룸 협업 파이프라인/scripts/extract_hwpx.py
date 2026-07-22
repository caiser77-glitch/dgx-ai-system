#!/usr/bin/env python3
# 007 — HWPX(OWPML zip) 본문 추출. hwp5txt가 못 여는 PK 포맷(HWPX) 회복.
# Created: 2026-07-23 by Antigravity(Claude Opus 4.8)
# 용법: extract_hwpx.py <file.hwpx>  → stdout에 본문. 라이브러리로도 import 가능.
import sys, zipfile, re
from xml.etree import ElementTree as ET

def extract_hwpx(path):
    out = []
    with zipfile.ZipFile(path) as z:
        secs = sorted(n for n in z.namelist() if re.match(r"Contents/section\d+\.xml$", n))
        if not secs:
            secs = sorted(n for n in z.namelist() if n.startswith("Contents/") and n.endswith(".xml"))
        for n in secs:
            try:
                root = ET.fromstring(z.read(n))
            except ET.ParseError:
                continue
            for p in root.iter():
                if p.tag.split("}")[-1] != "p":   # 문단(hp:p) 단위
                    continue
                runs = [t.text for t in p.iter()
                        if t.tag.split("}")[-1] == "t" and t.text]
                if runs:
                    out.append("".join(runs))
    return "\n".join(out)

if __name__ == "__main__":
    txt = extract_hwpx(sys.argv[1])
    sys.stdout.write(txt + "\n")
