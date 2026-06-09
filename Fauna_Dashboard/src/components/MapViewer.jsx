import React, { useEffect } from 'react';
import { MapContainer, TileLayer, CircleMarker, Popup, GeoJSON, Circle, useMap } from 'react-leaflet';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';

/**
 * ResizeMap Component
 * - Leaflet 지도의 레이아웃 크기를 렌더링 시점에 강제 업데이트하여 회색 화면 오류를 방지합니다.
 */
const ResizeMap = () => {
  const map = useMap();
  useEffect(() => {
    const timer = setTimeout(() => {
      map.invalidateSize();
    }, 400);
    return () => clearTimeout(timer);
  }, [map]);
  return null;
};

/**
 * AutoFitBounds Component
 * - 새롭게 로드된 GIS 도면 레이어 영역으로 지도의 초점을 자동으로 포커싱하고 줌인합니다.
 */
const AutoFitBounds = ({ geojson }) => {
  const map = useMap();
  useEffect(() => {
    if (geojson && geojson.features && geojson.features.length > 0) {
      try {
        const geojsonLayer = L.geoJSON(geojson);
        const bounds = geojsonLayer.getBounds();
        if (bounds.isValid()) {
          map.fitBounds(bounds, { padding: [50, 50], maxZoom: 15 });
        }
      } catch (err) {
        console.error("AutoFitBounds error:", err);
      }
    }
  }, [geojson, map]);
  return null;
};

// Leaflet 기본 마커 아이콘의 깨진 경로 복구
if (typeof L !== 'undefined' && L.Icon && L.Icon.Default) {
  delete L.Icon.Default.prototype._getIconUrl;
  L.Icon.Default.mergeOptions({
    iconRetinaUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon-2x.png',
    iconUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-shadow.png',
  });
}

/**
 * MapViewer Component
 * - 대시보드 리팩토링의 2단계로 분리된 Leaflet 기반의 GIS 지도 렌더링 전담 컴포넌트입니다.
 * - 수달 보호구역 500m 버퍼 및 CAD/KML 도면 경계선 가시화 등 고도화된 생태 정보를 오버레이합니다.
 */
export default function MapViewer({
  gisLayers,
  activeSurveyPoints = [],
  isGisOverlayEnabled = true,
  gisBoundaryVisible = true,
  gisRangeVisible = true,
  showBaseMap = true
}) {
  return (
    <MapContainer
      center={[37.647, 127.318]}
      zoom={13}
      style={{ height: '100%', width: '100%', position: 'absolute', top: 0, left: 0, right: 0, bottom: 0 }}
      className="z-0"
    >
      <ResizeMap />
      <AutoFitBounds geojson={gisLayers} />

      {/* 기본 위성 지도 레이어 */}
      {showBaseMap && (
        <TileLayer
          url="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"
          attribution='&copy; <a href="https://www.esri.com/">Esri</a>'
        />
      )}

      {/* 업로드된 GIS / CAD / KML 레이어 중첩 가시화 (경계선 vs 범위 분기) */}
      {isGisOverlayEnabled && gisLayers && gisLayers.features && gisLayers.features.length > 0 && (
        <GeoJSON
          key={JSON.stringify(gisLayers.features) + gisBoundaryVisible + gisRangeVisible}
          data={{
            type: "FeatureCollection",
            features: gisLayers.features.filter(f => {
              const type = f.properties?.layer_type || "Range";
              if (type === "Boundary") return gisBoundaryVisible;
              return gisRangeVisible;
            })
          }}
          style={(feature) => {
            const type = feature.properties?.layer_type || "Range";
            if (type === "Boundary") {
              return {
                color: "#f43f5e", // Rose 500 (Red)
                weight: 4,
                opacity: 0.9,
                fillColor: "#f43f5e",
                fillOpacity: 0.12,
                dashArray: "6, 6" // 경계선용 점선
              };
            } else {
              return {
                color: "#6366f1", // Indigo 500
                weight: 3,
                opacity: 0.85,
                fillColor: "#6366f1",
                fillOpacity: 0.08,
              };
            }
          }}
          onEachFeature={(feature, layer) => {
            const name = feature.properties?.name || "도면 레이어";
            const type = feature.properties?.layer_type === "Boundary" ? "사업지역 경계선" : "조사범위";
            layer.bindPopup(
              `<div style="font-family: sans-serif; padding: 4px; min-width: 140px;">
                 <span style="display: inline-block; padding: 2px 6px; font-size: 9px; font-weight: bold; background: ${feature.properties?.layer_type === "Boundary" ? "#ffe4e6; color: #e11d48;" : "#e0e7ff; color: #4f46e5;"} ; border-radius: 4px; margin-bottom: 6px;">
                   ${type}
                 </span>
                 <h4 style="margin: 0; font-size: 12px; font-weight: 800; color: #1e293b;">${name}</h4>
               </div>`
            );
          }}
        />
      )}

      {/* 야장(field notes) 실시간 위경도 좌표점 중첩 가시화 (Emerald Green 마커 및 수달 500m 버퍼) */}
      {activeSurveyPoints.map((item) => (
        <React.Fragment key={item.id || `${item.species}-${item.surveyId}-${item.latitude}`}>
          <CircleMarker
            center={[item.latitude, item.longitude]}
            radius={9}
            fillColor="#10b981"
            color="#ffffff"
            weight={2}
            opacity={1}
            fillOpacity={0.95}
          >
            <Popup>
              <div className="p-2 text-slate-900" style={{ minWidth: '160px' }}>
                <span className="inline-block px-1.5 py-0.5 bg-emerald-500 text-white rounded text-[9px] font-black mb-1.5 uppercase tracking-wider">
                  야장 실시간 지점
                </span>
                <h3 className="font-black text-slate-800 text-sm">{item.species} ({item.scientificName})</h3>
                <p className="text-xs text-slate-600 mt-1">조사 시기: <b>{item.surveyId}차 조사</b></p>
                <p className="text-xs text-slate-600">발견 흔적: <b>{item.traces} ({item.count}개체)</b></p>
                {item.protected && (
                  <p className="text-[10px] text-amber-600 font-extrabold mt-1.5 flex items-center gap-1">
                    🛡️ {item.protected}
                  </p>
                )}
              </div>
            </Popup>
          </CircleMarker>

          {/* 수달(Otter)일 경우 반경 500m 보호 버퍼 영역 실시간 가시화 */}
          {item.species === "수달" && (
            <Circle
              center={[item.latitude, item.longitude]}
              radius={500}
              pathOptions={{
                fillColor: "#ff4d4d",
                fillOpacity: 0.15,
                color: "#ff4d4d",
                weight: 1.5,
                dashArray: "4, 4"
              }}
            >
              <Popup>
                <div className="p-2 text-slate-900" style={{ minWidth: '150px' }}>
                  <span className="inline-block px-1.5 py-0.5 bg-rose-500 text-white rounded text-[9px] font-black mb-1.5 uppercase tracking-wider">
                    수달 보호구역 (Buffer)
                  </span>
                  <p className="text-xs text-slate-700 font-bold leading-normal mt-1">
                    실측 좌표 기준<br />
                    <b>반경 500m 핵심 서식 보전 권역</b>
                  </p>
                </div>
              </Popup>
            </Circle>
          )}
        </React.Fragment>
      ))}
    </MapContainer>
  );
}
