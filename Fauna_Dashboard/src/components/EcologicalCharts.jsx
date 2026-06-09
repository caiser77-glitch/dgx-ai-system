import React from 'react';
import {
  ResponsiveContainer, BarChart, CartesianGrid, XAxis, YAxis,
  Tooltip, Bar, Cell, PieChart, Pie, Legend
} from 'recharts';
import { TrendingUp, PieChart as PieChartIcon } from 'lucide-react';

const CHART_COLORS = ['#3b82f6', '#34d399', '#fbbf24', '#f87171', '#a78bfa'];

const tooltipStyle = {
  backgroundColor: '#162440',
  border: '1px solid #1e3a5f',
  borderRadius: 10,
  boxShadow: '0 8px 24px rgba(0,0,0,0.5)',
};
const tooltipLabelStyle = { color: '#94a3b8', fontWeight: 700, fontSize: 11 };
const tooltipItemStyle = { color: '#e2e8f0', fontWeight: 600, fontSize: 12 };

export default function EcologicalCharts({ stats }) {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
      {/* 분류군별 최우점 대표종 바차트 */}
      <div className="rounded-xl p-6" style={{
        background: '#0f1c32',
        border: '1px solid #1e3a5f',
        boxShadow: '0 4px 20px rgba(0,0,0,0.4)',
      }}>
        <h3 className="text-sm font-bold flex items-center gap-2 text-opencode-light mb-5">
          <span className="p-1.5 rounded-md" style={{ background: 'rgba(59,130,246,0.15)' }}>
            <TrendingUp size={14} className="text-opencode-accentBlue" />
          </span>
          분류군별 최우점 대표종
        </h3>
        <div style={{ height: 240, width: '100%', minWidth: 0 }}>
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={stats.topSpeciesPerTaxon} barCategoryGap="30%">
              <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="rgba(30,58,95,0.6)" />
              <XAxis
                dataKey="species"
                tick={{ fill: '#64748b', fontSize: 10, fontFamily: 'Inter, system-ui, sans-serif' }}
                axisLine={false}
                tickLine={false}
              />
              <YAxis
                axisLine={false}
                tickLine={false}
                tick={{ fill: '#64748b', fontSize: 10, fontFamily: 'Inter, system-ui, sans-serif' }}
              />
              <Tooltip
                cursor={{ fill: 'rgba(59,130,246,0.06)', radius: 4 }}
                contentStyle={tooltipStyle}
                labelStyle={tooltipLabelStyle}
                itemStyle={tooltipItemStyle}
                formatter={(value, name, props) => [`${value} 개체`, `분류군: ${props.payload.taxon}`]}
              />
              <Bar dataKey="totalCount" name="대표종 개체수" radius={[6, 6, 0, 0]}>
                {stats.topSpeciesPerTaxon.map((_, i) => (
                  <Cell key={i} fill={CHART_COLORS[i % CHART_COLORS.length]} fillOpacity={0.9} />
                ))}
              </Bar>
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>

      {/* 분류군별 구성 비율 파이차트 */}
      <div className="rounded-xl p-6" style={{
        background: '#0f1c32',
        border: '1px solid #1e3a5f',
        boxShadow: '0 4px 20px rgba(0,0,0,0.4)',
      }}>
        <h3 className="text-sm font-bold flex items-center gap-2 text-opencode-light mb-5">
          <span className="p-1.5 rounded-md" style={{ background: 'rgba(52,211,153,0.15)' }}>
            <PieChartIcon size={14} className="text-opencode-successGreen" />
          </span>
          분류군별 구성 비율
        </h3>
        <div style={{ height: 240, width: '100%', minWidth: 0 }}>
          <ResponsiveContainer width="100%" height="100%">
            <PieChart>
              <Pie
                data={Object.values(stats.taxonomicGroups || {}).map(g => ({ name: g.name, value: g.speciesCount }))}
                innerRadius={55}
                outerRadius={80}
                paddingAngle={4}
                dataKey="value"
                strokeWidth={0}
              >
                {Object.values(stats.taxonomicGroups || {}).map((_, i) => (
                  <Cell key={i} fill={CHART_COLORS[i % CHART_COLORS.length]} fillOpacity={0.9} />
                ))}
              </Pie>
              <Tooltip
                contentStyle={tooltipStyle}
                itemStyle={tooltipItemStyle}
              />
              <Legend
                verticalAlign="bottom"
                height={36}
                iconType="circle"
                iconSize={8}
                wrapperStyle={{
                  fontFamily: 'Inter, system-ui, sans-serif',
                  fontSize: 11,
                  color: '#94a3b8',
                }}
              />
            </PieChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );
}
