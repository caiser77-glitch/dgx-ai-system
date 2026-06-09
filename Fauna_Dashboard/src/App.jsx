import { useState, useEffect, useMemo } from 'react';
import ControlPanel from './components/ControlPanel';
import MapViewer from './components/MapViewer';
import EcologicalCharts from './components/EcologicalCharts';
import DataGrid from './components/DataGrid';

import { EcologyReportViewer } from './components/EcologyReportViewer';
import { ManualEntryModal } from './components/ManualEntryModal';
import { SwarmModal } from './components/SwarmModal';
import { useFaunaStats } from './hooks/useFaunaStats';
import { useFaunaApi } from './hooks/useFaunaApi';

import {
  ShieldAlert, Activity, Database, ChevronRight,
  TrendingUp, Wind, Zap, CheckCircle2, Loader2,
  Download, MapIcon, Layers, Printer, Leaf,
  LayoutDashboard, FileText, Bot, Table2,
  ChevronLeft, ChevronRight as ChevronRightIcon,
  Settings, Menu
} from 'lucide-react';
import { clsx } from 'clsx';
import { twMerge } from 'tailwind-merge';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';

delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon-2x.png',
  iconUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon.png',
  shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-shadow.png',
});

function cn(...inputs) { return twMerge(clsx(inputs)); }

const MOCK_DATA = [
  // ── 포유류·조류 (St. 1~4) ─────────────────────────────────────────────
  { id: 1,  surveyId: 1, site: "St. 1", species: "삵",    scientificName: "Prionailurus bengalensis",  class: "포유류", order: "식육목", family: "고양이과",  count: 2,  traces: "V", protected: "멸종위기 II급" },
  { id: 2,  surveyId: 1, site: "St. 2", species: "멧돼지", scientificName: "Sus scrofa",               class: "포유류", order: "우제목", family: "멧돼지과",  count: 5,  traces: "D", protected: null },
  { id: 3,  surveyId: 1, site: "St. 1", species: "다람쥐", scientificName: "Tamias sibiricus",         class: "포유류", order: "설치목", family: "다람쥐과",  count: 12, traces: "F", protected: null },
  { id: 4,  surveyId: 2, site: "St. 3", species: "삵",    scientificName: "Prionailurus bengalensis",  class: "포유류", order: "식육목", family: "고양이과",  count: 1,  traces: "V", protected: "멸종위기 II급" },
  { id: 5,  surveyId: 2, site: "St. 2", species: "너구리", scientificName: "Nyctereutes procyonoides", class: "포유류", order: "식육목", family: "개과",     count: 3,  traces: "D", protected: null },
  { id: 6,  surveyId: 2, site: "St. 3", species: "고라니", scientificName: "Hydropotes inermis",       class: "포유류", order: "우제목", family: "사슴과",   count: 8,  traces: "F", protected: null },
  { id: 7,  surveyId: 3, site: "St. 4", species: "삵",    scientificName: "Prionailurus bengalensis",  class: "포유류", order: "식육목", family: "고양이과",  count: 4,  traces: "V", protected: "멸종위기 II급" },
  { id: 8,  surveyId: 3, site: "St. 4", species: "수달",   scientificName: "Lutra lutra",               class: "포유류", order: "식육목", family: "족제비과", count: 1,  traces: "D", protected: "멸종위기 I급 / 제330호" },
  { id: 9,  surveyId: 3, site: "St. 2", species: "너구리", scientificName: "Nyctereutes procyonoides", class: "포유류", order: "식육목", family: "개과",     count: 2,  traces: "S", protected: null },
  { id: 10, surveyId: 4, site: "St. 1", species: "참매",   scientificName: "Accipiter gentilis",        class: "조류",  order: "수리목", family: "수리과",   count: 1,  traces: "V", protected: "천연기념물 제323-1호" },
  { id: 11, surveyId: 4, site: "St. 3", species: "삵",    scientificName: "Prionailurus bengalensis",  class: "포유류", order: "식육목", family: "고양이과",  count: 3,  traces: "F", protected: "멸종위기 II급" },
  { id: 12, surveyId: 4, site: "St. 4", species: "담비",   scientificName: "Martes flavigula",          class: "포유류", order: "식육목", family: "족제비과", count: 2,  traces: "D", protected: "멸종위기 II급" },
  // ── 어류 (St. 1~10) ──────────────────────────────────────────────────
  { id: 13, surveyId: 1, site: "St. 1",  species: "쉬리",   scientificName: "Coreoleuciscus splendidus", class: "어류", order: "잉어목", family: "잉어과",   count: 15, traces: "V", protected: null },
  { id: 14, surveyId: 1, site: "St. 2",  species: "참갈겨니", scientificName: "Zacco koreanus",          class: "어류", order: "잉어목", family: "잉어과",   count: 22, traces: "V", protected: null },
  { id: 15, surveyId: 1, site: "St. 3",  species: "피라미",  scientificName: "Zacco platypus",           class: "어류", order: "잉어목", family: "잉어과",   count: 31, traces: "V", protected: null },
  { id: 16, surveyId: 1, site: "St. 4",  species: "꺽지",   scientificName: "Coreoperca herzi",          class: "어류", order: "농어목", family: "꺽지과",   count: 8,  traces: "V", protected: null },
  { id: 17, surveyId: 1, site: "St. 5",  species: "돌고기",  scientificName: "Pungtungia herzi",         class: "어류", order: "잉어목", family: "잉어과",   count: 11, traces: "V", protected: null },
  { id: 18, surveyId: 1, site: "St. 6",  species: "묵납자루", scientificName: "Acheilognathus signifer", class: "어류", order: "잉어목", family: "잉어과",   count: 7,  traces: "V", protected: "멸종위기 II급" },
  { id: 19, surveyId: 1, site: "St. 7",  species: "버들치",  scientificName: "Rhynchocypris oxycephalus", class: "어류", order: "잉어목", family: "잉어과", count: 18, traces: "V", protected: null },
  { id: 20, surveyId: 1, site: "St. 8",  species: "참종개",  scientificName: "Iksookimia koreensis",     class: "어류", order: "미꾸리목", family: "미꾸리과", count: 9, traces: "V", protected: null },
  { id: 21, surveyId: 1, site: "St. 9",  species: "돌마자",  scientificName: "Microphysogobio yaluensis", class: "어류", order: "잉어목", family: "잉어과", count: 6,  traces: "V", protected: null },
  { id: 22, surveyId: 1, site: "St. 10", species: "한강납줄개", scientificName: "Rhodeus pseudosericeus", class: "어류", order: "잉어목", family: "잉어과", count: 4,  traces: "V", protected: "멸종위기 II급" },
  { id: 23, surveyId: 2, site: "St. 1",  species: "쉬리",   scientificName: "Coreoleuciscus splendidus", class: "어류", order: "잉어목", family: "잉어과",   count: 12, traces: "V", protected: null },
  { id: 24, surveyId: 2, site: "St. 5",  species: "돌고기",  scientificName: "Pungtungia herzi",         class: "어류", order: "잉어목", family: "잉어과",   count: 9,  traces: "V", protected: null },
  { id: 25, surveyId: 2, site: "St. 8",  species: "참종개",  scientificName: "Iksookimia koreensis",     class: "어류", order: "미꾸리목", family: "미꾸리과", count: 13, traces: "V", protected: null },
  // ── 저서무척추 (St. 1~12) ────────────────────────────────────────────
  { id: 26, surveyId: 1, site: "St. 1",  species: "부채하루살이", scientificName: "Epeorus pellucidus",   class: "저서무척추", order: "하루살이목", family: "납작하루살이과", count: 45, traces: "V", protected: null },
  { id: 27, surveyId: 1, site: "St. 2",  species: "민하루살이",   scientificName: "Baetis fuscatus",     class: "저서무척추", order: "하루살이목", family: "민하루살이과", count: 38, traces: "V", protected: null },
  { id: 28, surveyId: 1, site: "St. 3",  species: "강도래",       scientificName: "Kamimuria tibialis",  class: "저서무척추", order: "강도래목",   family: "강도래과",    count: 22, traces: "V", protected: null },
  { id: 29, surveyId: 1, site: "St. 4",  species: "각다귀",       scientificName: "Tipula sp.",          class: "저서무척추", order: "파리목",     family: "각다귀과",    count: 17, traces: "V", protected: null },
  { id: 30, surveyId: 1, site: "St. 5",  species: "물달팽이",     scientificName: "Radix auricularia",   class: "저서무척추", order: "기저류",     family: "물달팽이과",  count: 29, traces: "V", protected: null },
  { id: 31, surveyId: 1, site: "St. 6",  species: "재첩",         scientificName: "Corbicula fluminea",  class: "저서무척추", order: "이매패목",   family: "재첩과",      count: 56, traces: "V", protected: null },
  { id: 32, surveyId: 1, site: "St. 7",  species: "참게",         scientificName: "Eriocheir sinensis",  class: "저서무척추", order: "십각목",     family: "바위게과",    count: 14, traces: "V", protected: null },
  { id: 33, surveyId: 1, site: "St. 8",  species: "꼬마물벌레",   scientificName: "Hydropsyche sp.",     class: "저서무척추", order: "날도래목",   family: "줄날도래과",  count: 33, traces: "V", protected: null },
  { id: 34, surveyId: 1, site: "St. 9",  species: "물방개",       scientificName: "Cybister japonicus",  class: "저서무척추", order: "딱정벌레목", family: "물방개과",    count: 8,  traces: "V", protected: null },
  { id: 35, surveyId: 1, site: "St. 10", species: "다슬기",       scientificName: "Semisulcospira libertina", class: "저서무척추", order: "신생복족목", family: "다슬기과", count: 62, traces: "V", protected: null },
  { id: 36, surveyId: 1, site: "St. 11", species: "넓적하루살이", scientificName: "Heptagenia sulphurea", class: "저서무척추", order: "하루살이목", family: "넓적하루살이과", count: 27, traces: "V", protected: null },
  { id: 37, surveyId: 1, site: "St. 12", species: "두드럭조개",   scientificName: "Lamprotula coreana",  class: "저서무척추", order: "이매패목",   family: "석패과",      count: 11, traces: "V", protected: "멸종위기 II급" },
  { id: 38, surveyId: 2, site: "St. 3",  species: "강도래",       scientificName: "Kamimuria tibialis",  class: "저서무척추", order: "강도래목",   family: "강도래과",    count: 19, traces: "V", protected: null },
  { id: 39, surveyId: 2, site: "St. 7",  species: "참게",         scientificName: "Eriocheir sinensis",  class: "저서무척추", order: "십각목",     family: "바위게과",    count: 10, traces: "V", protected: null },
  { id: 40, surveyId: 2, site: "St. 11", species: "넓적하루살이", scientificName: "Heptagenia sulphurea", class: "저서무척추", order: "하루살이목", family: "넓적하루살이과", count: 24, traces: "V", protected: null },
];

const CATEGORIES = ["전체", "포유류", "조류", "어류", "양서파충류", "저서무척추"];

const NAV_ITEMS = [
  { id: 'dashboard', label: '대시보드',    subLabel: '통계 & 차트',          icon: LayoutDashboard },
  { id: 'data',      label: '데이터 조사표', subLabel: '분류군 조사 결과 표',   icon: Table2 },
  { id: 'species',   label: '보호종 & AI', subLabel: '보호종 현황 · 다양성',   icon: ShieldAlert },
  { id: 'map',       label: '조사 지도',   subLabel: '법정보호종 분포',         icon: MapIcon },
  { id: 'report',    label: '보고서',      subLabel: 'A4 실무 보고서',          icon: FileText },
];

/* ════════════════════════════════════════════════
   ROOT COMPONENT
   ════════════════════════════════════════════════ */
const App = () => {
  const [activeView,       setActiveView]       = useState('dashboard');
  const [sidebarCollapsed, setSidebarCollapsed] = useState(false);
  const [selectedCategory, setSelectedCategory] = useState('전체');
  const [activeSurvey,     setActiveSurvey]     = useState(1);
  const [selectedSite,     setSelectedSite]     = useState('전체');
  const [isCumulative,     setIsCumulative]     = useState(false);
  const [isAddingManual,   setIsAddingManual]   = useState(false);
  const [manualEntry,      setManualEntry]      = useState({ species: '', count: 1, traces: 'V', order: '포유류' });
  const [surveyData,       setSurveyData]       = useState(MOCK_DATA);
  const [protectedList,    setProtectedList]    = useState([]);
  const [speciesIndex,     setSpeciesIndex]     = useState({});
  const [showSwarmModal,   setShowSwarmModal]   = useState(false);
  const [swarmInputText,   setSwarmInputText]   = useState('');
  const [swarmResult,      setSwarmResult]      = useState(null);
  const [showModalResult,  setShowModalResult]  = useState(false);
  const [diversityResults, setDiversityResults] = useState(null);
  const [showBaseMap,        setShowBaseMap]        = useState(true);
  const [gisLayers,          setGisLayers]          = useState({ type: 'FeatureCollection', features: [] });
  const [isGisOverlayEnabled, setIsGisOverlayEnabled] = useState(true);
  const [gisBoundaryVisible,  setGisBoundaryVisible]  = useState(true);
  const [gisRangeVisible,     setGisRangeVisible]     = useState(true);

  const {
    BACKEND_URL, isCalculatingDiversity, isSwarmRunning,
    isExtractingText, isGisUploading,
    initLoad, saveToServer, calculateDiversity,
    runSwarm, extractSurveyText, uploadGis, clearGis,
  } = useFaunaApi(
    surveyData, setSurveyData, setActiveSurvey,
    setSwarmInputText, setSwarmResult, setShowModalResult,
    setDiversityResults, setGisLayers,
  );

  useEffect(() => {
    fetch('/data/species_search_index.json').then(r => r.json()).then(setSpeciesIndex).catch(console.error);
    fetch('/protected_species.json').then(r => r.json()).then(setProtectedList).catch(console.error);
    initLoad();
  }, []);

  useEffect(() => {
    const esc = (e) => { if (e.key === 'Escape') setShowSwarmModal(false); };
    if (showSwarmModal) window.addEventListener('keydown', esc);
    return () => window.removeEventListener('keydown', esc);
  }, [showSwarmModal]);

  // 데이터에서 차수·지점 목록 동적 추출
  const availableRounds = useMemo(() =>
    [...new Set(surveyData.map(d => d.surveyId))].sort((a, b) => a - b),
  [surveyData]);

  const availableSites = useMemo(() =>
    [...new Set(surveyData.map(d => d.site).filter(Boolean))]
      .sort((a, b) => {
        const na = parseInt(a.replace('St.', '').trim(), 10);
        const nb = parseInt(b.replace('St.', '').trim(), 10);
        return na - nb;
      }),
  [surveyData]);

  const stats = useFaunaStats(surveyData, activeSurvey, isCumulative, selectedCategory, speciesIndex, selectedSite);

  const handleAddManualEntry = () => {
    if (!manualEntry.species) return alert('종 이름을 입력해주세요.');
    const clean = manualEntry.species.replace(/\s+/g, '');
    const prot  = protectedList.find(p => p.name.replace(/\s+/g, '') === clean);
    const mstr  = speciesIndex[manualEntry.species] || {};
    setSurveyData(prev => [...prev, {
      id: prev.length + 1, surveyId: activeSurvey,
      species: manualEntry.species, scientificName: mstr.Scientific_Name || '',
      class: mstr.Class || '분류중...', order: manualEntry.order || mstr.Order || '기타',
      family: mstr.Family || '기타', count: parseInt(manualEntry.count) || 1,
      traces: manualEntry.traces, protected: prot?.rank || null,
    }]);
    setIsAddingManual(false);
    setManualEntry({ species: '', count: 1, traces: 'V', order: '포유류' });
  };

  const handleGisUpload = (e) => {
    const file = e.target.files[0];
    if (file) uploadGis(file, (n) => alert(`${n} 도면 레이어가 변환 및 중첩되었습니다.`));
  };
  const handleClearGis = async () => {
    if (confirm('모든 도면 레이어를 초기화하시겠습니까?')) {
      const ok = await clearGis();
      if (ok) alert('도면 레이어가 초기화되었습니다.');
    }
  };
  const downloadCSV  = () => window.open(`${BACKEND_URL}/api/download-csv?survey_id=${activeSurvey}&is_cumulative=${isCumulative}`, '_blank');
  const downloadHWPX = () => window.open(`${BACKEND_URL}/api/download-hwpx?survey_id=${activeSurvey}&is_cumulative=${isCumulative}`, '_blank');

  /* ── Sidebar width ── */
  const SW = sidebarCollapsed ? 64 : 220;

  return (
    <div style={{ display: 'flex', height: '100vh', overflow: 'hidden', background: '#080e1a' }}>

      {/* ══════════════════════════════════════════
          SIDEBAR (VS Code Activity Bar + Panel)
          ══════════════════════════════════════════ */}
      <aside style={{
        width: SW, flexShrink: 0,
        display: 'flex', flexDirection: 'column',
        background: '#060c18',
        borderRight: '1px solid #1e3a5f',
        transition: 'width 0.25s cubic-bezier(0.4,0,0.2,1)',
        overflow: 'hidden',
        zIndex: 40,
      }}>
        {/* Logo */}
        <div style={{
          padding: sidebarCollapsed ? '18px 0' : '18px 16px',
          display: 'flex', alignItems: 'center',
          justifyContent: sidebarCollapsed ? 'center' : 'space-between',
          borderBottom: '1px solid #1e3a5f',
          gap: 10, flexShrink: 0,
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
            <div style={{
              background: 'linear-gradient(135deg, #1d4ed8 0%, #3b82f6 100%)',
              borderRadius: 8, padding: 7, flexShrink: 0,
              boxShadow: '0 0 14px rgba(59,130,246,0.35)',
            }}>
              <Leaf size={16} color="#fff" />
            </div>
            {!sidebarCollapsed && (
              <div>
                <div style={{ fontSize: 13, fontWeight: 700, color: '#e2e8f0', lineHeight: 1.2, whiteSpace: 'nowrap' }}>
                  Fauna Dashboard
                </div>
                <div style={{ fontSize: 10, color: '#3b82f6', marginTop: 2, whiteSpace: 'nowrap' }}>
                  생태계 현지조사 시스템
                </div>
              </div>
            )}
          </div>
          {!sidebarCollapsed && (
            <button
              onClick={() => setSidebarCollapsed(true)}
              style={{
                background: 'rgba(255,255,255,0.04)', border: '1px solid #1e3a5f',
                borderRadius: 6, padding: '4px 6px', cursor: 'pointer', color: '#64748b', flexShrink: 0,
              }}
              title="사이드바 접기"
            >
              <ChevronLeft size={13} />
            </button>
          )}
          {sidebarCollapsed && (
            <button
              onClick={() => setSidebarCollapsed(false)}
              style={{
                background: 'transparent', border: 'none',
                cursor: 'pointer', color: '#64748b', padding: 0,
              }}
              title="사이드바 펼치기"
            >
              <Menu size={16} />
            </button>
          )}
        </div>

        {/* Nav Items */}
        <nav style={{ flex: 1, overflowY: 'auto', padding: '8px 0' }}>
          {NAV_ITEMS.map(item => {
            const active = activeView === item.id;
            const Icon = item.icon;
            return (
              <button
                key={item.id}
                onClick={() => setActiveView(item.id)}
                title={sidebarCollapsed ? item.label : undefined}
                style={{
                  width: '100%', display: 'flex', alignItems: 'center',
                  gap: 12, padding: sidebarCollapsed ? '12px 0' : '10px 16px',
                  justifyContent: sidebarCollapsed ? 'center' : 'flex-start',
                  background: active ? 'rgba(59,130,246,0.12)' : 'transparent',
                  border: 'none', borderLeft: active ? '2px solid #3b82f6' : '2px solid transparent',
                  cursor: 'pointer', transition: 'all 0.15s ease',
                  position: 'relative', textAlign: 'left',
                  marginBottom: 2,
                }}
                onMouseEnter={e => { if (!active) e.currentTarget.style.background = 'rgba(255,255,255,0.04)'; }}
                onMouseLeave={e => { if (!active) e.currentTarget.style.background = 'transparent'; }}
              >
                <Icon
                  size={18}
                  color={active ? '#3b82f6' : '#64748b'}
                  style={{ flexShrink: 0 }}
                />
                {!sidebarCollapsed && (
                  <div>
                    <div style={{ fontSize: 13, fontWeight: active ? 600 : 400, color: active ? '#e2e8f0' : '#94a3b8', lineHeight: 1.3, whiteSpace: 'nowrap' }}>
                      {item.label}
                    </div>
                    <div style={{ fontSize: 10, color: '#475569', whiteSpace: 'nowrap', marginTop: 1 }}>
                      {item.subLabel}
                    </div>
                  </div>
                )}
              </button>
            );
          })}

          {/* Divider */}
          <div style={{ height: 1, background: '#1e3a5f', margin: '8px 16px' }} />

          {/* AI 도우미 */}
          <button
            onClick={() => { setShowSwarmModal(true); setShowModalResult(false); }}
            title={sidebarCollapsed ? 'AI 도우미' : undefined}
            style={{
              width: '100%', display: 'flex', alignItems: 'center',
              gap: 12, padding: sidebarCollapsed ? '12px 0' : '10px 16px',
              justifyContent: sidebarCollapsed ? 'center' : 'flex-start',
              background: 'transparent', border: 'none', borderLeft: '2px solid transparent',
              cursor: 'pointer', transition: 'all 0.15s ease',
            }}
            onMouseEnter={e => e.currentTarget.style.background = 'rgba(255,255,255,0.04)'}
            onMouseLeave={e => e.currentTarget.style.background = 'transparent'}
          >
            <Bot size={18} color="#34d399" style={{ flexShrink: 0 }} />
            {!sidebarCollapsed && (
              <div>
                <div style={{ fontSize: 13, fontWeight: 400, color: '#94a3b8', lineHeight: 1.3, whiteSpace: 'nowrap' }}>
                  AI 도우미
                </div>
                <div style={{ fontSize: 10, color: '#475569', whiteSpace: 'nowrap', marginTop: 1 }}>
                  야장 판독 & Swarm 분석
                </div>
              </div>
            )}
          </button>
        </nav>

        {/* ── Survey Controls (bottom of sidebar) ── */}
        {!sidebarCollapsed && (
          <div style={{
            borderTop: '1px solid #1e3a5f',
            padding: '14px', flexShrink: 0,
            overflowY: 'auto', maxHeight: 360,
          }}>

            {/* 누적/독립 모드 토글 — 차수·지점 모두에 적용 */}
            <button
              onClick={() => setIsCumulative(!isCumulative)}
              style={{
                width: '100%', marginBottom: 12,
                padding: '7px 0', borderRadius: 7,
                fontSize: 11, fontWeight: 700, cursor: 'pointer',
                background: isCumulative ? 'rgba(52,211,153,0.12)' : '#162440',
                color: isCumulative ? '#34d399' : '#64748b',
                border: `1px solid ${isCumulative ? 'rgba(52,211,153,0.35)' : '#1e3a5f'}`,
                display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 6,
                transition: 'all 0.15s ease',
                boxShadow: isCumulative ? '0 0 10px rgba(52,211,153,0.15)' : 'none',
              }}
            >
              <Layers size={13} />
              {isCumulative ? '누적 모드 (차수 + 지점)' : '독립 모드 (차수 + 지점)'}
            </button>

            {/* ① 조사차수 — 데이터에서 동적 추출 */}
            <SidebarSection label="조사 차수">
              <div style={{
                maxHeight: 120, overflowY: 'auto',
                borderRadius: 8, border: '1px solid #1e3a5f',
                background: '#060c18',
              }}>
                {availableRounds.map((num, idx) => {
                  const active = activeSurvey === num;
                  const isCumIncluded = isCumulative && num <= activeSurvey;
                  return (
                    <button
                      key={num}
                      onClick={() => setActiveSurvey(num)}
                      style={{
                        width: '100%', padding: '7px 12px', textAlign: 'left',
                        fontSize: 12, fontWeight: active ? 700 : 400, cursor: 'pointer',
                        border: 'none',
                        borderBottom: idx < availableRounds.length - 1 ? '1px solid #1e3a5f' : 'none',
                        background: active
                          ? 'rgba(52,211,153,0.15)'
                          : isCumIncluded ? 'rgba(52,211,153,0.05)' : 'transparent',
                        color: active ? '#34d399' : isCumIncluded ? '#4a9a6a' : '#64748b',
                        display: 'flex', alignItems: 'center', justifyContent: 'space-between',
                        transition: 'background 0.12s ease',
                        boxSizing: 'border-box',
                      }}
                      onMouseEnter={e => { if (!active) e.currentTarget.style.background = 'rgba(255,255,255,0.04)'; }}
                      onMouseLeave={e => { if (!active) e.currentTarget.style.background = isCumIncluded ? 'rgba(52,211,153,0.05)' : 'transparent'; }}
                    >
                      <span style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{
                          width: 5, height: 5, borderRadius: '50%', flexShrink: 0,
                          background: active ? '#34d399' : isCumIncluded ? '#2d6b4a' : '#2d4a6e',
                          boxShadow: active ? '0 0 5px rgba(52,211,153,0.6)' : 'none',
                        }} />
                        {num}차 조사
                      </span>
                      {active && (
                        <span style={{ fontSize: 9, color: '#34d399', fontWeight: 700, letterSpacing: '0.05em' }}>
                          {isCumulative ? '기준' : '선택'}
                        </span>
                      )}
                    </button>
                  );
                })}
              </div>
            </SidebarSection>

            {/* ② 조사지점 — 데이터에서 동적 추출 */}
            <SidebarSection label={`조사 지점`} count={availableSites.length}>
              <div style={{
                maxHeight: 160, overflowY: 'auto',
                borderRadius: 8, border: '1px solid #1e3a5f',
                background: '#060c18',
              }}>
                {['전체', ...availableSites].map((site, idx) => {
                  const active = selectedSite === site;
                  const siteNum = parseInt(site.replace('St.', '').trim(), 10);
                  const selNum  = parseInt(selectedSite.replace('St.', '').trim(), 10);
                  const isCumIncluded = isCumulative && selectedSite !== '전체'
                    && !isNaN(siteNum) && siteNum <= selNum;
                  const totalLen = availableSites.length + 1;
                  return (
                    <button
                      key={site}
                      onClick={() => setSelectedSite(site)}
                      style={{
                        width: '100%',
                        padding: '5px 10px',   // 조밀하게
                        textAlign: 'left',
                        fontSize: 11, fontWeight: active ? 700 : 400, cursor: 'pointer',
                        border: 'none',
                        borderBottom: idx < totalLen - 1 ? '1px solid rgba(30,58,95,0.5)' : 'none',
                        background: active
                          ? 'rgba(59,130,246,0.15)'
                          : isCumIncluded ? 'rgba(59,130,246,0.05)' : 'transparent',
                        color: active ? '#3b82f6' : isCumIncluded ? '#3a5a8a' : '#64748b',
                        display: 'flex', alignItems: 'center', justifyContent: 'space-between',
                        transition: 'background 0.12s ease',
                        boxSizing: 'border-box',
                      }}
                      onMouseEnter={e => { if (!active) e.currentTarget.style.background = 'rgba(255,255,255,0.04)'; }}
                      onMouseLeave={e => { if (!active) e.currentTarget.style.background = isCumIncluded ? 'rgba(59,130,246,0.05)' : 'transparent'; }}
                    >
                      <span style={{ display: 'flex', alignItems: 'center', gap: 7 }}>
                        <span style={{
                          width: 4, height: 4, borderRadius: '50%', flexShrink: 0,
                          background: active ? '#3b82f6' : isCumIncluded ? '#2d4a6e' : '#1e3a5f',
                          boxShadow: active ? '0 0 4px rgba(59,130,246,0.7)' : 'none',
                        }} />
                        {site}
                      </span>
                      {active && selectedSite !== '전체' && (
                        <span style={{ fontSize: 9, color: '#3b82f6', fontWeight: 700, letterSpacing: '0.04em' }}>
                          {isCumulative ? '기준' : '선택'}
                        </span>
                      )}
                    </button>
                  );
                })}
              </div>
            </SidebarSection>

            {/* Live status */}
            <div style={{ display: 'flex', alignItems: 'center', gap: 6, marginTop: 8 }}>
              <span style={{ width: 6, height: 6, borderRadius: '50%', background: '#34d399', boxShadow: '0 0 5px rgba(52,211,153,0.6)', flexShrink: 0 }} />
              <span style={{ fontSize: 10, color: '#475569' }}>시스템 정상 동작 중</span>
            </div>
          </div>
        )}

        {/* Collapsed survey controls */}
        {sidebarCollapsed && (
          <div style={{ borderTop: '1px solid #1e3a5f', padding: '8px 0', display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 3 }}>
            <div style={{ fontSize: 8, color: '#2d4a6e', fontWeight: 700, marginBottom: 2, letterSpacing: '0.05em' }}>차수</div>
            {availableRounds.map(num => (
              <button
                key={num}
                onClick={() => setActiveSurvey(num)}
                title={`${num}차 조사`}
                style={{
                  width: 36, height: 22, borderRadius: 5, fontSize: 10, fontWeight: 700,
                  cursor: 'pointer', border: 'none',
                  background: activeSurvey === num ? 'linear-gradient(135deg,#059669,#34d399)' : '#162440',
                  color: activeSurvey === num ? '#fff' : '#64748b',
                  transition: 'all 0.15s',
                }}
              >
                {num}
              </button>
            ))}
            <div style={{ height: 1, width: 28, background: '#1e3a5f', margin: '3px 0' }} />
            <div style={{ fontSize: 8, color: '#2d4a6e', fontWeight: 700, marginBottom: 2, letterSpacing: '0.05em' }}>지점</div>
            {availableSites.map(site => {
              const active = selectedSite === site;
              const label = site.replace('St. ', 'S');
              return (
                <button
                  key={site}
                  onClick={() => setSelectedSite(active ? '전체' : site)}
                  title={site}
                  style={{
                    width: 36, height: 22, borderRadius: 5, fontSize: 9, fontWeight: 700,
                    cursor: 'pointer', border: `1px solid ${active ? 'rgba(59,130,246,0.4)' : 'transparent'}`,
                    background: active ? 'rgba(59,130,246,0.15)' : '#162440',
                    color: active ? '#3b82f6' : '#64748b',
                    transition: 'all 0.15s',
                  }}
                >
                  {label}
                </button>
              );
            })}
          </div>
        )}
      </aside>

      {/* ══════════════════════════════════════════
          MAIN AREA
          ══════════════════════════════════════════ */}
      <div style={{ flex: 1, display: 'flex', flexDirection: 'column', overflow: 'hidden', minWidth: 0 }}>

        {/* ── Top Toolbar ── */}
        <header style={{
          flexShrink: 0,
          background: '#0a1628',
          borderBottom: '1px solid #1e3a5f',
          padding: '0 20px',
          height: 48,
          display: 'flex', alignItems: 'center', justifyContent: 'space-between',
          gap: 12,
        }}>
          {/* Breadcrumb */}
          <div style={{ display: 'flex', alignItems: 'center', gap: 6, fontSize: 12, color: '#475569' }}>
            <span style={{ color: '#64748b' }}>Fauna</span>
            <ChevronRightIcon size={12} color="#2d4a6e" />
            <span style={{ color: '#94a3b8', fontWeight: 600 }}>
              {NAV_ITEMS.find(n => n.id === activeView)?.label || 'Dashboard'}
            </span>
          </div>

          {/* Toolbar actions */}
          <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
            {/* Category pills (shown only for dashboard/data) */}
            {['dashboard', 'data', 'species'].includes(activeView) && (
              <div style={{ display: 'flex', alignItems: 'center', gap: 4 }}>
                {CATEGORIES.map(cat => (
                  <button
                    key={cat}
                    onClick={() => setSelectedCategory(cat)}
                    style={{
                      padding: '4px 10px', borderRadius: 999,
                      fontSize: 11, fontWeight: 600, cursor: 'pointer',
                      border: 'none', transition: 'all 0.15s',
                      background: selectedCategory === cat
                        ? 'linear-gradient(135deg,#1d4ed8,#3b82f6)'
                        : '#162440',
                      color: selectedCategory === cat ? '#fff' : '#64748b',
                      boxShadow: selectedCategory === cat ? '0 0 10px rgba(59,130,246,0.25)' : 'none',
                    }}
                  >
                    {cat}
                  </button>
                ))}
              </div>
            )}

            <div style={{ width: 1, height: 24, background: '#1e3a5f' }} />

            {/* Download buttons */}
            <ToolbarButton onClick={() => setIsAddingManual(true)} title="직접 입력">
              <Database size={13} />
            </ToolbarButton>
            <ToolbarButton onClick={downloadCSV} title="엑셀 내보내기 (.csv)">
              <Download size={13} />
              <span style={{ fontSize: 11 }}>CSV</span>
            </ToolbarButton>
            <ToolbarButton onClick={downloadHWPX} title="한글 보고서 (.hwpx)" accent="#34d399">
              <Download size={13} />
              <span style={{ fontSize: 11 }}>HWPX</span>
            </ToolbarButton>
            {swarmResult && (
              <ToolbarButton
                onClick={() => {
                  const blob = new Blob([swarmResult], { type: 'text/markdown' });
                  const url = URL.createObjectURL(blob);
                  Object.assign(document.createElement('a'), { href: url, download: `현지조사_보고서_${new Date().toISOString().split('T')[0]}.md` }).click();
                }}
                title="AI 보고서 다운로드 (.md)"
                accent="#a78bfa"
              >
                <Download size={13} />
                <span style={{ fontSize: 11 }}>MD</span>
              </ToolbarButton>
            )}
            <ToolbarButton onClick={() => saveToServer(surveyData)} title="서버 저장" accent="#3b82f6">
              <CheckCircle2 size={13} />
            </ToolbarButton>
          </div>
        </header>

        {/* ── Content Area ── */}
        <main style={{ flex: 1, overflowY: 'auto', overflowX: 'hidden' }}>
          {activeView === 'dashboard' && (
            <DashboardView stats={stats} />
          )}
          {activeView === 'data' && (
            <DataView stats={stats} />
          )}
          {activeView === 'species' && (
            <SpeciesView
              stats={stats}
              diversityResults={diversityResults}
              isCalculatingDiversity={isCalculatingDiversity}
              onCalculate={calculateDiversity}
            />
          )}
          {activeView === 'map' && (
            <MapView
              stats={stats}
              gisLayers={gisLayers}
              isGisUploading={isGisUploading}
              isGisOverlayEnabled={isGisOverlayEnabled} setIsGisOverlayEnabled={setIsGisOverlayEnabled}
              gisBoundaryVisible={gisBoundaryVisible}   setGisBoundaryVisible={setGisBoundaryVisible}
              gisRangeVisible={gisRangeVisible}         setGisRangeVisible={setGisRangeVisible}
              showBaseMap={showBaseMap} setShowBaseMap={setShowBaseMap}
              onGisUpload={handleGisUpload}
              onClearGis={handleClearGis}
            />
          )}
          {activeView === 'report' && (
            <ReportView
              swarmResult={swarmResult}
              onPrint={() => window.print()}
              onDownloadMd={() => {
                const blob = new Blob([swarmResult], { type: 'text/markdown' });
                const url = URL.createObjectURL(blob);
                Object.assign(document.createElement('a'), { href: url, download: `현지조사_보고서_${new Date().toISOString().split('T')[0]}.md` }).click();
              }}
            />
          )}
        </main>
      </div>

      {/* ── Modals ── */}
      <ManualEntryModal
        isOpen={isAddingManual}
        onClose={() => setIsAddingManual(false)}
        manualEntry={manualEntry}
        setManualEntry={setManualEntry}
        onAddEntry={handleAddManualEntry}
      />
      <SwarmModal
        isOpen={showSwarmModal}
        onClose={() => setShowSwarmModal(false)}
        swarmInputText={swarmInputText}
        setSwarmInputText={setSwarmInputText}
        isSwarmRunning={isSwarmRunning}
        isExtractingText={isExtractingText}
        swarmResult={swarmResult}
        onRunSwarm={() => runSwarm(swarmInputText)}
        onExtractText={extractSurveyText}
        showModalResult={showModalResult}
        setShowModalResult={setShowModalResult}
      />
    </div>
  );
};

/* ════════════════════════════════════════════════
   TOOLBAR BUTTON
   ════════════════════════════════════════════════ */
function ToolbarButton({ children, onClick, title, accent }) {
  const [hover, setHover] = useState(false);
  return (
    <button
      onClick={onClick}
      title={title}
      onMouseEnter={() => setHover(true)}
      onMouseLeave={() => setHover(false)}
      style={{
        display: 'flex', alignItems: 'center', gap: 4,
        padding: '5px 10px', borderRadius: 6, fontSize: 12, fontWeight: 600,
        cursor: 'pointer', border: '1px solid #1e3a5f',
        background: hover ? (accent ? `${accent}18` : 'rgba(255,255,255,0.06)') : '#162440',
        color: hover ? (accent || '#e2e8f0') : '#64748b',
        transition: 'all 0.15s ease',
      }}
    >
      {children}
    </button>
  );
}

/* ════════════════════════════════════════════════
   STAT CARD
   ════════════════════════════════════════════════ */
function StatCard({ title, value, unit, icon, description, accentColor, gradient }) {
  return (
    <div style={{
      background: '#0f1c32', borderRadius: 12,
      border: `1px solid ${accentColor}25`,
      boxShadow: `0 4px 20px rgba(0,0,0,0.4), 0 0 0 1px ${accentColor}10`,
      padding: '20px', position: 'relative', overflow: 'hidden',
      transition: 'transform 0.2s ease',
    }}
    onMouseEnter={e => e.currentTarget.style.transform = 'translateY(-2px)'}
    onMouseLeave={e => e.currentTarget.style.transform = 'translateY(0)'}
    >
      <div style={{
        position: 'absolute', top: 0, right: 0, width: 90, height: 90,
        background: `radial-gradient(circle, ${accentColor}12 0%, transparent 70%)`,
        borderRadius: '0 12px',
      }} />
      <div style={{ position: 'relative' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 16 }}>
          <div style={{ background: gradient, borderRadius: 8, padding: 9, boxShadow: `0 0 12px ${accentColor}30` }}>
            <span style={{ color: '#fff', display: 'flex' }}>{icon}</span>
          </div>
          <span style={{
            fontSize: 9, fontWeight: 700, letterSpacing: '0.08em',
            padding: '3px 8px', borderRadius: 999,
            background: `${accentColor}15`, color: accentColor, border: `1px solid ${accentColor}25`,
          }}>LIVE</span>
        </div>
        <div style={{ fontSize: 11, fontWeight: 600, color: '#64748b', marginBottom: 6 }}>{title}</div>
        <div style={{ display: 'flex', alignItems: 'baseline', gap: 4, marginBottom: 4 }}>
          <span style={{ fontSize: 28, fontWeight: 800, color: '#e2e8f0', lineHeight: 1 }}>{value}</span>
          {unit && <span style={{ fontSize: 13, color: '#64748b' }}>{unit}</span>}
        </div>
        <div style={{ fontSize: 11, color: '#475569' }}>{description}</div>
      </div>
    </div>
  );
}

/* ════════════════════════════════════════════════
   PANEL WRAPPER (reusable card)
   ════════════════════════════════════════════════ */
function Panel({ title, accent = '#3b82f6', children, extra }) {
  return (
    <div style={{
      background: '#0f1c32', borderRadius: 12,
      border: '1px solid #1e3a5f',
      boxShadow: '0 4px 20px rgba(0,0,0,0.35)',
      overflow: 'hidden',
    }}>
      {(title || extra) && (
        <div style={{
          padding: '14px 20px',
          borderBottom: '1px solid #1e3a5f',
          background: '#162440',
          display: 'flex', alignItems: 'center', justifyContent: 'space-between',
        }}>
          {title && (
            <h3 style={{ display: 'flex', alignItems: 'center', gap: 10, fontSize: 13, fontWeight: 700, color: '#e2e8f0', margin: 0 }}>
              <span style={{ width: 3, height: 16, background: accent, borderRadius: 9999, flexShrink: 0, boxShadow: `0 0 6px ${accent}60` }} />
              {title}
            </h3>
          )}
          {extra}
        </div>
      )}
      <div style={{ padding: 20 }}>
        {children}
      </div>
    </div>
  );
}

/* ════════════════════════════════════════════════
   SIDEBAR SECTION HELPER
   ════════════════════════════════════════════════ */
function SidebarSection({ label, count, children }) {
  return (
    <div style={{ marginBottom: 14 }}>
      <div style={{
        fontSize: 9, fontWeight: 700, color: '#2d4a6e',
        textTransform: 'uppercase', letterSpacing: '0.1em',
        marginBottom: 7,
        display: 'flex', alignItems: 'center', gap: 6,
      }}>
        <span style={{ flex: 1, height: 1, background: '#1e3a5f' }} />
        {label}
        {count !== undefined && (
          <span style={{
            fontSize: 8, fontWeight: 700, color: '#3b82f6',
            background: 'rgba(59,130,246,0.12)',
            borderRadius: 4, padding: '1px 4px',
          }}>{count}</span>
        )}
        <span style={{ flex: 1, height: 1, background: '#1e3a5f' }} />
      </div>
      {children}
    </div>
  );
}

/* ════════════════════════════════════════════════
   VIEWS
   ════════════════════════════════════════════════ */

function DashboardView({ stats }) {
  const STAT_CARDS = [
    { title: "종 풍부도 (S)",      value: stats.richness,        unit: "종",  icon: <TrendingUp size={18} />, description: "전체 발견된 종의 수",  accentColor: '#3b82f6', gradient: 'linear-gradient(135deg,#1d4ed8,#3b82f6)' },
    { title: "총 개체수 (N)",      value: stats.totalAbundance,  unit: "개체", icon: <Database size={18} />,   description: "필터링된 표본 총합",    accentColor: '#34d399', gradient: 'linear-gradient(135deg,#059669,#34d399)' },
    { title: "Shannon Index (H')", value: stats.shannonIndex,    unit: "",    icon: <Wind size={18} />,       description: "종 다양성 지수",        accentColor: '#fbbf24', gradient: 'linear-gradient(135deg,#d97706,#fbbf24)' },
    { title: "Pielou Index (E)",   value: stats.pielouEvenness,  unit: "",    icon: <Zap size={18} />,        description: "종 균등도 0.0 ~ 1.0",  accentColor: '#a78bfa', gradient: 'linear-gradient(135deg,#7c3aed,#a78bfa)' },
  ];
  const GROUP_COLORS = ['#3b82f6', '#34d399', '#fbbf24', '#f87171', '#a78bfa'];

  return (
    <div style={{ padding: 24, display: 'flex', flexDirection: 'column', gap: 24 }}>
      {/* Stat row */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: 16 }}>
        {STAT_CARDS.map(c => <StatCard key={c.title} {...c} />)}
      </div>

      {/* Charts */}
      <EcologicalCharts stats={stats} />

      {/* Group summary */}
      <Panel title="분류군별 요약 보고서" accent="#34d399">
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(240px, 1fr))', gap: 12 }}>
          {stats.groupStats.map((g, idx) => {
            const c = GROUP_COLORS[idx % GROUP_COLORS.length];
            const pct = Math.min((g.abundance / (stats.totalAbundance || 1)) * 100, 100);
            return (
              <div key={g.name} style={{
                background: '#162440', borderRadius: 10,
                border: `1px solid ${c}20`, padding: 16,
                transition: 'transform 0.15s',
              }}
              onMouseEnter={e => e.currentTarget.style.transform = 'scale(1.01)'}
              onMouseLeave={e => e.currentTarget.style.transform = 'scale(1)'}
              >
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 12 }}>
                  <div>
                    <div style={{ fontSize: 10, fontWeight: 700, color: c, textTransform: 'uppercase', letterSpacing: '0.07em', marginBottom: 3 }}>Taxon</div>
                    <div style={{ fontSize: 14, fontWeight: 700, color: '#e2e8f0' }}>{g.name}</div>
                  </div>
                  <div style={{ textAlign: 'right' }}>
                    <div style={{ fontSize: 22, fontWeight: 800, color: '#e2e8f0', lineHeight: 1 }}>{g.species}<span style={{ fontSize: 11, fontWeight: 400, color: '#64748b', marginLeft: 3 }}>종</span></div>
                    <div style={{ fontSize: 10, color: '#475569', marginTop: 2 }}>{g.abundance} 개체</div>
                  </div>
                </div>
                <div style={{ height: 4, background: '#0f1c32', borderRadius: 9999, overflow: 'hidden' }}>
                  <div style={{ height: '100%', width: `${pct}%`, background: c, borderRadius: 9999, transition: 'width 0.6s ease' }} />
                </div>
              </div>
            );
          })}
        </div>
      </Panel>
    </div>
  );
}

function DataView({ stats }) {
  return (
    <div style={{ padding: 24 }}>
      <DataGrid stats={stats} />
    </div>
  );
}

function SpeciesView({ stats, diversityResults, isCalculatingDiversity, onCalculate }) {
  const protectedItems = stats.displayData.filter(d => d.protected);
  return (
    <div style={{ padding: 24, display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 20 }}>
      {/* 보호종 목록 */}
      <Panel title="보호종 관리 현황" accent="#3b82f6">
        <div style={{ marginBottom: 20, display: 'flex', justifyContent: 'space-between', alignItems: 'flex-end' }}>
          <div style={{ fontSize: 11, color: '#94a3b8' }}>관찰된 보호종</div>
          <div style={{ fontSize: 32, fontWeight: 800, color: '#e2e8f0', lineHeight: 1 }}>
            {protectedItems.length}<span style={{ fontSize: 13, fontWeight: 400, color: '#64748b', marginLeft: 4 }}>종</span>
          </div>
        </div>
        <div style={{ height: 6, background: '#162440', borderRadius: 9999, overflow: 'hidden', marginBottom: 16 }}>
          <div style={{
            height: '100%', borderRadius: 9999,
            width: `${(protectedItems.length / (stats.richness || 1)) * 100}%`,
            background: 'linear-gradient(90deg,#1d4ed8,#3b82f6)',
            boxShadow: '0 0 8px rgba(59,130,246,0.4)',
            transition: 'width 0.6s ease',
          }} />
        </div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 8, maxHeight: 300, overflowY: 'auto' }}>
          {protectedItems.map((d, i) => (
            <div key={i} style={{
              display: 'flex', justifyContent: 'space-between', alignItems: 'center',
              padding: '10px 14px', borderRadius: 8,
              background: '#162440', border: '1px solid rgba(248,113,113,0.15)',
            }}>
              <div>
                <div style={{ fontSize: 13, fontWeight: 600, color: '#e2e8f0' }}>{d.species}</div>
                <div style={{ fontSize: 10, color: '#64748b', fontStyle: 'italic', marginTop: 2 }}>{d.scientificName}</div>
              </div>
              <div style={{
                fontSize: 10, fontWeight: 600, padding: '3px 8px', borderRadius: 999,
                background: 'rgba(248,113,113,0.12)', color: '#f87171', border: '1px solid rgba(248,113,113,0.25)',
                whiteSpace: 'nowrap',
              }}>
                <ShieldAlert size={9} style={{ display: 'inline', marginRight: 3 }} />
                {d.protected}
              </div>
            </div>
          ))}
          {protectedItems.length === 0 && (
            <div style={{ textAlign: 'center', padding: '40px 0', color: '#475569', fontSize: 13 }}>
              현재 필터 조건에서 보호종 없음
            </div>
          )}
        </div>
      </Panel>

      {/* AI 다양성 진단 */}
      <Panel title="AI 생태 다양성 정밀 진단" accent="#34d399">
        {!diversityResults ? (
          <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
            <p style={{ fontSize: 12, color: '#94a3b8', lineHeight: 1.6 }}>
              FastAPI 통계 엔진으로 Shannon 다양성 지수, Simpson 우점도를 정밀 산출하고 생태계 건전성 신호등을 판별합니다.
            </p>
            <button
              onClick={onCalculate}
              disabled={isCalculatingDiversity}
              style={{
                padding: '12px 0', borderRadius: 8, border: 'none',
                background: 'linear-gradient(135deg,#059669,#34d399)',
                color: '#fff', fontSize: 13, fontWeight: 600,
                cursor: isCalculatingDiversity ? 'not-allowed' : 'pointer',
                opacity: isCalculatingDiversity ? 0.7 : 1,
                display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 8,
                boxShadow: '0 0 16px rgba(52,211,153,0.25)',
              }}
            >
              {isCalculatingDiversity ? <><Loader2 size={14} className="animate-spin" /> 분석 중...</> : <><Activity size={14} /> 정밀 지수 연산 실행</>}
            </button>
          </div>
        ) : (
          <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
            {Object.entries(diversityResults).map(([taxon, data]) => {
              let alertText = 'GREEN (안정)', badgeColor = '#34d399', badgeBg = 'rgba(52,211,153,0.12)', badgeBorder = 'rgba(52,211,153,0.25)';
              if (data.simpson >= 0.3)                                                     { alertText = 'RED (우점 심각)'; badgeColor = '#f87171'; badgeBg = 'rgba(248,113,113,0.12)'; badgeBorder = 'rgba(248,113,113,0.25)'; }
              else if (data.shannon < 2.0 || data.simpson >= 0.2 || data.evenness < 0.6)  { alertText = 'YELLOW (주의)';   badgeColor = '#fbbf24'; badgeBg = 'rgba(251,191,36,0.12)';  badgeBorder = 'rgba(251,191,36,0.25)'; }
              return (
                <div key={taxon} style={{ padding: '14px', background: '#162440', borderRadius: 10, border: '1px solid #1e3a5f' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 10 }}>
                    <span style={{ fontSize: 13, fontWeight: 600, color: '#e2e8f0' }}>{taxon}</span>
                    <span style={{ fontSize: 10, fontWeight: 700, padding: '3px 8px', borderRadius: 999, background: badgeBg, color: badgeColor, border: `1px solid ${badgeBorder}`, letterSpacing: '0.05em' }}>
                      {alertText}
                    </span>
                  </div>
                  <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: 8, textAlign: 'center' }}>
                    {[['Shannon H\'', data.shannon.toFixed(3), '#3b82f6'], ["Simpson D", data.simpson.toFixed(3), '#fbbf24'], ["Evenness E'", data.evenness.toFixed(3), '#a78bfa']].map(([l, v, c]) => (
                      <div key={l} style={{ background: '#0f1c32', borderRadius: 7, padding: '8px 0' }}>
                        <div style={{ fontSize: 9, color: '#475569', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.06em', marginBottom: 4 }}>{l}</div>
                        <div style={{ fontSize: 14, fontWeight: 800, color: c, fontFamily: 'monospace' }}>{v}</div>
                      </div>
                    ))}
                  </div>
                </div>
              );
            })}
            <button onClick={onCalculate} disabled={isCalculatingDiversity} style={{
              padding: '8px 0', borderRadius: 8, border: '1px solid #1e3a5f',
              background: '#162440', color: '#64748b', fontSize: 12, fontWeight: 600,
              cursor: isCalculatingDiversity ? 'not-allowed' : 'pointer',
              display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 6,
            }}>
              {isCalculatingDiversity && <Loader2 size={12} className="animate-spin" />} 재연산
            </button>
          </div>
        )}
      </Panel>
    </div>
  );
}

function MapView({ stats, gisLayers, isGisUploading, isGisOverlayEnabled, setIsGisOverlayEnabled, gisBoundaryVisible, setGisBoundaryVisible, gisRangeVisible, setGisRangeVisible, showBaseMap, setShowBaseMap, onGisUpload, onClearGis }) {
  return (
    <div style={{ display: 'flex', height: '100%', position: 'relative' }}>
      {/* GIS Control Panel */}
      <div style={{
        position: 'absolute', top: 16, left: 16, zIndex: 1000,
        width: 260, display: 'flex', flexDirection: 'column', gap: 10,
      }}>
        <div style={{ background: 'rgba(15,28,50,0.96)', border: '1px solid #1e3a5f', borderRadius: 12, padding: 14, backdropFilter: 'blur(8px)' }}>
          <div style={{ fontSize: 11, fontWeight: 700, color: '#3b82f6', marginBottom: 10 }}>GIS 도면 레이어 업로드</div>
          <div
            style={{ border: '2px dashed #1e3a5f', borderRadius: 8, padding: '14px 10px', textAlign: 'center', cursor: 'pointer', background: '#162440', transition: 'border-color 0.15s' }}
            onClick={() => document.getElementById('gis-map-input').click()}
          >
            {isGisUploading
              ? <><Loader2 size={18} style={{ color: '#3b82f6', margin: '0 auto 4px', display: 'block' }} className="animate-spin" /><div style={{ fontSize: 11, color: '#94a3b8' }}>변환 중...</div></>
              : <><Layers size={18} style={{ color: '#3b82f6', margin: '0 auto 6px', display: 'block' }} /><div style={{ fontSize: 11, color: '#e2e8f0', fontWeight: 600 }}>CAD · SHP · KML</div><div style={{ fontSize: 10, color: '#64748b', marginTop: 2 }}>파일 선택 또는 드래그</div></>
            }
          </div>
          <input id="gis-map-input" type="file" accept=".dxf,.kml,.zip" style={{ display: 'none' }} onChange={onGisUpload} />
          {gisLayers.features?.length > 0 && (
            <button onClick={onClearGis} style={{ marginTop: 8, width: '100%', padding: '6px 0', borderRadius: 7, border: '1px solid rgba(248,113,113,0.25)', background: 'rgba(248,113,113,0.1)', color: '#f87171', fontSize: 11, fontWeight: 600, cursor: 'pointer' }}>
              도면 전체 삭제
            </button>
          )}
        </div>

        <div style={{ background: 'rgba(15,28,50,0.96)', border: '1px solid #1e3a5f', borderRadius: 12, padding: 14, backdropFilter: 'blur(8px)' }}>
          <div style={{ fontSize: 11, fontWeight: 700, color: '#34d399', marginBottom: 10 }}>레이어 가시화 컨트롤</div>
          {[
            { label: '위성 배경 지도', state: showBaseMap, toggle: () => setShowBaseMap(!showBaseMap), color: '#34d399' },
            { label: '도면 오버레이', state: isGisOverlayEnabled, toggle: () => setIsGisOverlayEnabled(!isGisOverlayEnabled), color: '#3b82f6' },
          ].map(item => (
            <button key={item.label} onClick={item.toggle} style={{
              width: '100%', display: 'flex', justifyContent: 'space-between', alignItems: 'center',
              padding: '7px 10px', borderRadius: 7, marginBottom: 6, cursor: 'pointer',
              background: item.state ? `${item.color}18` : '#162440',
              border: `1px solid ${item.state ? `${item.color}30` : '#1e3a5f'}`,
              color: item.state ? item.color : '#64748b',
              fontSize: 11, fontWeight: 600,
            }}>
              <span>{item.label}</span>
              <span style={{ fontSize: 10 }}>{item.state ? '켬' : '끔'}</span>
            </button>
          ))}
        </div>
      </div>

      <MapViewer
        gisLayers={gisLayers}
        activeSurveyPoints={stats.filteredRaw.filter(d => d.latitude && d.longitude)}
        isGisOverlayEnabled={isGisOverlayEnabled}
        gisBoundaryVisible={gisBoundaryVisible}
        gisRangeVisible={gisRangeVisible}
        showBaseMap={showBaseMap}
      />
    </div>
  );
}

function ReportView({ swarmResult, onPrint, onDownloadMd }) {
  return (
    <div style={{ padding: 24, display: 'flex', flexDirection: 'column', gap: 16 }}>
      <div style={{
        display: 'flex', justifyContent: 'space-between', alignItems: 'center',
        background: '#0f1c32', border: '1px solid #1e3a5f', borderRadius: 12, padding: '14px 20px',
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
          <span style={{ width: 8, height: 8, borderRadius: '50%', background: '#34d399', boxShadow: '0 0 6px #34d399', display: 'inline-block' }} />
          <div>
            <div style={{ fontSize: 13, fontWeight: 700, color: '#e2e8f0' }}>A4 규격 실무 보고서 출력기</div>
            <div style={{ fontSize: 11, color: '#64748b', marginTop: 2 }}>인쇄 또는 PDF 저장 시 A4 흑백 가독성 모드로 변환됩니다.</div>
          </div>
        </div>
        <div style={{ display: 'flex', gap: 8 }}>
          {swarmResult && (
            <button onClick={onDownloadMd} style={{ padding: '8px 16px', borderRadius: 8, border: '1px solid #1e3a5f', background: '#162440', color: '#94a3b8', fontSize: 12, fontWeight: 600, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 6 }}>
              <Download size={13} /> 다운로드 (.md)
            </button>
          )}
          <button onClick={onPrint} style={{ padding: '8px 16px', borderRadius: 8, border: 'none', background: 'linear-gradient(135deg,#1d4ed8,#3b82f6)', color: '#fff', fontSize: 12, fontWeight: 600, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 6, boxShadow: '0 0 14px rgba(59,130,246,0.25)' }}>
            <Printer size={13} /> PDF 인쇄
          </button>
        </div>
      </div>

      <div style={{ background: '#fff', borderRadius: 12, padding: 40, minHeight: 900, border: '1px solid #e2e8f0', boxShadow: '0 4px 20px rgba(0,0,0,0.15)' }}>
        {swarmResult
          ? <div style={{ color: '#1e293b' }}><EcologyReportViewer markdownText={swarmResult} isPrintView={true} /></div>
          : <div style={{ textAlign: 'center', paddingTop: 120, color: '#94a3b8', fontSize: 14 }}>AI 분석 결과 대기 중 — 좌측 사이드바 [AI 도우미] 버튼으로 분석을 시작해 주세요.</div>
        }
      </div>
    </div>
  );
}

export default App;
