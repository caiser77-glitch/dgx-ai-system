import { useState } from 'react';

const BACKEND_URL = import.meta.env.VITE_API_BASE_URL || window.location.origin;

export const useFaunaApi = (surveyData, setSurveyData, setActiveSurvey, setSwarmInputText, setSwarmResult, setShowModalResult, setDiversityResults, setGisLayers) => {
  const [isCalculatingDiversity, setIsCalculatingDiversity] = useState(false);
  const [isSwarmRunning, setIsSwarmRunning] = useState(false);
  const [isExtractingText, setIsExtractingText] = useState(false);
  const [isGisUploading, setIsGisUploading] = useState(false);

  // 1. 초기 로컬 서버 데이터 로드
  const initLoad = async () => {
    try {
      const resData = await fetch(`${BACKEND_URL}/load-data`);
      const data = await resData.json();
      if (Array.isArray(data) && data.length > 0) {
        setSurveyData(data);
        const ids = [...new Set(data.map(d => d.surveyId))].filter(Boolean);
        if (ids.length > 0) {
          setActiveSurvey(Math.max(...ids));
        }
      }

      const resText = await fetch(`${BACKEND_URL}/api/get-survey-text`);
      const textObj = await resText.json();
      if (textObj.text) setSwarmInputText(textObj.text);

      const resReport = await fetch(`${BACKEND_URL}/api/get-report`);
      const reportObj = await resReport.json();
      if (reportObj.report) setSwarmResult(reportObj.report);
    } catch (err) {
      console.error("Initial backend load failed:", err);
    }
  };

  // 2. 서버 영구 저장 핸들러
  const saveToServer = async (currentData) => {
    try {
      const response = await fetch(`${BACKEND_URL}/save-data`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(currentData || surveyData),
      });
      const result = await response.json();
      if (result.status === "success") {
        alert("모든 데이터가 서버 파일(database.json)에 영구 저장되었습니다! 💾");
        return true;
      }
    } catch (error) {
      console.error("Save to Server Error:", error);
      alert("서버 저장 실패: 서버가 실행 중인지 확인하세요.");
    }
    return false;
  };

  // 3. 다양성 지수 정밀 통계 요청 핸들러
  const calculateDiversity = async () => {
    setIsCalculatingDiversity(true);
    try {
      const groups = ["포유류", "조류", "어류", "양서파충류", "저서무척추"];
      const diversityPayload = { diversity: {} };

      groups.forEach(g => {
        const filtered = surveyData.filter(d => {
          const group = d.class || "";
          if (g === "양서파충류") {
            return group === "양서류" || group === "파충류" || group === "양서파충류";
          }
          return group === g;
        });

        const countsMap = filtered.reduce((acc, curr) => {
          const name = curr.species || "Unknown";
          acc[name] = (acc[name] || 0) + (curr.count || 0);
          return acc;
        }, {});

        const countsArray = Object.values(countsMap);
        if (countsArray.length > 0) {
          diversityPayload.diversity[g] = {
            individual_counts: countsArray
          };
        }
      });

      const response = await fetch(`${BACKEND_URL}/api/analysis/summary`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(diversityPayload)
      });
      const result = await response.json();
      if (result.status === "success") {
        setDiversityResults(result.results);
        alert("FastAPI 백엔드 통계 엔진 연산 완료: 각 분류군별 정밀 다양성 지수가 대시보드에 정상적으로 반영되었습니다! 📊");
      } else {
        alert("다양성 지수 연산 실패: " + result.message);
      }
    } catch (err) {
      console.error("Diversity calculation failed:", err);
      alert("서버 연결 실패: 백엔드가 구동 중인지 확인하세요.");
    } finally {
      setIsCalculatingDiversity(false);
    }
  };

  // 4. AI Swarm 야장 판독 분석 실행 핸들러
  const runSwarm = async (textToAnalyze) => {
    setIsSwarmRunning(true);
    setSwarmResult(null);
    try {
      const response = await fetch(`${BACKEND_URL}/api/swarm-analyze`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: textToAnalyze }),
      });
      const result = await response.json();
      if (result.status === "success") {
        setSwarmResult(result.report);
        setShowModalResult(true);
        if (result.data && Array.isArray(result.data)) {
          const newData = result.data.map((item, index) => ({
            ...item,
            id: Date.now() + index,
            status: "확정",
            category: "AI 분석"
          }));

          if (newData.length > 0) {
            setSurveyData(newData);
            // 백엔드 영구 저장
            fetch(`${BACKEND_URL}/save-data`, {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify(newData),
            }).catch(err => console.error("Swarm Auto-save failed:", err));
          } else {
            alert("⚠️ 분석 결과에서 추출된 종 데이터가 없습니다. 야장 텍스트 형식을 확인하거나 잠시 후 다시 시도해주세요.");
          }
        }
      } else {
        alert("분석 오류: " + result.message);
      }
    } catch (error) {
      console.error("Swarm run error:", error);
      alert("서버 연결 실패: 백엔드가 켜져 있는지 확인하세요.");
    } finally {
      setIsSwarmRunning(false);
    }
  };

  // 5. 현지조사표 이미지/PDF OCR 텍스트 추출 핸들러
  const extractSurveyText = async (event) => {
    const file = event.target.files[0];
    if (!file) return;

    setIsExtractingText(true);
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch(`${BACKEND_URL}/api/extract-survey-text`, {
        method: 'POST',
        body: formData,
      });
      const result = await response.json();

      if (result.status === "success") {
        setSwarmInputText(prev => prev ? prev + "\n\n" + result.text : result.text);
      } else {
        alert("현지조사표 판독 실패: " + result.message);
      }
    } catch (error) {
      console.error("Extraction Error:", error);
      alert("서버 연결 실패: 백엔드가 켜져 있는지 확인하세요.");
    } finally {
      setIsExtractingText(false);
    }
  };

  // 6. GIS 도면(SHP, CAD 등) 업로드 핸들러
  const uploadGis = async (file, onGisSuccess) => {
    setIsGisUploading(true);
    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch(`${BACKEND_URL}/api/upload-gis`, {
        method: "POST",
        body: formData,
      });
      const data = await response.json();
      if (data.status === "success") {
        setGisLayers(data.geojson);
        if (onGisSuccess) onGisSuccess(file.name);
      } else {
        alert(`❌ 업로드 실패: ${data.message}`);
      }
    } catch (err) {
      console.error("GIS upload error:", err);
      alert("❌ 서버와 통신 중 오류가 발생했습니다.");
    } finally {
      setIsGisUploading(false);
    }
  };

  // 7. GIS 도면 레이어 초기화
  const clearGis = async () => {
    try {
      const response = await fetch(`${BACKEND_URL}/api/clear-gis`, {
        method: "POST"
      });
      const data = await response.json();
      if (data.status === "success") {
        setGisLayers({ type: "FeatureCollection", features: [] });
        return true;
      }
    } catch (err) {
      console.error("GIS clear error:", err);
      alert("도면 레이어 초기화 중 오류가 발생했습니다.");
    }
    return false;
  };

  return {
    BACKEND_URL,
    isCalculatingDiversity,
    isSwarmRunning,
    isExtractingText,
    isGisUploading,
    initLoad,
    saveToServer,
    calculateDiversity,
    runSwarm,
    extractSurveyText,
    uploadGis,
    clearGis
  };
};
