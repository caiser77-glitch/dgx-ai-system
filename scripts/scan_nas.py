#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
NAS(또는 공유 디렉토리) 스캔 스크립트
지정된 경로의 파일 목록을 스캔하여 파싱 대상 문서 리포트를 생성합니다.
"""

import os
import json
import argparse
from datetime import datetime

SUPPORTED_EXTENSIONS = {
    'documents': ['.pdf', '.docx', '.txt', '.pptx', '.xlsx', '.csv'],
    'images': ['.png', '.jpg', '.jpeg', '.tif', '.tiff', '.gif'],
}

def scan_directory(target_path):
    """
    지정된 디렉토리를 순회하며 파일 목록 및 메타데이터를 수집합니다.
    """
    report = {
        'scan_time': datetime.now().isoformat(),
        'target_path': target_path,
        'summary': {
            'total_files': 0,
            'total_size_bytes': 0,
            'supported_docs_count': 0,
            'supported_images_count': 0,
            'unsupported_count': 0,
            'extension_stats': {}
        },
        'files': []
    }
    
    if not os.path.exists(target_path):
        print(f"오류: 경로가 존재하지 않습니다: {target_path}")
        return report

    for root, dirs, files in os.walk(target_path):
        # 숨김 디렉토리 제외 (.git, .obsidian 등)
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            if file.startswith('.'):
                continue
                
            file_path = os.path.join(root, file)
            try:
                stat = os.stat(file_path)
                size = stat.st_size
                mtime = datetime.fromtimestamp(stat.st_mtime).isoformat()
                ext = os.path.splitext(file)[1].lower()
                
                # 상대 경로 계산
                rel_path = os.path.relpath(file_path, target_path)
                
                # 지원 여부 체크
                is_doc = ext in SUPPORTED_EXTENSIONS['documents']
                is_img = ext in SUPPORTED_EXTENSIONS['images']
                supported = is_doc or is_img
                
                file_info = {
                    'name': file,
                    'relative_path': rel_path,
                    'absolute_path': os.path.abspath(file_path),
                    'size_bytes': size,
                    'modified_time': mtime,
                    'extension': ext,
                    'category': 'document' if is_doc else ('image' if is_img else 'unknown'),
                    'supported': supported
                }
                
                report['files'].append(file_info)
                
                # 통계 업데이트
                report['summary']['total_files'] += 1
                report['summary']['total_size_bytes'] += size
                if is_doc:
                    report['summary']['supported_docs_count'] += 1
                elif is_img:
                    report['summary']['supported_images_count'] += 1
                else:
                    report['summary']['unsupported_count'] += 1
                    
                report['summary']['extension_stats'][ext] = report['summary']['extension_stats'].get(ext, 0) + 1
                
            except Exception as e:
                print(f"파일 스캔 중 오류 발생 ({file_path}): {e}")
                
    return report

def write_markdown_report(report, out_path):
    """
    스캔 결과를 사람이 읽기 쉬운 Markdown 형식으로 저장합니다.
    """
    lines = []
    lines.append(f"# NAS 파일 스캔 리포트")
    lines.append(f"- **스캔 시간**: {report['scan_time']}")
    lines.append(f"- **대상 경로**: `{report['target_path']}`")
    lines.append("")
    lines.append("## 📊 요약 통계")
    lines.append(f"- **전체 파일 수**: {report['summary']['total_files']} 개")
    lines.append(f"- **전체 크기**: {report['summary']['total_size_bytes'] / (1024*1024):.2f} MB ({report['summary']['total_size_bytes']} bytes)")
    lines.append(f"- **지원 문서 수 (.pdf, .docx 등)**: {report['summary']['supported_docs_count']} 개")
    lines.append(f"- **지원 이미지 수 (.png, .jpg 등)**: {report['summary']['supported_images_count']} 개")
    lines.append(f"- **미지원 파일 수**: {report['summary']['unsupported_count']} 개")
    lines.append("")
    
    lines.append("### 확장자별 분포")
    lines.append("| 확장자 | 파일 수 |")
    lines.append("| --- | --- |")
    for ext, count in sorted(report['summary']['extension_stats'].items(), key=lambda x: x[1], reverse=True):
        lines.append(f"| {ext if ext else '(없음)'} | {count} 개 |")
    lines.append("")
    
    lines.append("## 📂 스캔된 파일 목록")
    lines.append("| 파일명 | 상대 경로 | 크기 (KB) | 최종 수정일 | 지원 여부 |")
    lines.append("| --- | --- | --- | --- | --- |")
    for f in report['files']:
        supported_str = "✅ 지원됨" if f['supported'] else "❌ 미지원"
        size_kb = f['size_bytes'] / 1024
        lines.append(f"| {f['name']} | `{f['relative_path']}` | {size_kb:.1f} | {f['modified_time'][:10]} | {supported_str} |")
        
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f"Markdown 리포트가 저장되었습니다: {out_path}")

def main():
    parser = argparse.ArgumentParser(description="NAS/공유 디렉토리 파일 스캔 및 리포트 생성")
    parser.add_argument('--path', type=str, default='/home/caiser77/dgx_workspace/uploads', help='스캔할 대상 디렉토리 경로')
    parser.add_argument('--output-json', type=str, default='/home/caiser77/dgx_workspace/outputs/scan_report.json', help='결과를 저장할 JSON 파일 경로')
    parser.add_argument('--output-md', type=str, default='/home/caiser77/dgx_workspace/outputs/scan_report.md', help='결과를 저장할 MD 파일 경로')
    
    args = parser.parse_args()
    
    # 출력 폴더 생성
    os.makedirs(os.path.dirname(args.output_json), exist_ok=True)
    os.makedirs(os.path.dirname(args.output_md), exist_ok=True)
    
    print(f"스캔 시작: {args.path}")
    report = scan_directory(args.path)
    
    # JSON 저장
    with open(args.output_json, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=4, ensure_ascii=False)
    print(f"JSON 리포트가 저장되었습니다: {args.output_json}")
    
    # MD 저장
    write_markdown_report(report, args.output_md)
    
if __name__ == '__main__':
    main()
