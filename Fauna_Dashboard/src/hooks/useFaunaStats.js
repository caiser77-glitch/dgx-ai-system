import { useMemo } from 'react';

export const useFaunaStats = (surveyData, activeSurvey, isCumulative, selectedCategory, speciesIndex, selectedSite = '전체') => {
  return useMemo(() => {
    // ── 1. 조사차수 필터 (누적/독립 공통) ──────────────────────────────
    const byRound = isCumulative
      ? surveyData.filter(d => d.surveyId <= activeSurvey)
      : surveyData.filter(d => d.surveyId === activeSurvey);

    // ── 2. 조사지점 필터 (누적/독립 모드 동일하게 적용) ─────────────────
    //   독립: 선택한 지점만
    //   누적: 선택한 지점 번호 이하 전체 (St. 1 선택 시 St. 1만, St. 3 선택 시 St. 1~3)
    let bySite;
    if (selectedSite === '전체') {
      bySite = byRound;
    } else {
      const selNum = parseInt(selectedSite.replace('St.', '').trim(), 10);
      bySite = isCumulative
        ? byRound.filter(d => {
            const n = parseInt((d.site || '').replace('St.', '').trim(), 10);
            return !isNaN(n) && n <= selNum;
          })
        : byRound.filter(d => d.site === selectedSite);
    }

    // ── 3. 분류명 정규화 ──────────────────────────────────────────────
    const classMap = {
      "Mammalia": "포유류", "포유류": "포유류",
      "Aves": "조류", "조류": "조류",
      "Amphibia": "양서류", "양서류": "양서류",
      "Reptilia": "파충류", "파충류": "파충류",
      "Pisces": "어류", "Actinopterygii": "어류", "Chondrichthyes": "어류", "어류": "어류",
      "Insecta": "저서무척추", "Gastropoda": "저서무척추", "Bivalvia": "저서무척추",
      "Malacostraca": "저서무척추", "Clitellata": "저서무척추", "Polychaeta": "저서무척추",
      "Hexanauplia": "저서무척추", "Ostracoda": "저서무척추", "Branchiopoda": "저서무척추",
      "곤충류": "저서무척추", "저서무척추": "저서무척추",
      "무척추동물류(곤충류 제외)": "저서무척추",
    };

    const filteredRaw = bySite
      .map(d => {
        const masterInfo = speciesIndex[d.species] || {};
        const rawClass   = d.class || masterInfo.Class || '미분류';
        let finalOrder   = d.order || masterInfo.Order || '';
        if (finalOrder === '우경목') finalOrder = '우제목';
        return {
          ...d,
          scientificName: d.scientificName || masterInfo.Scientific_Name || '',
          class: classMap[rawClass] || rawClass,
          order: finalOrder,
        };
      })
      .filter(d => {
        if (selectedCategory === '전체') return true;
        const g = d.class || '';
        if (selectedCategory === '양서파충류') return g === '양서류' || g === '파충류' || g === '양서파충류';
        return g === selectedCategory;
      });

    // ── 4. 종별 개체수 합산 ──────────────────────────────────────────
    const speciesMap = filteredRaw.reduce((acc, curr) => {
      const key = curr.species || 'Unknown';
      if (!acc[key]) acc[key] = { ...curr, totalCount: 0 };
      acc[key].totalCount += (curr.count || 0);
      return acc;
    }, {});

    const displayData = Object.values(speciesMap).sort((a, b) => b.totalCount - a.totalCount);

    // ── 5. 생태 지수 산출 ────────────────────────────────────────────
    const N = filteredRaw.reduce((sum, d) => sum + (d.count || 0), 0);
    const S = Object.keys(speciesMap).length;
    let hPrime = 0;
    if (N > 0) {
      Object.values(speciesMap).forEach(sp => {
        const pi = sp.totalCount / N;
        if (pi > 0) hPrime -= pi * Math.log(pi);
      });
    }
    const evenness = S > 1 ? hPrime / Math.log(S) : 0;

    // ── 6. 분류군별 집계 ─────────────────────────────────────────────
    const taxonomicGroups = filteredRaw.reduce((acc, curr) => {
      const group = curr.class || '미분류';
      if (!acc[group]) acc[group] = {
        name: group, items: [], totalAbundance: 0,
        orders: new Set(), families: new Set(), species: new Set(),
      };
      acc[group].items.push(curr);
      acc[group].totalAbundance += (curr.count || 0);
      if (curr.order)   acc[group].orders.add(curr.order);
      if (curr.family)  acc[group].families.add(curr.family);
      if (curr.species) acc[group].species.add(curr.species);
      return acc;
    }, {});

    const groupStats = Object.values(taxonomicGroups).map(g => ({
      name: g.name, abundance: g.totalAbundance,
      orders: g.orders.size, families: g.families.size, species: g.species.size,
    }));

    const taxonomicGroupsFormatted = {};
    Object.entries(taxonomicGroups).forEach(([name, g]) => {
      taxonomicGroupsFormatted[name] = {
        ...g,
        orderCount:   g.orders.size,
        familyCount:  g.families.size,
        speciesCount: g.species.size,
      };
    });

    const topSpeciesPerTaxon = Object.values(taxonomicGroups).map(g => {
      const spMap = g.items.reduce((acc, curr) => {
        const sp = curr.species;
        if (!acc[sp]) acc[sp] = { species: sp, totalCount: 0, taxon: g.name };
        acc[sp].totalCount += (curr.count || 0);
        return acc;
      }, {});
      return Object.values(spMap).sort((a, b) => b.totalCount - a.totalCount)[0];
    }).filter(Boolean);

    return {
      filteredRaw, displayData,
      totalAbundance: N, richness: S,
      shannonIndex:    Number(hPrime).toFixed(4),
      pielouEvenness:  Number(evenness).toFixed(4),
      groupStats, taxonomicGroups: taxonomicGroupsFormatted, topSpeciesPerTaxon,
    };
  }, [surveyData, activeSurvey, isCumulative, selectedCategory, speciesIndex, selectedSite]);
};
