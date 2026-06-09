import React from 'react';
import { Database, Download, Layers, Bot } from 'lucide-react';

export default function ControlPanel({
  surveyIds = [1, 2, 3, 5],
  activeSurvey,
  setActiveSurvey,
  isCumulative,
  setIsCumulative,
  isAddingManual,
  setIsAddingManual,
  handleDownloadCSV,
  handleDownloadHWPX,
  swarmResult,
  setShowSwarmModal,
  setShowModalResult,
}) {
  const btnBase = {
    display: 'flex', alignItems: 'center', gap: 6,
    padding: '8px 16px', borderRadius: 8,
    fontSize: 13, fontWeight: 600,
    cursor: 'pointer', whiteSpace: 'nowrap',
    transition: 'all 0.15s ease',
    border: 'none', outline: 'none',
  };

  return (
    <div className="flex flex-wrap items-center gap-2">
      {/* AI 도우미 */}
      <button
        onClick={() => { setShowSwarmModal(true); setShowModalResult?.(false); }}
        style={{
          ...btnBase,
          background: 'linear-gradient(135deg, #1d4ed8 0%, #3b82f6 100%)',
          color: '#fff',
          boxShadow: '0 0 16px rgba(59,130,246,0.3)',
        }}
        onMouseEnter={e => { e.currentTarget.style.boxShadow = '0 0 20px rgba(59,130,246,0.45)'; e.currentTarget.style.transform = 'translateY(-1px)'; }}
        onMouseLeave={e => { e.currentTarget.style.boxShadow = '0 0 16px rgba(59,130,246,0.3)'; e.currentTarget.style.transform = 'translateY(0)'; }}
      >
        <Bot size={14} />
        AI 도우미
      </button>

      {/* 직접 입력 */}
      <button
        onClick={() => setIsAddingManual(!isAddingManual)}
        style={{
          ...btnBase,
          background: isAddingManual ? 'rgba(251,191,36,0.15)' : '#162440',
          color: isAddingManual ? '#fbbf24' : '#94a3b8',
          border: `1px solid ${isAddingManual ? 'rgba(251,191,36,0.3)' : '#1e3a5f'}`,
        }}
        onMouseEnter={e => e.currentTarget.style.color = isAddingManual ? '#fbbf24' : '#e2e8f0'}
        onMouseLeave={e => e.currentTarget.style.color = isAddingManual ? '#fbbf24' : '#94a3b8'}
      >
        <Database size={13} />
        직접 입력
      </button>

      {/* 엑셀 내보내기 */}
      <button
        onClick={handleDownloadCSV}
        className="no-print"
        style={{ ...btnBase, background: '#162440', color: '#94a3b8', border: '1px solid #1e3a5f' }}
        onMouseEnter={e => e.currentTarget.style.color = '#e2e8f0'}
        onMouseLeave={e => e.currentTarget.style.color = '#94a3b8'}
      >
        <Database size={12} />
        엑셀 내보내기
      </button>

      {/* 한글 보고서 */}
      <button
        onClick={handleDownloadHWPX}
        className="no-print"
        style={{
          ...btnBase,
          background: 'rgba(52,211,153,0.12)',
          color: '#34d399',
          border: '1px solid rgba(52,211,153,0.25)',
        }}
        onMouseEnter={e => e.currentTarget.style.background = 'rgba(52,211,153,0.2)'}
        onMouseLeave={e => e.currentTarget.style.background = 'rgba(52,211,153,0.12)'}
      >
        <Download size={12} />
        한글 보고서 (.hwpx)
      </button>

      {/* AI 보고서 다운로드 */}
      {swarmResult && (
        <button
          onClick={() => {
            const blob = new Blob([swarmResult], { type: 'text/markdown' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `현지조사_분석_보고서_${new Date().toISOString().split('T')[0]}.md`;
            a.click();
          }}
          style={{
            ...btnBase,
            background: 'rgba(167,139,250,0.12)',
            color: '#a78bfa',
            border: '1px solid rgba(167,139,250,0.25)',
          }}
        >
          <Download size={12} />
          보고서 다운로드 (.md)
        </button>
      )}

      {/* 조사 차수 선택 */}
      <div className="flex items-center gap-1 p-1 rounded-lg" style={{
        background: '#162440',
        border: '1px solid #1e3a5f',
      }}>
        {surveyIds.map((num) => (
          <button
            key={num}
            onClick={() => setActiveSurvey(num)}
            style={{
              padding: '6px 12px',
              borderRadius: 6,
              fontSize: 12,
              fontWeight: 600,
              cursor: 'pointer',
              border: 'none',
              outline: 'none',
              transition: 'all 0.15s ease',
              background: activeSurvey === num
                ? 'linear-gradient(135deg, #059669 0%, #34d399 100%)'
                : 'transparent',
              color: activeSurvey === num ? '#fff' : '#64748b',
              boxShadow: activeSurvey === num ? '0 0 10px rgba(52,211,153,0.25)' : 'none',
            }}
          >
            {num}차
          </button>
        ))}

        <div style={{ width: 1, height: 20, background: '#1e3a5f', margin: '0 2px' }} />

        <button
          onClick={() => setIsCumulative(!isCumulative)}
          style={{
            padding: '6px 12px',
            borderRadius: 6,
            fontSize: 12,
            fontWeight: 600,
            cursor: 'pointer',
            border: `1px solid ${isCumulative ? 'rgba(52,211,153,0.3)' : 'transparent'}`,
            outline: 'none',
            transition: 'all 0.15s ease',
            background: isCumulative ? 'rgba(52,211,153,0.1)' : 'transparent',
            color: isCumulative ? '#34d399' : '#64748b',
            display: 'flex', alignItems: 'center', gap: 5,
          }}
        >
          <Layers size={12} />
          {isCumulative ? '누적' : '독립'}
        </button>
      </div>
    </div>
  );
}
