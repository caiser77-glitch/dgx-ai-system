import React from 'react';
import { X } from 'lucide-react';

const inputStyle = {
  width: '100%',
  background: '#162440',
  border: '1px solid #1e3a5f',
  color: '#e2e8f0',
  fontSize: 13,
  borderRadius: 8,
  padding: '10px 12px',
  outline: 'none',
  transition: 'border-color 0.15s ease',
  boxSizing: 'border-box',
};

export const ManualEntryModal = ({
  isOpen,
  onClose,
  manualEntry,
  setManualEntry,
  onAddEntry,
  orderOptions = ["포유류", "조류", "어류", "양서파충류", "저서무척추"],
}) => {
  if (!isOpen) return null;

  const handleFocus = (e) => { e.target.style.borderColor = '#3b82f6'; };
  const handleBlur  = (e) => { e.target.style.borderColor = '#1e3a5f'; };

  return (
    <div className="fixed inset-0 flex items-center justify-center z-[9999] p-4" style={{
      background: 'rgba(8,14,26,0.80)',
      backdropFilter: 'blur(8px)',
    }}>
      <div className="w-full max-w-md overflow-hidden rounded-2xl" style={{
        background: '#0f1c32',
        border: '1px solid #1e3a5f',
        boxShadow: '0 32px 80px rgba(0,0,0,0.7)',
      }}>
        {/* Header */}
        <div className="px-6 py-4 flex justify-between items-center" style={{
          background: '#162440',
          borderBottom: '1px solid #1e3a5f',
        }}>
          <h3 className="text-sm font-bold text-opencode-light flex items-center gap-2">
            <span style={{ width: 8, height: 8, borderRadius: 9999, background: '#3b82f6', boxShadow: '0 0 8px rgba(59,130,246,0.5)', display: 'inline-block' }} />
            생태 수동 조사 기록 등록
          </h3>
          <button
            onClick={onClose}
            className="p-1.5 rounded-lg text-opencode-midGray hover:text-opencode-light transition-colors"
            style={{ background: 'rgba(255,255,255,0.05)' }}
          >
            <X size={14} />
          </button>
        </div>

        {/* Form */}
        <div className="p-6 space-y-4">
          <div>
            <label className="block text-xs font-semibold text-opencode-midGray uppercase tracking-wider mb-2">
              분류 분류군
            </label>
            <select
              value={manualEntry.order}
              onChange={(e) => setManualEntry(prev => ({ ...prev, order: e.target.value }))}
              style={inputStyle}
              onFocus={handleFocus}
              onBlur={handleBlur}
            >
              {orderOptions.map(opt => <option key={opt} value={opt} style={{ background: '#162440' }}>{opt}</option>)}
            </select>
          </div>

          <div>
            <label className="block text-xs font-semibold text-opencode-midGray uppercase tracking-wider mb-2">
              국명 (종 이름)
            </label>
            <input
              type="text"
              placeholder="예: 삵, 수달, 멧돼지 등"
              value={manualEntry.species}
              onChange={(e) => setManualEntry(prev => ({ ...prev, species: e.target.value }))}
              style={{ ...inputStyle, '::placeholder': { color: '#64748b' } }}
              onFocus={handleFocus}
              onBlur={handleBlur}
            />
          </div>

          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="block text-xs font-semibold text-opencode-midGray uppercase tracking-wider mb-2">
                개체수
              </label>
              <input
                type="number"
                min="1"
                value={manualEntry.count}
                onChange={(e) => setManualEntry(prev => ({ ...prev, count: parseInt(e.target.value) || 1 }))}
                style={inputStyle}
                onFocus={handleFocus}
                onBlur={handleBlur}
              />
            </div>
            <div>
              <label className="block text-xs font-semibold text-opencode-midGray uppercase tracking-wider mb-2">
                관찰 유형
              </label>
              <select
                value={manualEntry.traces}
                onChange={(e) => setManualEntry(prev => ({ ...prev, traces: e.target.value }))}
                style={inputStyle}
                onFocus={handleFocus}
                onBlur={handleBlur}
              >
                <option value="V" style={{ background: '#162440' }}>생체 실물 목격 (V)</option>
                <option value="D" style={{ background: '#162440' }}>사체 흔적 (D)</option>
                <option value="F" style={{ background: '#162440' }}>분변/배설물 (F)</option>
                <option value="S" style={{ background: '#162440' }}>서식지/둥지/굴 (S)</option>
                <option value="T" style={{ background: '#162440' }}>발자국/보행 (T)</option>
              </select>
            </div>
          </div>
        </div>

        {/* Footer */}
        <div className="px-6 py-4 flex justify-end gap-2" style={{
          background: '#162440',
          borderTop: '1px solid #1e3a5f',
        }}>
          <button
            onClick={onClose}
            className="px-4 py-2 rounded-lg text-sm font-semibold text-opencode-midGray hover:text-opencode-light transition-colors"
            style={{ background: '#0f1c32', border: '1px solid #1e3a5f' }}
          >
            취소
          </button>
          <button
            onClick={onAddEntry}
            className="px-5 py-2 rounded-lg text-sm font-semibold text-white transition-all"
            style={{
              background: 'linear-gradient(135deg, #1d4ed8 0%, #3b82f6 100%)',
              boxShadow: '0 0 16px rgba(59,130,246,0.25)',
            }}
            onMouseEnter={e => e.currentTarget.style.boxShadow = '0 0 20px rgba(59,130,246,0.4)'}
            onMouseLeave={e => e.currentTarget.style.boxShadow = '0 0 16px rgba(59,130,246,0.25)'}
          >
            조사항목 추가
          </button>
        </div>
      </div>
    </div>
  );
};
