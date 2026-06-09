import React from 'react';
import { EcologyReportViewer } from './EcologyReportViewer';
import { Loader2, Camera, Zap, X } from 'lucide-react';

export const SwarmModal = ({
  isOpen,
  onClose,
  swarmInputText,
  setSwarmInputText,
  isSwarmRunning,
  isExtractingText,
  swarmResult,
  onRunSwarm,
  onExtractText,
  showModalResult,
  setShowModalResult,
}) => {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 flex items-center justify-center z-[9999] p-4" style={{
      background: 'rgba(8,14,26,0.85)',
      backdropFilter: 'blur(8px)',
    }}>
      <div className="w-full max-w-4xl max-h-[85vh] flex flex-col overflow-hidden rounded-2xl" style={{
        background: '#0f1c32',
        border: '1px solid #1e3a5f',
        boxShadow: '0 32px 80px rgba(0,0,0,0.75)',
      }}>
        {/* Header */}
        <div className="px-6 py-4 flex justify-between items-center" style={{
          background: '#162440',
          borderBottom: '1px solid #1e3a5f',
        }}>
          <h3 className="text-sm font-bold text-opencode-light flex items-center gap-2.5">
            <span style={{
              width: 8, height: 8, borderRadius: 9999,
              background: '#34d399',
              boxShadow: '0 0 8px rgba(52,211,153,0.5)',
              display: 'inline-block',
            }} />
            AI Swarm 수색 조사야장 판독 및 통계 변환
          </h3>
          <button
            onClick={onClose}
            className="p-1.5 rounded-lg text-opencode-midGray hover:text-opencode-light transition-colors"
            style={{ background: 'rgba(255,255,255,0.05)' }}
          >
            <X size={14} />
          </button>
        </div>

        {/* Body */}
        <div className="flex-1 overflow-y-auto p-6">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
            {/* Input */}
            <div className="flex flex-col space-y-3">
              <div className="flex justify-between items-center">
                <span className="text-xs font-bold text-opencode-midGray uppercase tracking-wider">
                  현지 야장 원문 텍스트
                </span>
                <label className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold cursor-pointer transition-all" style={{
                  background: '#162440',
                  border: '1px solid #1e3a5f',
                  color: '#94a3b8',
                }}>
                  {isExtractingText
                    ? <><Loader2 className="w-3 h-3 animate-spin text-opencode-accentBlue" /> 판독 중...</>
                    : <><Camera className="w-3 h-3 text-opencode-accentBlue" /> 현지조사표 업로드 (OCR)</>
                  }
                  <input
                    type="file"
                    accept="image/*,application/pdf"
                    className="hidden"
                    onChange={onExtractText}
                    disabled={isExtractingText || isSwarmRunning}
                  />
                </label>
              </div>

              <textarea
                placeholder={`야생멧돼지 수색 조사야장 원문을 입력하거나, 상단 OCR 버튼으로 조사표를 업로드해 주세요.\n\n예:\n[조사 개요]\n조사자: 남택우, 날짜: 2026.05.06\n작업장소: 강원도 삼척시 도계읍 도계리 12번 격자\n멧돼지 1마리 사체 목격(상태 양호)`}
                value={swarmInputText}
                onChange={(e) => setSwarmInputText(e.target.value)}
                className="flex-1 min-h-[300px] text-xs font-mono leading-relaxed transition-all resize-none"
                style={{
                  background: '#162440',
                  border: '1px solid #1e3a5f',
                  borderRadius: 10,
                  color: '#e2e8f0',
                  padding: '12px',
                  outline: 'none',
                }}
                onFocus={e => e.target.style.borderColor = '#3b82f6'}
                onBlur={e => e.target.style.borderColor = '#1e3a5f'}
                disabled={isSwarmRunning}
              />
            </div>

            {/* Result */}
            <div className="flex flex-col rounded-xl p-5 min-h-[300px] overflow-y-auto" style={{
              background: '#162440',
              border: '1px solid #1e3a5f',
            }}>
              <span className="text-xs font-bold text-opencode-midGray uppercase tracking-wider mb-3 block">
                AI Swarm 판독 결과
              </span>

              {isSwarmRunning ? (
                <div className="flex-1 flex flex-col items-center justify-center space-y-3 py-10">
                  <Loader2 className="w-6 h-6 animate-spin text-opencode-accentBlue" />
                  <span className="text-sm text-opencode-midGray text-center leading-relaxed">
                    AI Swarm 협업 에이전트들이 야장을 해독하여<br />통계 데이터를 추출 중입니다...
                  </span>
                </div>
              ) : swarmResult ? (
                <div className="flex-1">
                  <EcologyReportViewer markdownText={swarmResult} />
                </div>
              ) : (
                <div className="flex-1 flex flex-col items-center justify-center text-center py-10">
                  <div className="p-4 rounded-xl mb-3" style={{ background: 'rgba(59,130,246,0.08)', border: '1px solid rgba(59,130,246,0.15)' }}>
                    <Zap className="w-7 h-7 text-opencode-accentBlue opacity-60 mx-auto" />
                  </div>
                  <p className="text-sm text-opencode-midGray leading-relaxed">
                    야장 텍스트를 기입한 뒤<br />아래 'AI Swarm 분석 실행'을 눌러 주세요.
                  </p>
                </div>
              )}
            </div>
          </div>
        </div>

        {/* Footer */}
        <div className="px-6 py-4 flex justify-between items-center" style={{
          background: '#162440',
          borderTop: '1px solid #1e3a5f',
        }}>
          <span className="text-xs text-opencode-midGray">
            AI Swarm 연산 시 종 마스터 인덱스 매핑 및 분류 자동 보정이 병행됩니다.
          </span>
          <div className="flex gap-2">
            <button
              onClick={onClose}
              className="px-4 py-2 rounded-lg text-sm font-semibold text-opencode-midGray hover:text-opencode-light transition-colors"
              style={{ background: '#0f1c32', border: '1px solid #1e3a5f' }}
            >
              닫기
            </button>
            <button
              onClick={onRunSwarm}
              disabled={isSwarmRunning || !swarmInputText.trim()}
              className="px-5 py-2 rounded-lg text-sm font-semibold text-white flex items-center gap-1.5 transition-all disabled:opacity-40"
              style={{
                background: 'linear-gradient(135deg, #1d4ed8 0%, #3b82f6 100%)',
                boxShadow: '0 0 16px rgba(59,130,246,0.25)',
              }}
            >
              {isSwarmRunning && <Loader2 className="w-3.5 h-3.5 animate-spin" />}
              AI Swarm 분석 실행
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};
