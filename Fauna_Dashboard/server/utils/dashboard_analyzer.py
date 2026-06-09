# Fauna_Dashboard 데이터베이스 분석 및 보고서 주입 엔진
# database.json의 속성(protected, traces, class 등)을 분석하여
# PDF 보고서 섹션별(법정보호종, 종 다양성, 조사 흔적)로 데이터를 정밀하게 분류하고 주입합니다.

import json
import sys
import os
from collections import defaultdict


# ─── 흔적 코드 한국어 매핑 ────────────────────────────────────────────────────
TRACE_LABELS = {
    "V": "직접 목격 (Visual)",
    "D": "배설물 (Dropping)",
    "F": "발자국 (Footprint)",
    "S": "털·비늘·뼈 (Sign)",
    "T": "포획틀·족적 (Trap/Track)",
}


class FaunaReportEngine:
    """
    database.json을 읽어 PDF 보고서의 3대 섹션에
    정밀하게 데이터를 분류·주입하는 엔진입니다.

    섹션 1: 법정보호종 목록 (protected == True인 종)
    섹션 2: 종 다양성 분석 (class별 개체 수 집계)
    섹션 3: 조사 흔적 분류 (traces 유형별 종 목록)
    """

    def __init__(self):
        self.records: list = []

    # ── 데이터 로드 ─────────────────────────────────────────────────────────
    def load(self, db_path: str) -> "FaunaReportEngine":
        if not os.path.exists(db_path):
            raise FileNotFoundError(f"database.json을 찾을 수 없습니다: {db_path}")
        with open(db_path, "r", encoding="utf-8") as f:
            self.records = json.load(f)
        print(f"  ✅ {len(self.records)}개 레코드 로드 완료: {db_path}")
        return self

    # ── 섹션 1: 법정보호종 ───────────────────────────────────────────────────
    def protected_species_section(self) -> dict:
        """protected == True인 레코드를 수집하고 분류군별로 정리합니다."""
        by_class: dict[str, list[str]] = defaultdict(list)
        seen: set[str] = set()

        for r in self.records:
            protected_val = r.get("protected")
            if not protected_val:
                continue
            species = r.get("species", "미확인종")
            cls = r.get("class", "미분류")
            
            # category (멸종위기 I급/II급 등) 추가 정보는 protected 필드 자체가 문자열일 경우 그 값을 사용
            category = protected_val if isinstance(protected_val, str) else r.get("category", "")
            label = f"{species} ({category})" if category else species

            key = f"{species}|{cls}"
            if key not in seen:
                seen.add(key)
                by_class[cls].append(label)

        total = sum(len(v) for v in by_class.values())
        return {"total": total, "by_class": dict(by_class)}

    # ── 섹션 2: 종 다양성 ───────────────────────────────────────────────────
    def diversity_section(self) -> dict:
        """분류군(class)별 총 개체 수와 종 수를 집계합니다."""
        count_sum: dict[str, int] = defaultdict(int)
        species_set: dict[str, set] = defaultdict(set)

        for r in self.records:
            cls = r.get("class", "미분류")
            count_sum[cls] += int(r.get("count", 0) or 0)
            species_set[cls].add(r.get("species", "미확인종"))

        result = {}
        for cls in sorted(count_sum.keys()):
            result[cls] = {
                "total_count": count_sum[cls],
                "species_count": len(species_set[cls]),
                "species_list": sorted(species_set[cls]),
            }
        return result

    # ── 섹션 3: 조사 흔적 ───────────────────────────────────────────────────
    def traces_section(self) -> dict:
        """흔적 유형(V/D/F/S/T)별로 탐지된 종 목록을 분류합니다."""
        trace_map: dict[str, set] = defaultdict(set)

        for r in self.records:
            species = r.get("species", "미확인종")
            raw = r.get("traces", "")
            if isinstance(raw, list):
                codes = raw
            elif isinstance(raw, str) and raw:
                codes = [x.strip() for x in raw.split(",") if x.strip()]
            else:
                codes = []

            for code in codes:
                trace_map[code].add(species)

        result = {}
        for code in sorted(trace_map.keys()):
            result[code] = {
                "label": TRACE_LABELS.get(code, code),
                "species_count": len(trace_map[code]),
                "species_list": sorted(trace_map[code]),
            }
        return result

    # ── 데이터 주입용 페이로드 생성 ──────────────────────────────────────────
    def get_injection_payload(self) -> dict:
        """
        PDF 등 외부 생성 모듈에 즉시 주입할 수 있는 형태의 정제된 JSON 페이로드를 반환합니다.
        """
        return {
            "metadata": {
                "total_records": len(self.records),
                "title": "생태 조사 통합 분석 보고서 데이터"
            },
            "protected_species": self.protected_species_section(),
            "diversity": self.diversity_section(),
            "traces": self.traces_section()
        }

    # ── 보고서 렌더링 ────────────────────────────────────────────────────────
    def render_report(self) -> str:
        lines = [
            "# 📑 생태 조사 통합 분석 보고서",
            f"\n> 총 조사 레코드: **{len(self.records)}건**\n",
        ]

        # ── 섹션 1 ──
        lines.append("---\n## 🛡️ 섹션 1: 법정보호종 현황\n")
        ps = self.protected_species_section()
        lines.append(f"**법정보호종 합계: {ps['total']}종**\n")
        if ps["by_class"]:
            lines.append("| 분류군 | 법정보호종 |")
            lines.append("| :--- | :--- |")
            for cls, species_list in ps["by_class"].items():
                lines.append(f"| {cls} | {', '.join(species_list)} |")
        else:
            lines.append("_법정보호종 없음_")

        # ── 섹션 2 ──
        lines.append("\n---\n## 🌳 섹션 2: 종 다양성 분석\n")
        div = self.diversity_section()
        lines.append("| 분류군 | 종 수 | 총 개체 수 |")
        lines.append("| :--- | :---: | :---: |")
        for cls, info in div.items():
            lines.append(f"| {cls} | {info['species_count']} | {info['total_count']:,} |")

        # ── 섹션 3 ──
        lines.append("\n---\n## 🔍 섹션 3: 조사 흔적 유형별 탐지 현황\n")
        tr = self.traces_section()
        if tr:
            for code, info in tr.items():
                lines.append(f"### [{code}] {info['label']} — {info['species_count']}종 탐지")
                lines.append(f"- 탐지 종: {', '.join(info['species_list'])}\n")
        else:
            lines.append("_흔적 데이터 없음_")

        return "\n".join(lines)


# ─── 기존 호환성 함수 (main.py 등에서 import하여 사용) ─────────────────────
def analyze_fauna_data(db_path: str) -> dict:
    """분류군별 총 개체 수를 반환합니다 (기존 API 호환)."""
    engine = FaunaReportEngine()
    try:
        engine.load(db_path)
    except FileNotFoundError as e:
        print(f"[오류] {e}")
        return {}
    return {
        cls: info["total_count"]
        for cls, info in engine.diversity_section().items()
    }


def generate_markdown_report(counts: dict) -> str:
    """분류군 집계 딕셔너리를 마크다운 표로 변환합니다 (기존 API 호환)."""
    lines = ["## 🌳 단순 집계 보고서", "", "| 분류군 | 총 개체 수 |", "| :--- | :---: |"]
    for cls, total in sorted(counts.items()):
        lines.append(f"| {cls} | {total:,} |")
    return "\n".join(lines)


# ─── 단독 실행 ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # 사용법: python3 dashboard_analyzer.py [database.json 경로]
    # 인자가 없으면 스크립트 위치를 기준으로 server 폴더의 database.json을 자동 탐색합니다.
    if len(sys.argv) > 1:
        db_file_path = sys.argv[1]
    else:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        db_file_path = os.path.join(base_dir, "database.json")

    print("=" * 60)
    print("🔬 Fauna Dashboard 데이터 주입 엔진 시작")
    print("=" * 60)

    engine = FaunaReportEngine()
    try:
        engine.load(db_file_path)
    except FileNotFoundError:
        print(f"❌ 데이터베이스 파일을 찾을 수 없습니다: {db_file_path}")
        sys.exit(1)

    report = engine.render_report()
    payload = engine.get_injection_payload()

    # 결과 보고서를 실제 파일로 주입(저장)
    output_dir = os.path.dirname(db_file_path)
    if not output_dir:
        output_dir = "."
        
    output_path = os.path.join(output_dir, "dashboard_report.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report)

    # 주입용 JSON 페이로드 저장
    payload_path = os.path.join(output_dir, "injection_payload.json")
    with open(payload_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 60)
    print(f"✅ 분석 완료 — 보고서가 실제 파일로 성공적으로 주입(저장)되었습니다: {output_path}")
    print(f"✅ 데이터 주입 준비 완료 — 페이로드 JSON 저장 완료: {payload_path}")
    print("=" * 60 + "\n")
    print(report)
    print("\n" + "=" * 60 + "\n")
