from fastapi import FastAPI, UploadFile, File, Body
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, Response
import google.generativeai as genai
import os
import sys
import json
from dotenv import load_dotenv
from PIL import Image
import io
from lxml import etree
from typing import List
from pydantic import BaseModel
import asyncio
from utils.hwpx_builder import HwpxBuilder
from utils.statistics_engine import calculate_diversity_indices

load_dotenv()

# Gemini 설정 (이미지 스캔 등 기본 기능용)
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-2.5-flash')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE_DIR = os.path.abspath(os.path.join(BASE_DIR, "../../Fauna_Workspace"))
DB_FILE = os.path.join(BASE_DIR, "database.json")

class SwarmInput(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Fauna AI Scan Server (MLX 8007 Engine) is Running!"}

@app.get("/load-data")
def load_data():
    parsed_json_file = os.path.join(WORKSPACE_DIR, "parsed_data.json")
    
    # 1. 만약 database.json이 존재하지 않거나 비어 있다면, parsed_data.json에서 읽어서 동기화해 줍니다.
    if not os.path.exists(DB_FILE) or os.path.getsize(DB_FILE) <= 2:
        if os.path.exists(parsed_json_file):
            try:
                with open(parsed_json_file, "r", encoding="utf-8") as pf:
                    raw_json = pf.read().strip()
                    if "```json" in raw_json: raw_json = raw_json.split("```json")[1].split("```")[0].strip()
                    elif "```" in raw_json: raw_json = raw_json.split("```")[1].split("```")[0].strip()
                    parsed_data = json.loads(raw_json)
                    
                    # database.json에 영구 저장하여 동기화
                    with open(DB_FILE, "w", encoding="utf-8") as df:
                        json.dump(parsed_data, df, ensure_ascii=False, indent=2)
            except Exception as e:
                print(f"Sync parsed_data.json to database.json failed: {e}")

    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            return {"error": str(e)}
    return []

@app.get("/api/get-survey-text")
def get_survey_text():
    path = os.path.join(WORKSPACE_DIR, "1_입력_야장기록.txt")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return {"text": f.read()}
    return {"text": ""}

@app.get("/api/get-report")
def get_report():
    path = os.path.join(WORKSPACE_DIR, "2_결과_최종보고서.md")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return {"report": f.read()}
    return {"report": ""}

@app.get("/api/download-csv")
def download_csv(survey_id: str = "all", is_cumulative: str = "false"):
    try:
        import csv
        import io
        from fastapi.responses import StreamingResponse
        
        parsed_data = []
        if os.path.exists(DB_FILE):
            with open(DB_FILE, "r", encoding="utf-8") as f:
                parsed_data = json.load(f)
                
        is_cum = is_cumulative.lower() == "true"
        
        if survey_id != "all":
            try:
                sid = int(survey_id)
                if is_cum:
                    parsed_data = [d for d in parsed_data if d.get("surveyId") <= sid]
                else:
                    parsed_data = [d for d in parsed_data if d.get("surveyId") == sid]
            except ValueError:
                pass

        # 1. 분류군별 정렬 (포유류, 조류, 어류, 양서파충류, 저서무척추 순)
        class_order = {"포유류": 1, "조류": 2, "어류": 3, "양서파충류": 4, "저서무척추": 5}
        
        def get_class_priority(c):
            c_clean = (c or "").replace("·", "").replace("성", "").strip()
            return class_order.get(c_clean, 99)

        # 데이터 정렬 (분류군 우선순위 -> 과 -> 종명)
        sorted_data = sorted(
            parsed_data, 
            key=lambda x: (
                get_class_priority(x.get("class")), 
                x.get("family", ""), 
                x.get("species", "")
            )
        )

        # CSV 작성을 위한 메모리 스트림 생성
        output = io.StringIO()
        writer = csv.writer(output)
        
        # 헤더 정렬 (['과', '학명', '종명', '개체수', '흔적', '법적보호종'])
        writer.writerow(['과', '학명', '종명', '개체수', '흔적', '법적보호종'])
        
        for item in sorted_data:
            # 2. 법적보호종 필터링 (일반종은 빈칸)
            protected_val = item.get("protected")
            if not protected_val or str(protected_val).lower() == "false" or str(protected_val) == "일반종":
                protected_str = ""
            else:
                protected_str = str(protected_val)
            
            # 3. 개체수는 단순 숫자만 표기
            count_val = str(item.get("count", 0))
            
            row = [
                item.get("family", ""),
                item.get("scientificName", ""),
                item.get("species", ""),
                count_val,
                item.get("traces", ""),
                protected_str
            ]
            writer.writerow(row)
            
        csv_data = output.getvalue()
        output.close()
        
        # UTF-8-BOM을 추가하여 엑셀에서 바로 열어도 한글이 깨지지 않도록 함
        bom_csv_data = io.BytesIO(b'\xef\xbb\xbf' + csv_data.encode('utf-8'))
        
        filename = f"fauna_data_v{survey_id}.csv" if survey_id != "all" else "fauna_data_all.csv"
        
        return StreamingResponse(
            bom_csv_data,
            media_type="text/csv",
            headers={"Content-Disposition": f"attachment; filename={filename}"}
        )

    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/api/download-hwpx")
def download_hwpx(survey_id: str = "all", is_cumulative: str = "false"):
    try:
        is_cum = is_cumulative.lower() == "true"
        
        # HWPX 리포트 빌더를 초기화하여 파일을 생성합니다.
        template_dir = os.path.join(BASE_DIR, "utils", "hwpx_templates")
        database_path = DB_FILE
        report_markdown_path = os.path.join(WORKSPACE_DIR, "2_결과_최종보고서.md")
        
        builder = HwpxBuilder(
            template_dir=template_dir,
            database_path=database_path,
            report_markdown_path=report_markdown_path
        )
        
        hwpx_stream = builder.build(survey_id=survey_id, is_cumulative=is_cum)
        
        filename = f"fauna_report_v{survey_id}.hwpx" if survey_id != "all" else "fauna_report_all.hwpx"
        
        return Response(
            content=hwpx_stream.getvalue(),
            media_type="application/hwpml-package+xml",
            headers={"Content-Disposition": f"attachment; filename={filename}"}
        )
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.post("/save-data")
async def save_data(data: List[dict] = Body(...)):
    try:
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.post("/api/swarm-analyze")
async def run_swarm_api(data: SwarmInput):
    """사용자 요청에 따라 MLX 8007 로컬 분석 엔진을 호출합니다."""
    input_file = os.path.join(WORKSPACE_DIR, "1_입력_야장기록.txt")
    script_path = os.path.join(WORKSPACE_DIR, "System_Engine/swarm_orchestrator.py")
    python_bin = sys.executable  # 현재 실행 중인 파이썬 환경 사용
    
    try:
        # 1. 입력받은 텍스트 저장
        with open(input_file, "w", encoding="utf-8") as f:
            f.write(data.text)
            
        # 2. MLX 8007 로컬 분석 엔진 실행
        process = await asyncio.create_subprocess_exec(
            python_bin, script_path,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()

        # 프로세스 실행 오류 처리 (LM Studio 미구동 또는 API 통신 장애 등)
        if process.returncode != 0:
            error_msg = stderr.decode(errors="ignore").strip()
            if "Connection error" in error_msg or "Failed to connect" in error_msg or "ConnectionRefusedError" in error_msg:
                error_msg = "로컬 MLX 서버(8007) 또는 LM Studio(1234)가 꺼져 있습니다. AI 서버 구동 상태를 확인해 주세요!"
            elif not error_msg:
                error_msg = stdout.decode(errors="ignore").strip() or "알 수 없는 서브프로세스 에러가 발생했습니다."
            return {"status": "error", "message": error_msg}
        
        # 3. 결과 파일 읽기
        parsed_json_file = os.path.join(WORKSPACE_DIR, "parsed_data.json")
        output_report_file = os.path.join(WORKSPACE_DIR, "2_결과_최종보고서.md")
        
        parsed_data = []
        report = ""

        if os.path.exists(parsed_json_file):
            with open(parsed_json_file, "r", encoding="utf-8") as f:
                raw_json = f.read().strip()
                # 불필요한 마크다운 제거
                if "```json" in raw_json: raw_json = raw_json.split("```json")[1].split("```")[0].strip()
                elif "```" in raw_json: raw_json = raw_json.split("```")[1].split("```")[0].strip()
                try:
                    parsed_data = json.loads(raw_json)
                except: pass
                
        if os.path.exists(output_report_file):
            with open(output_report_file, "r", encoding="utf-8") as f:
                report = f.read()

        return {"status": "success", "report": report, "data": parsed_data}
            
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.post("/api/extract-survey-text")
async def extract_survey_text(file: UploadFile = File(...)):
    """Gemini API를 사용하여 이미지 야장 문서로부터 텍스트를 정밀 추출합니다."""
    try:
        content = await file.read()

        # 파일 타입이 이미지인지 체크
        try:
            image = Image.open(io.BytesIO(content))
            prompt = (
                "이 이미지는 현지 생태 조사 야장 기록입니다. 이미지에 기록된 모든 텍스트 내용을 "
                "한 글자도 빠짐없이, 사람이 읽을 수 있는 깔끔한 텍스트 형식으로 정확하게 추출해 주세요. "
                "서론이나 부연 설명 없이 오직 야장에 기재된 텍스트 본문만을 한글로 반환하세요."
            )
            response = model.generate_content([prompt, image])
            text_result = response.text.strip()
        except Exception:
            # 이미지가 아닌 일반 텍스트 파일인 경우의 처리
            text_result = content.decode("utf-8", errors="ignore").strip()

        return {"status": "success", "text": text_result}
    except Exception as e:
        print(f"Error in extract_survey_text: {e}")
        return {"status": "error", "message": str(e)}

@app.post("/scan-note")
async def scan_note(file: UploadFile = File(...)):
    try:
        content = await file.read()
        image = Image.open(io.BytesIO(content))
        
        # Gemini 프롬프트에 JSON 구조를 더 명확하게 지시
        prompt = "야장 사진을 분석하여 발견된 생물종의 정보를 반드시 아래 JSON 형식으로만 응답하세요: {\"species\": \"종명\", \"traces\": \"흔적(V/D/F/S)\", \"count\": 개체수(숫자)}"
        response = model.generate_content([prompt, image])
        
        # 마크다운 코드 블록 제거 및 JSON 파싱
        raw_text = response.text.replace("```json", "").replace("```", "").strip()
        data = json.loads(raw_text)
        
        # 프론트엔드가 기대하는 구조로 래핑하여 반환
        return {
            "status": "success",
            "species": data.get("species", "미상"),
            "traces": data.get("traces", "-"),
            "count": int(data.get("count", 1))
        }
    except Exception as e:
        print(f"Error in scan_note: {e}")
        return {"status": "error", "message": str(e)}


# --- [NEW] GIS, CAD, SHP, KML PARSING AND VISUALIZATION PIPELINE ---

GIS_LAYERS_FILE = "project_gis_layers.json"

# 스마트 좌표 변환 도구 (한국 측량 도면 전형적인 좌표계 대응)
def convert_to_wgs84(x, y):
    import pyproj
    # 1. 이미 WGS84 위경도 범위 내라면 그대로 반환
    if 124.0 <= x <= 132.0 and 33.0 <= y <= 39.0:
        return x, y
    if 33.0 <= x <= 39.0 and 124.0 <= y <= 132.0:
        return y, x  # 위경도 반대로 입력된 경우 보정
        
    try:
        # 주요 좌표계들 선언
        # EPSG:5186 (Korea 2000 Central Belt - 환경영향평가서 CAD/SHP에서 가장 보편적)
        proj_5186 = pyproj.Transformer.from_crs("epsg:5186", "epsg:4326", always_xy=True)
        # EPSG:5179 (Korea Unified Grid / UTM-K - 산림청 및 국가공동망 표준)
        proj_5179 = pyproj.Transformer.from_crs("epsg:5179", "epsg:4326", always_xy=True)
        # EPSG:5181 (중부원점 - 다음지도/카카오맵 기준)
        proj_5181 = pyproj.Transformer.from_crs("epsg:5181", "epsg:4326", always_xy=True)
        # EPSG:3857 (Web Mercator - 구글/ESRI 타일 맵 기준)
        proj_3857 = pyproj.Transformer.from_crs("epsg:3857", "epsg:4326", always_xy=True)

        # 2. 범위별 적합한 투영계 추정 적용
        # 중부원점 (GRS80) 범위 추정
        if 150000 <= x <= 350000 and 300000 <= y <= 700000:
            lng, lat = proj_5186.transform(x, y)
            if 124.0 <= lng <= 132.0 and 33.0 <= lat <= 39.0:
                return lng, lat
                
        # UTM-K (Unified Grid) 범위 추정
        if 700000 <= x <= 1300000 and 1300000 <= y <= 2200000:
            lng, lat = proj_5179.transform(x, y)
            if 124.0 <= lng <= 132.0 and 33.0 <= lat <= 39.0:
                return lng, lat

        # 카카오/Daum TM 구좌표 범위 추정
        if 180000 <= x <= 220000 and 430000 <= y <= 470000:
            lng, lat = proj_5181.transform(x, y)
            if 124.0 <= lng <= 132.0 and 33.0 <= lat <= 39.0:
                return lng, lat

        # Web Mercator 미터단위 범위 추정
        if abs(x) > 1000000 or abs(y) > 1000000:
            lng, lat = proj_3857.transform(x, y)
            if 124.0 <= lng <= 132.0 and 33.0 <= lat <= 39.0:
                return lng, lat
    except Exception as e:
        print(f"Coordinate translation warning: {e}")
        
    return x, y

def parse_kml_to_geojson(kml_content: bytes):
    from lxml import etree
    parser = etree.XMLParser(recover=True)
    root = etree.fromstring(kml_content, parser)
    
    features = []
    # KML의 모든 Placemark 탐색
    placemarks = root.xpath("//*[local-name()='Placemark']")
    
    for pm in placemarks:
        name_els = pm.xpath(".//*[local-name()='name']")
        name = name_els[0].text if name_els else "KML 레이어"
        
        # 1. 다각형(Polygon) 검출
        poly_els = pm.xpath(".//*[local-name()='Polygon']")
        if poly_els:
            coord_els = poly_els[0].xpath(".//*[local-name()='coordinates']")
            if coord_els and coord_els[0].text:
                coord_text = coord_els[0].text.strip()
                coords = []
                for pt_str in coord_text.split():
                    pt_parts = pt_str.split(",")
                    if len(pt_parts) >= 2:
                        try:
                            lng, lat = convert_to_wgs84(float(pt_parts[0]), float(pt_parts[1]))
                            coords.append([lng, lat])
                        except ValueError:
                            pass
                if coords:
                    features.append({
                        "type": "Feature",
                        "properties": {
                            "name": name,
                            "layer_type": "Boundary" if "경계" in name or "boundary" in name.lower() else "Range"
                        },
                        "geometry": {
                            "type": "Polygon",
                            "coordinates": [coords]
                        }
                    })
                    continue

        # 2. 선(LineString) 검출
        line_els = pm.xpath(".//*[local-name()='LineString']")
        if line_els:
            coord_els = line_els[0].xpath(".//*[local-name()='coordinates']")
            if coord_els and coord_els[0].text:
                coord_text = coord_els[0].text.strip()
                coords = []
                for pt_str in coord_text.split():
                    pt_parts = pt_str.split(",")
                    if len(pt_parts) >= 2:
                        try:
                            lng, lat = convert_to_wgs84(float(pt_parts[0]), float(pt_parts[1]))
                            coords.append([lng, lat])
                        except ValueError:
                            pass
                if coords:
                    features.append({
                        "type": "Feature",
                        "properties": {
                            "name": name,
                            "layer_type": "Range"
                        },
                        "geometry": {
                            "type": "LineString",
                            "coordinates": coords
                        }
                    })
                    continue

    return {"type": "FeatureCollection", "features": features}

def parse_dxf_to_geojson(dxf_bytes: bytes):
    import ezdxf
    import tempfile
    
    with tempfile.NamedTemporaryFile(suffix=".dxf", delete=False) as tmp:
        tmp.write(dxf_bytes)
        tmp_path = tmp.name
        
    try:
        doc = ezdxf.readfile(tmp_path)
        msp = doc.modelspace()
        features = []
        
        # LWPOLYLINE, POLYLINE, LINE 쿼리하여 좌표 추출
        for entity in msp.query("LWPOLYLINE POLYLINE LINE"):
            coords = []
            layer_name = entity.dxf.layer
            
            if entity.dxftype() == "LINE":
                start = entity.dxf.start
                end = entity.dxf.end
                lng1, lat1 = convert_to_wgs84(start.x, start.y)
                lng2, lat2 = convert_to_wgs84(end.x, end.y)
                coords = [[lng1, lat1], [lng2, lat2]]
                geom_type = "LineString"
            else:
                for point in entity.get_points():
                    lng, lat = convert_to_wgs84(point[0], point[1])
                    coords.append([lng, lat])
                
                if entity.is_closed and len(coords) >= 3:
                    if coords[0] != coords[-1]:
                        coords.append(coords[0])
                    geom_type = "Polygon"
                    coords = [coords]
                else:
                    geom_type = "LineString"
            
            if len(coords) >= 2:
                features.append({
                    "type": "Feature",
                    "properties": {
                        "name": f"CAD 도면 레이어: {layer_name}",
                        "layer_type": "Boundary" if "경계" in layer_name or "boundary" in layer_name.lower() else "Range"
                    },
                    "geometry": {
                        "type": geom_type,
                        "coordinates": coords
                    }
                })
                
        return {"type": "FeatureCollection", "features": features}
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)

def parse_shp_zip_to_geojson(zip_bytes: bytes):
    import zipfile
    import tempfile
    import shapefile
    import shutil
    
    temp_dir = tempfile.mkdtemp()
    zip_path = os.path.join(temp_dir, "uploaded_shp.zip")
    with open(zip_path, "wb") as f:
        f.write(zip_bytes)
        
    try:
        with zipfile.ZipFile(zip_path, "r") as z:
            z.extractall(temp_dir)
            
        shp_file = None
        for f in os.listdir(temp_dir):
            if f.endswith(".shp"):
                shp_file = os.path.join(temp_dir, f)
                break
                
        if not shp_file:
            raise ValueError("ZIP 압축 파일 내부에 .shp 파일이 존재하지 않습니다.")
            
        sf = shapefile.Reader(shp_file)
        features = []
        
        for shape_record in sf.shapeRecords():
            shape = shape_record.shape
            record = shape_record.record
            
            name = "SHP 객체"
            if len(record) > 0:
                name = str(record[0])
                
            coords = []
            for pt in shape.points:
                lng, lat = convert_to_wgs84(pt[0], pt[1])
                coords.append([lng, lat])
                
            if not coords:
                continue
                
            # Polygon 타입인 경우 (PyShp 코드: 5)
            if shape.shapeType == 5:
                parts = list(shape.parts) + [len(shape.points)]
                rings = []
                for i in range(len(parts) - 1):
                    ring_coords = coords[parts[i]:parts[i+1]]
                    if ring_coords:
                        if ring_coords[0] != ring_coords[-1]:
                            ring_coords.append(ring_coords[0])
                        rings.append(ring_coords)
                if rings:
                    features.append({
                        "type": "Feature",
                        "properties": {
                            "name": name,
                            "layer_type": "Boundary" if "경계" in name or "boundary" in name.lower() else "Range"
                        },
                        "geometry": {
                            "type": "Polygon",
                            "coordinates": rings
                        }
                    })
            # LineString 타입인 경우 (PyShp 코드: 3)
            elif shape.shapeType == 3:
                parts = list(shape.parts) + [len(shape.points)]
                for i in range(len(parts) - 1):
                    part_coords = coords[parts[i]:parts[i+1]]
                    if len(part_coords) >= 2:
                        features.append({
                            "type": "Feature",
                            "properties": {
                                "name": name,
                                "layer_type": "Range"
                            },
                            "geometry": {
                                "type": "LineString",
                                "coordinates": part_coords
                            }
                        })
                        
        return {"type": "FeatureCollection", "features": features}
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)


@app.get("/api/get-gis-layers")
def get_gis_layers():
    """저장된 GIS 도면 레이어와 실시간 정제 완료된 생태 공간 좌표 피처들을 동적으로 융합하여 반환합니다."""
    combined_geojson = {"type": "FeatureCollection", "features": []}
    
    # 1. 업로드된 기존 GIS/CAD 도면 레이어 로드
    if os.path.exists(GIS_LAYERS_FILE):
        try:
            with open(GIS_LAYERS_FILE, "r", encoding="utf-8") as f:
                uploaded_data = json.load(f)
                if isinstance(uploaded_data, dict) and "features" in uploaded_data:
                    combined_geojson["features"].extend(uploaded_data["features"])
        except Exception as e:
            print(f"Error reading GIS layers file: {e}")
            
    # 2. 실시간 정제 완료된 생태 공간 좌표 GeoJSON 로드 및 실시간 병합
    refined_gis_path = os.path.join(WORKSPACE_DIR, "생태현장_정밀공간좌표_정제완료.geojson")
    if os.path.exists(refined_gis_path):
        try:
            with open(refined_gis_path, "r", encoding="utf-8") as f:
                refined_data = json.load(f)
                if isinstance(refined_data, dict) and "features" in refined_data:
                    # 융합 식별 속성 주입 (이름이 없는 경우를 대비한 가이드 매핑)
                    for feature in refined_data["features"]:
                        props = feature.setdefault("properties", {})
                        if "name" not in props:
                            props["name"] = props.get("species", "생태 조사 지점")
                    combined_geojson["features"].extend(refined_data["features"])
        except Exception as e:
            print(f"Error reading refined ecological GeoJSON: {e}")
            
    return combined_geojson

@app.post("/api/upload-gis")
async def upload_gis(file: UploadFile = File(...)):
    """CAD(.dxf), SHP(.zip), KML(.kml) 도면 파일을 읽어 표준 GeoJSON으로 파싱 및 영구 반영합니다."""
    filename = file.filename
    content = await file.read()
    
    try:
        if filename.endswith(".kml"):
            geojson = parse_kml_to_geojson(content)
        elif filename.endswith(".dxf"):
            geojson = parse_dxf_to_geojson(content)
        elif filename.endswith(".zip"):
            geojson = parse_shp_zip_to_geojson(content)
        else:
            return {"status": "error", "message": "지원하지 않는 파일 형식입니다. (.kml, .dxf, .zip(SHP 압축) 파일만 지원합니다.)"}
            
        # 기존 저장 파일이 있다면 로드하여 병합(Merge)
        existing = {"type": "FeatureCollection", "features": []}
        if os.path.exists(GIS_LAYERS_FILE):
            try:
                with open(GIS_LAYERS_FILE, "r", encoding="utf-8") as f:
                    existing = json.load(f)
            except:
                pass
                
        # 새 피처들 병합 및 중복 배제
        existing["features"].extend(geojson["features"])
        
        # 파일 저장
        with open(GIS_LAYERS_FILE, "w", encoding="utf-8") as f:
            json.dump(existing, f, ensure_ascii=False, indent=2)
            
        return {"status": "success", "geojson": existing}
    except Exception as e:
        print(f"Error parsing GIS file: {e}")
        import traceback
        traceback.print_exc()
        return {"status": "error", "message": f"GIS 파일 해독 중 오류가 발생했습니다: {str(e)}"}

@app.post("/api/clear-gis")
def clear_gis_layers():
    """모든 GIS 중첩 경계선 및 범위 레이어를 깨끗이 삭제합니다."""
    if os.path.exists(GIS_LAYERS_FILE):
        try:
            os.remove(GIS_LAYERS_FILE)
            return {"status": "success"}
        except Exception as e:
            return {"status": "error", "message": str(e)}
    return {"status": "success", "message": "삭제할 GIS 파일이 없습니다."}


@app.post("/api/analysis/summary")
async def api_analysis_summary(payload: dict = Body(...)):
    """종 다양성 통계 데이터를 가공하여 분석 지수 결과를 산출합니다."""
    try:
        diversity_data = payload.get("diversity", {})
        results = {}
        for group, info in diversity_data.items():
            counts = info.get("individual_counts", [])
            if counts:
                results[group] = calculate_diversity_indices(counts)
        return {"status": "success", "results": results}
    except Exception as e:
        return {"status": "error", "message": str(e)}



# Serve Static React files (Production)
dist_dir = os.path.abspath(os.path.join(BASE_DIR, "../dist"))
if os.path.exists(dist_dir):
    app.mount("/", StaticFiles(directory=dist_dir, html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8005)
