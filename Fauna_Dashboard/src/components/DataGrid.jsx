import React from 'react';
import { ShieldAlert } from 'lucide-react';

const GROUP_COLORS = ['#3b82f6', '#34d399', '#fbbf24', '#f87171', '#a78bfa'];

export default function DataGrid({ stats }) {
  const groups = Object.entries(stats.taxonomicGroups || {});

  return (
    <div className="space-y-5">
      {groups.map(([groupName, groupData], gIdx) => {
        const accent = GROUP_COLORS[gIdx % GROUP_COLORS.length];
        return (
          <div key={groupName} className="rounded-xl overflow-hidden" style={{
            background: '#0f1c32',
            border: `1px solid ${accent}20`,
            boxShadow: '0 4px 20px rgba(0,0,0,0.35)',
          }}>
            {/* Group Header */}
            <div className="px-5 py-3.5 flex justify-between items-center" style={{
              background: '#162440',
              borderBottom: `1px solid ${accent}20`,
            }}>
              <h3 className="text-sm font-bold text-opencode-light flex items-center gap-2.5">
                <span style={{
                  width: 3, height: 16,
                  background: accent,
                  borderRadius: 9999,
                  display: 'inline-block',
                  boxShadow: `0 0 8px ${accent}60`,
                }} />
                {groupName} 현황
              </h3>
              <div className="flex items-center gap-2 text-[11px] font-semibold px-3 py-1 rounded-full" style={{
                background: `${accent}15`,
                color: accent,
                border: `1px solid ${accent}25`,
              }}>
                <span>{groupData.orderCount || 0} 목</span>
                <span className="opacity-40">·</span>
                <span>{groupData.familyCount || 0} 과</span>
                <span className="opacity-40">·</span>
                <span>{groupData.speciesCount || 0} 종</span>
              </div>
            </div>

            {/* Table */}
            <div className="overflow-x-auto">
              <table className="w-full text-left">
                <thead>
                  <tr style={{ borderBottom: '1px solid #1e3a5f' }}>
                    {['목 (Order)', '과 (Family)', '학명 (Scientific Name)', '국명 (Species)', '차수', '개체수/흔적', '보호 등급'].map((h, i) => (
                      <th key={h} className="px-4 py-3 text-[10px] font-bold uppercase tracking-wider text-opencode-midGray"
                        style={{ textAlign: i >= 5 ? 'center' : i === 6 ? 'right' : 'left', whiteSpace: 'nowrap' }}
                      >
                        {h}
                      </th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {groupData.items.map((row, idx) => (
                    <tr
                      key={row.id || `${row.species}-${idx}`}
                      className="transition-colors duration-100"
                      style={{
                        borderBottom: idx < groupData.items.length - 1 ? '1px solid rgba(30,58,95,0.5)' : 'none',
                        background: idx % 2 === 1 ? 'rgba(22,36,64,0.4)' : 'transparent',
                      }}
                      onMouseEnter={e => e.currentTarget.style.background = 'rgba(59,130,246,0.06)'}
                      onMouseLeave={e => e.currentTarget.style.background = idx % 2 === 1 ? 'rgba(22,36,64,0.4)' : 'transparent'}
                    >
                      <td className="px-4 py-3 text-sm text-opencode-light font-semibold whitespace-nowrap">{row.order}</td>
                      <td className="px-4 py-3 text-xs text-opencode-midGray whitespace-nowrap">{row.family}</td>
                      <td className="px-4 py-3 italic text-opencode-midGray font-mono text-xs leading-tight max-w-[180px] truncate">
                        {row.scientificName || "—"}
                      </td>
                      <td className="px-4 py-3">
                        <div className="flex items-center gap-2">
                          <span
                            className="w-1.5 h-1.5 rounded-full flex-shrink-0"
                            style={{
                              background: row.protected ? '#fbbf24' : '#1e3a5f',
                              boxShadow: row.protected ? '0 0 6px rgba(251,191,36,0.5)' : 'none',
                            }}
                          />
                          <span className="text-sm font-semibold text-opencode-light whitespace-nowrap">{row.species}</span>
                        </div>
                      </td>
                      <td className="px-4 py-3 text-center text-xs text-opencode-midGray font-semibold">{row.surveyId}차</td>
                      <td className="px-4 py-3">
                        <div className="flex items-center justify-center gap-1.5">
                          <span className="font-mono font-bold text-sm text-opencode-accentBlue">{row.count}</span>
                          <span className="px-1.5 py-0.5 rounded font-mono text-[9px] font-bold uppercase" style={{
                            background: '#162440',
                            border: '1px solid #1e3a5f',
                            color: '#94a3b8',
                          }}>
                            {row.traces}
                          </span>
                        </div>
                      </td>
                      <td className="px-4 py-3 text-right">
                        {row.protected && (
                          <div className="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-semibold" style={{
                            background: 'rgba(248,113,113,0.12)',
                            border: '1px solid rgba(248,113,113,0.25)',
                            color: '#f87171',
                            whiteSpace: 'nowrap',
                          }}>
                            <ShieldAlert size={9} />
                            {row.protected}
                          </div>
                        )}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>

            {/* Footer */}
            <div className="px-5 py-2.5 text-center text-[10px] font-semibold text-opencode-midGray" style={{
              borderTop: '1px solid rgba(30,58,95,0.5)',
              background: '#162440',
            }}>
              {groupName} · 총 {groupData.totalAbundance} 개체 관찰
            </div>
          </div>
        );
      })}
    </div>
  );
}
