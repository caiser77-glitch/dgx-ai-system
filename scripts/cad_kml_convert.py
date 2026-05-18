import sys
from pathlib import Path
import xml.etree.ElementTree as ET

import ezdxf
import simplekml
from pyproj import Transformer

WGS84 = "EPSG:4326"
KOREA_TM = "EPSG:5186"

to_tm = Transformer.from_crs(WGS84, KOREA_TM, always_xy=True)
to_wgs = Transformer.from_crs(KOREA_TM, WGS84, always_xy=True)


def parse_kml_coordinates(kml_path):
    ns = {"kml": "http://www.opengis.net/kml/2.2"}
    tree = ET.parse(kml_path)
    root = tree.getroot()
    groups = []

    for node in root.findall(".//kml:coordinates", ns):
        if not node.text:
            continue

        pts = []
        for item in node.text.strip().split():
            parts = item.split(",")
            if len(parts) >= 2:
                lon = float(parts[0])
                lat = float(parts[1])
                x, y = to_tm.transform(lon, lat)
                pts.append((x, y))

        if pts:
            groups.append(pts)

    return groups


def kml_to_dxf(input_file, output_file):
    groups = parse_kml_coordinates(input_file)

    # R12 DXF로 저장: 호환성 높음
    doc = ezdxf.new("R12")
    msp = doc.modelspace()

    for pts in groups:
        if len(pts) == 1:
            x, y = pts[0]
            msp.add_circle((x, y), radius=2)
        else:
            closed = pts[0] == pts[-1]
            msp.add_polyline2d(pts, close=closed)

    doc.saveas(output_file)


def dxf_to_kml_by_ezdxf(input_file, output_file):
    doc = ezdxf.readfile(input_file)
    msp = doc.modelspace()
    kml = simplekml.Kml()

    for e in msp:
        if e.dxftype() == "LWPOLYLINE":
            coords = []
            for p in e.get_points():
                x, y = p[0], p[1]
                lon, lat = to_wgs.transform(x, y)
                coords.append((lon, lat))
            if coords:
                kml.newlinestring(name="DXF LWPOLYLINE", coords=coords)

        elif e.dxftype() == "POLYLINE":
            coords = []
            for v in e.vertices:
                loc = v.dxf.location
                lon, lat = to_wgs.transform(loc.x, loc.y)
                coords.append((lon, lat))
            if coords:
                kml.newlinestring(name="DXF POLYLINE", coords=coords)

        elif e.dxftype() == "LINE":
            start = e.dxf.start
            end = e.dxf.end
            lon1, lat1 = to_wgs.transform(start.x, start.y)
            lon2, lat2 = to_wgs.transform(end.x, end.y)
            kml.newlinestring(name="DXF LINE", coords=[(lon1, lat1), (lon2, lat2)])

        elif e.dxftype() == "CIRCLE":
            center = e.dxf.center
            lon, lat = to_wgs.transform(center.x, center.y)
            kml.newpoint(name="DXF CIRCLE CENTER", coords=[(lon, lat)])

    kml.save(output_file)


def read_dxf_pairs(input_file):
    lines = Path(input_file).read_text(errors="ignore").splitlines()
    pairs = []
    i = 0
    while i + 1 < len(lines):
        code = lines[i].strip()
        value = lines[i + 1].strip()
        pairs.append((code, value))
        i += 2
    return pairs


def dxf_to_kml_by_raw_parser(input_file, output_file):
    pairs = read_dxf_pairs(input_file)
    kml = simplekml.Kml()

    i = 0
    while i < len(pairs):
        code, value = pairs[i]

        # LINE
        if code == "0" and value == "LINE":
            x1 = y1 = x2 = y2 = None
            i += 1
            while i < len(pairs) and pairs[i][0] != "0":
                c, v = pairs[i]
                if c == "10":
                    x1 = float(v)
                elif c == "20":
                    y1 = float(v)
                elif c == "11":
                    x2 = float(v)
                elif c == "21":
                    y2 = float(v)
                i += 1

            if None not in (x1, y1, x2, y2):
                lon1, lat1 = to_wgs.transform(x1, y1)
                lon2, lat2 = to_wgs.transform(x2, y2)
                kml.newlinestring(name="DXF LINE", coords=[(lon1, lat1), (lon2, lat2)])
            continue

        # LWPOLYLINE
        if code == "0" and value == "LWPOLYLINE":
            pts = []
            current_x = None
            i += 1
            while i < len(pairs) and pairs[i][0] != "0":
                c, v = pairs[i]
                if c == "10":
                    current_x = float(v)
                elif c == "20" and current_x is not None:
                    y = float(v)
                    pts.append((current_x, y))
                    current_x = None
                i += 1

            if pts:
                coords = []
                for x, y in pts:
                    lon, lat = to_wgs.transform(x, y)
                    coords.append((lon, lat))
                kml.newlinestring(name="DXF LWPOLYLINE", coords=coords)
            continue

        # POLYLINE / VERTEX / SEQEND
        if code == "0" and value == "POLYLINE":
            pts = []
            i += 1
            while i < len(pairs):
                c, v = pairs[i]

                if c == "0" and v == "VERTEX":
                    vx = vy = None
                    i += 1
                    while i < len(pairs) and pairs[i][0] != "0":
                        cc, vv = pairs[i]
                        if cc == "10":
                            vx = float(vv)
                        elif cc == "20":
                            vy = float(vv)
                        i += 1
                    if vx is not None and vy is not None:
                        pts.append((vx, vy))
                    continue

                if c == "0" and v == "SEQEND":
                    i += 1
                    break

                i += 1

            if pts:
                coords = []
                for x, y in pts:
                    lon, lat = to_wgs.transform(x, y)
                    coords.append((lon, lat))
                kml.newlinestring(name="DXF POLYLINE", coords=coords)
            continue

        i += 1

    kml.save(output_file)


def dxf_to_kml(input_file, output_file):
    try:
        dxf_to_kml_by_ezdxf(input_file, output_file)
    except Exception as e:
        print(f"ezdxf 읽기 실패 → 원문 파서로 전환: {e}")
        dxf_to_kml_by_raw_parser(input_file, output_file)


def main():
    if len(sys.argv) < 4:
        print("사용법:")
        print("python scripts/cad_kml_convert.py kml_to_dxf input.kml output.dxf")
        print("python scripts/cad_kml_convert.py dxf_to_kml input.dxf output.kml")
        sys.exit(1)

    mode = sys.argv[1]
    input_file = Path(sys.argv[2])
    output_file = Path(sys.argv[3])
    output_file.parent.mkdir(parents=True, exist_ok=True)

    if mode == "kml_to_dxf":
        kml_to_dxf(input_file, output_file)
    elif mode == "dxf_to_kml":
        dxf_to_kml(input_file, output_file)
    else:
        raise ValueError("mode는 kml_to_dxf 또는 dxf_to_kml 이어야 합니다.")

    print(f"변환 완료: {output_file}")


if __name__ == "__main__":
    main()
