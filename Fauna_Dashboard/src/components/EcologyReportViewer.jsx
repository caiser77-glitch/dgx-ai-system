import React from 'react';
import { twMerge } from 'tailwind-merge';
import { clsx } from 'clsx';

function cn(...inputs) {
  return twMerge(clsx(inputs));
}

export const EcologyReportViewer = ({ markdownText, isPrintView = false }) => {
  if (!markdownText) return null;

  const parseMarkdown = (text) => {
    const lines = text.split('\n');
    const elements = [];
    let inTable = false;
    let tableHeaders = [];
    let tableRows = [];
    let currentClass = ""; // 포유류, 조류, 어류, 양서파충류, 저서무척추 등 추적

    const getPastelStyles = (cls) => {
      switch (cls) {
        case "포유류":
          return {
            printBg: "print-bg-mammals",
            border: "border-[#30d158]/30",
            headerBg: "bg-[#30d158]/10 text-[#30d158]",
            rowBg: "hover:bg-[#30d158]/5",
            rowOdd: "bg-[#30d158]/5",
            rowEven: "bg-[#30d158]/10",
            text: "text-[#30d158]",
            badge: "bg-[#30d158]/10 text-[#30d158] border border-[#30d158]/20"
          };
        case "조류":
          return {
            printBg: "print-bg-birds",
            border: "border-[#007aff]/30",
            headerBg: "bg-[#007aff]/10 text-[#007aff]",
            rowBg: "hover:bg-[#007aff]/5",
            rowOdd: "bg-[#007aff]/5",
            rowEven: "bg-[#007aff]/10",
            text: "text-[#007aff]",
            badge: "bg-[#007aff]/10 text-[#007aff] border border-[#007aff]/20"
          };
        case "어류":
          return {
            printBg: "print-bg-fish",
            border: "border-[#ff9f0a]/30",
            headerBg: "bg-[#ff9f0a]/10 text-[#ff9f0a]",
            rowBg: "hover:bg-[#ff9f0a]/5",
            rowOdd: "bg-[#ff9f0a]/5",
            rowEven: "bg-[#ff9f0a]/10",
            text: "text-[#ff9f0a]",
            badge: "bg-[#ff9f0a]/10 text-[#ff9f0a] border border-[#ff9f0a]/20"
          };
        case "양서파충류":
          return {
            printBg: "print-bg-reptiles",
            border: "border-[#af52de]/30",
            headerBg: "bg-[#af52de]/10 text-[#af52de]",
            rowBg: "hover:bg-[#af52de]/5",
            rowOdd: "bg-[#af52de]/5",
            rowEven: "bg-[#af52de]/10",
            text: "text-[#af52de]",
            badge: "bg-[#af52de]/10 text-[#af52de] border border-[#af52de]/20"
          };
        case "저서무척추":
          return {
            printBg: "print-bg-benthos",
            border: "border-[#55bef9]/30",
            headerBg: "bg-[#55bef9]/10 text-[#55bef9]",
            rowBg: "hover:bg-[#55bef9]/5",
            rowOdd: "bg-[#55bef9]/5",
            rowEven: "bg-[#55bef9]/10",
            text: "text-[#55bef9]",
            badge: "bg-[#55bef9]/10 text-[#55bef9] border border-[#55bef9]/20"
          };
        default:
          return {
            printBg: "print-bg-stats",
            border: "border-opencode-borderWarm",
            headerBg: "bg-opencode-darkSurface text-opencode-light",
            rowBg: "hover:bg-opencode-dark/10",
            rowOdd: "bg-opencode-dark/5",
            rowEven: "bg-opencode-dark/10",
            text: "text-opencode-light",
            badge: "bg-opencode-darkSurface text-opencode-light border border-opencode-borderWarm"
          };
      }
    };

    const flushTable = (key) => {
      if (tableRows.length > 0 || tableHeaders.length > 0) {
        const style = getPastelStyles(currentClass);

        elements.push(
          <div key={`table-${key}`} className={cn(
            "overflow-x-auto my-4 border rounded-[4px] print-border shadow-none",
            isPrintView
              ? "bg-white border-slate-400 my-6"
              : `bg-opencode-dark border-opencode-borderWarm`
          )}>
            <table className={cn("w-full text-xs text-left print-text-dark", isPrintView ? "text-black font-normal" : "text-opencode-light")}>
              <thead className={cn(
                "text-[10px] uppercase font-bold print-border border-b tracking-wider",
                isPrintView
                  ? "bg-slate-100 text-black border-slate-400"
                  : `${style.headerBg} ${style.printBg} border-opencode-borderWarm`
              )}>
                <tr>
                  {tableHeaders.map((h, i) => (
                    <th key={i} className={cn(
                      "text-center border-r font-bold",
                      isPrintView ? "border-slate-400 text-black px-3 py-2 bg-slate-100" : "px-4 py-3 border-opencode-borderWarm/50 print-text-dark"
                    )}>{h.trim()}</th>
                  ))}
                </tr>
              </thead>
              <tbody className={cn("divide-y print-border", isPrintView ? "divide-slate-400" : "divide-opencode-borderWarm/40")}>
                {tableRows.map((row, rowIndex) => (
                  <tr key={rowIndex} className={cn(
                    "transition-colors duration-150",
                    isPrintView
                      ? "bg-white hover:bg-slate-50"
                      : `${rowIndex % 2 === 0 ? style.rowOdd : style.rowEven} ${style.rowBg}`
                  )}>
                    {row.map((cell, cellIndex) => {
                      const cleanCell = cell.trim();
                      const isEndangered = cleanCell.includes('멸종위기') || cleanCell.includes('천연기념물');

                      return (
                        <td
                          key={cellIndex}
                          className={cn(
                            "border-r text-center",
                            isPrintView
                              ? "border-slate-400 text-black text-[11px] px-3 py-2 font-medium"
                              : cn("px-4 py-2.5 border-opencode-borderWarm/50 print-text-dark font-mono text-opencode-light", isEndangered ? "text-[#ff3b30] font-bold bg-[#ff3b30]/5 print-bg-stats" : "text-opencode-light/80"),
                            cleanCell === "-" ? (isPrintView ? "text-slate-400 font-normal" : "text-opencode-midGray font-normal") : ""
                          )}
                        >
                          {isEndangered && !isPrintView ? (
                            <span className="inline-block px-2.5 py-0.5 bg-[#ff3b30]/10 text-[#ff3b30] rounded-[4px] text-[10px] font-bold border border-[#ff3b30]/20 print-text-dark">
                              {cleanCell}
                            </span>
                          ) : cleanCell}
                        </td>
                      );
                    })}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        );
        tableHeaders = [];
        tableRows = [];
        inTable = false;
      }
    };

    let keyCounter = 0;
    for (let i = 0; i < lines.length; i++) {
      const line = lines[i].trim();
      keyCounter++;

      // 테이블 감지
      if (line.startsWith('|')) {
        const cells = line.split('|').map(c => c.trim()).filter((c, idx, arr) => idx > 0 && idx < arr.length - 1);
        if (cells.every(c => c.startsWith(':') || c.startsWith('-') || c === '')) {
          continue;
        }
        if (!inTable) {
          inTable = true;
          tableHeaders = cells;
        } else {
          tableRows.push(cells);
        }
        continue;
      } else {
        if (inTable) {
          flushTable(keyCounter);
        }
      }

      // 대시보드 타이틀 감지: === Title ===
      if (line.startsWith('===') && line.endsWith('===')) {
        const titleText = line.replace(/===/g, '').trim();
        elements.push(
          <div key={keyCounter} className={cn(
            "text-center py-3 mb-4 border-b print-border",
            isPrintView ? "border-black" : "border-opencode-borderWarm"
          )}>
            <h1 className={cn(
              "font-mono tracking-tight font-bold",
              isPrintView ? "text-black text-[22px] font-black" : "text-opencode-light text-xl"
            )}>{titleText}</h1>
          </div>
        );
        continue;
      }

      // 소제목 감지: [조사 개요] or [포유류 관찰 일람표]
      if (line.startsWith('[') && line.endsWith(']')) {
        const headerText = line.replace(/\[|\]/g, '').trim();

        // 현재 표를 그릴 대상 분류군 클래스명 변경
        if (headerText.includes("포유류")) currentClass = "포유류";
        else if (headerText.includes("조류")) currentClass = "조류";
        else if (headerText.includes("어류")) currentClass = "어류";
        else if (headerText.includes("양서파충류")) currentClass = "양서파충류";
        else if (headerText.includes("저서무척추")) currentClass = "저서무척추";
        else currentClass = "";

        const style = getPastelStyles(currentClass);

        elements.push(
          <h2 key={keyCounter} className={cn(
            "font-mono mt-5 mb-2.5 pb-1 border-b flex items-center gap-2 print-border font-bold",
            isPrintView
              ? "text-black text-[15px] border-black"
              : cn("text-opencode-light text-sm border-opencode-borderWarm", style.text)
          )}>
            {!isPrintView && (
              <span className={cn("w-2 h-2 rounded-[1px] inline-block", currentClass ? "bg-opencode-successGreen" : "bg-opencode-accentBlue")}></span>
            )}
            {headerText}
          </h2>
        );
        continue;
      }

      // 일반 텍스트 라인
      if (line !== '') {
        elements.push(
          <p key={keyCounter} className={cn(
            "leading-relaxed my-1.5 select-text font-mono",
            isPrintView
              ? "text-[12px] text-slate-800 font-normal"
              : "text-xs text-opencode-light/80 font-normal"
          )} dangerouslySetInnerHTML={{ __html: line }} />
        );
      }
    }

    flushTable(keyCounter + 1);
    return elements;
  };

  return (
    <div className={cn(
      "space-y-3 pb-8 select-text font-mono",
      isPrintView ? "print-report-container text-black" : "text-opencode-light/80 leading-relaxed"
    )}>
      {/* 종이 인쇄 강제 백업 스타일 이식 */}
      <style>{`
        @media print {
          body * {
            visibility: hidden !important;
          }
          .print-report-container, .print-report-container * {
            visibility: visible !important;
            color: #000000 !important;
          }
          .print-report-container {
            position: absolute !important;
            left: 0 !important;
            top: 0 !important;
            width: 100% !important;
            background: #ffffff !important;
            color: #000000 !important;
            padding: 20px !important;
            box-shadow: none !important;
            border: none !important;
          }
          .print-border {
            border: 1px solid #000000 !important;
            border-collapse: collapse !important;
          }
          .print-text-dark {
            color: #000000 !important;
          }
        }
      `}</style>
      {parseMarkdown(markdownText)}
    </div>
  );
};
