--- 
source: GIS와 Weight of Evidence를 이용한 산산태 취약성 분석 및 검증_오현주.pdf
--- 

지질학회지 제46권 제2호, p. 157-170, (2010년 4월)
1. 서 론
지공간상에서 발생하는 지질재해는 국민생활 안
전에 큰 위험요소로 작용하고, 재산 손실을 유발하
는 등 국가적인 문제로 부각되고 있다. 따라서 지질
재해를 완화하고 예방하기 위하여 지공간상에서 발
생하는 재해의 원인과 패턴을 탐지하고 그 밖의 불
확실한 지질현상에 대한 예측 연구가 필요하다. 그
러나 지질현상과 연관된 실세계 지공간 자료는 첨단
기술과 장비의 개발로 인하여 점점 더 방대해져가고 
복잡해지고 있다. 그러므로 자료의 홍수 속에서 지
질현상과 관련된 정보를 효과적으로 찾고, 지공간 
요소들과의 복합적인 상관관계를 파악하기 위해 지
리정보시스템(GIS)이 필요하다. 과거의 GIS는 단순
GIS와 Weight of Evidence를 이용한 산사태 취약성 분석 및 검증
오현주
한국지질자원연구원 지질정보연구실
요  약
 
본 연구는 Weight-of-Evidence (WOE) 기법과 GIS를 이용한 진부면 지역의 산사태 취약성을 평가하는데 있다. 
연구지역의 산사태 위치는 산사태 발생 전후의 항공사진을 판독 후 현장에서 재확인되었다. 지형, 지질, 토양, 임상, 
토지이용 등의 자료는 GIS 기반의 공간데이터베이스로 구축하였고, 산사태와 관련있는 요인으로는 경사, 경사면, 
곡률, 임상, 경급, 영급, 밀도, 지형, 유효토심, 모재, 토질, 지질, 선구조밀도, 토지이용 등을 선정하였다. 연구지역의 
산사태 개수는 취약성 분석 및 검증을 위해 70:30 비율로 랜덤 분류하였다. 산사태 취약성도는 WOE의 W+와 W-가 
부여된 각 요인들의 중첩분석을 통하여 작성되었고, 요인별 독립성 검증 후 경사, 경사면, 곡률, 선구조밀도, 토지이용, 
임상, 영급, 모재 등의 조합이 가장 높은 72.90%의 예측 정확도를 보였다. 이 결과는 산사태로 인한 피해예방과 토지이
용 계획에 중요한 자료로 사용될 수 있을 것이다.
주요어: GIS, Weight-of-Evidence, 산사태 취약성, 진부
Hyun-Joo Oh, 2010, Landslide susceptibility analysis and validation using Weight-of-Evidence model. 
Journal of the Geological Society of Korea. v. 46, no. 2, p. 157-170
ABSTRACT: The aim of this study is to evaluate the landslide susceptibility at Jinbu area in Korea, using 
Weight-of-Evidence(WOE) and Geographic Information System(GIS). Landslide locations of the study area were 
identified from the before and after aerial photographs of landslide occurrence, and field survey. Topographic maps, 
geological data, soil data, timber data, and land use data were collected, processed, and constructed into a spatial 
database in a GIS platform. The factors chosen that influence landslide were: slope, aspect, curvature, timber type, 
timber diameter, timber age, timer density, topography, soil thickness, soil material, soil texture, geology, lineament 
and land use. The known landslides were randomly split 70/30 for training/testing, which used for analyzing and 
validating landslide susceptibility map using WOE. For each factor rating, W+ and W- were overlaid for landslide 
susceptibility mapping. After tests of conditional independence, the combination including slope, aspect, curvature, 
density of lineament, land use, timber typ, timber age and soil material factors showed the best result. The result 
can be used to prevent damage associated with landslides and to perform a proper land use planning.
Key words: GIS, Weight-of-Evidence, Landslide susceptibility, Jinbu
(Hyun-Joo Oh, Geoscience Information Department, Korea Institute of Geoscience and Mineral Resources 
92 Gwahang-no, Yuseong-gu, Daejeon 305-350, Korea)
 
                 
‡Corresponding author: +82-42-868-3738, E-mail: ohj@kigam.re.kr


158
오현주
히 지도제작의 성격이 강하였으나, IT기술이 발달되
면서 GIS 활용분야와 개념이 변화되기 시작하였다. 
최근 GIS는 지리정보 구축, 유지관리, 출력 등과 같
은 다양한 기능을 제공하기 때문에 지공간과 관련된 
지질, 환경, 생태분야에서 그 활용도가 매우 높다
(Koret, 1997). 하지만 GIS는 공간자료들의 연관성 
예측에 다소 제한된 부분이 있기에 이에 대한 보완
으로 확률, 통계, 데이터 마이닝 기법을 같이 사용하
고 있다.
최근 지구온난화 및 이상고온의 증가추세로 태풍 
및 집중호우가 빈발화되면서 산사태 발생 빈도도 같
이 증가하고 있다. 우리나라 역시 1998년 태풍 예니, 
2002년 태풍 루사, 2003년 태풍 매미의 영향으로 산
사태와 산림피해가 급격히 늘었으며 특히 2006년도
에는 연속적인 태풍 에위니아, 빌리스, 개미로 인하
여 많은 산사태가 발생하였고, 이로 인한 피해지역
들은 특별재난 지역으로 선포되었다. 그러므로 산사
태로 인한 인재, 재산, 시설물 등의 피해를 예방하기 
위해 정량적인 산사태 취약성 평가가 수행될 필요가 
있다.
이에 따라 GIS 및 확률, 통계, 인공신경망 기법으
로 국내외 지역의 산사태 취약성 분석은 많이 수행
되어왔다(Lee and Min, 2001; Lee et al., 2003a, 2003b). 
확률기반의 Weight of Evidence 기법은 자료유도
형 방법으로써 의학분야에서 처음 적용되어(Spiegelhater 
and Kill-Jones, 1984) 광상부존 유망지 분석(Bonham- 
Catter et al., 1989; Bonham-Catter, 1994), 산사태 취
약성도 분석(Lee et al., 2002; Lee and Choi, 2004)
에 적용되었다. WOE 방법은 입력자료를 W+와 W-
로 이분화시키기 때문에 사건의 수가 적을시 예측 
정확도가 떨어진다. 이러한 단점으로 기존의 연구에
서는 동일한 사건 자료를 분석과 검증에 함께 사용
하여왔다. 하지만 본 연구에서는 대국민에게 서비스 
되는 50 cm급의 해상도를 가지는 디지털 항공사진을 
이용함으로써 접근이 어려운 지역에서 발생한 산사
태와 규모가 작은 산사태까지 판독하였다. 그 결과 
많은 산사태 자료를 수집할 수 있었고, 수집된 1,803
개의 산사태를 70:30 비율로 랜덤 분류하여 각각 분
석 및 검증자료로 사용하였다. 
본 연구에서는 강원도 평창군 진부면 지역을 대
상으로 WOE 기법을 적용하여 산사태 취약성을 정
량적으로 분석하고, 분석에 사용하지 않은 산사태 
자료를 검증자료로 사용하여 취약성도의 예측 정확
도를 판단하고자 한다. 
2. 이론적 배경
WOE 기법은 기존의 산사태 위치와 지질 및 지형
정보 사이의 관계를 확률로 표현하는 자료유도형 방
법으로써 베이지안 확률을 기반으로 한다. 사건 발
생지역을 점으로 표시하고 그 사상을 D로 나타내면 
경우의 수는 N(D)로 나타낼 수 있으며(Bonham-Carter, 
1994), 표본공간 T에 대한 사전확률은 식 (1)과 같다. 
}
{
}
{
}
{
T
N
D
N
D
P
=
(1)
일정한 크기를 갖는 단위 픽셀들로 이루어진 연구지
역 주제별 요소를 사상 B로 나타내면, 사상 D와 사
상 B의 공통 사건의 경우의 수는 
로 나타
낼 수 있다. 사상 B가 발생하였을 때 사상 D가 발생
할 가능성을 베이지안 이론을 적용하여 나타내면 식 
(2)와 같다. 
(2)
P{B|D}는 사상 D가 발생하였을 때 사상 B가 발생
할 가능성을 나타낸 사후확률을 나타내고, P{B}는
사상 B가 발생할 가능성을 나타낸 사전확률을 나타
Fig. 1. Venn diagram to illustrate weights of evidence
calculations.


GIS와 Weight of Evidence를 이용한 산사태 취약성 분석 및 검증
159
낸다. 같은 경우로써 여사상 B 가 발생하였을 때 사
상 D가 발생할 가능성을 베이지안 이론을 적용하여 
나타내면 식 (3)과 같다.
(3)
 
식 (2)와 (3)을 odds로 표현하면 각각 식 (4), (5)와 
같다.
 
}
|
{
}
|
{
}
{
}
|
{
D
B
P
D
B
P
D
O
B
D
O
=
(4)
}
|
{
}
|
{
}
{
}
|
{
D
B
P
D
B
P
D
O
B
D
O
=
(5)
 
}
|
{
B
D
O
와 
}
|
{
B
D
O
는 Posterior odds를 나타내
며, 
}
{D
O
는 Prior odds를 말한다. 
 
식 (4)와 (5)의
}
|
{
}
|
{
D
B
P
D
B
P
,
}
|
{
}
|
{
D
B
P
D
B
P
은 각각
sufficiency ratio (LS), necessity ratio (LN)라고 하
며, 또한 LS와 LN은 우도비(likelihood ratios)라고 
한다. WOE는 LS와 LN에 자연로그를 취함으로써 
다음과 같이 정의 된다.
 
}
|
{
}
|
{
log
D
B
P
D
B
P
W
e
=
+
(6)
}
|
{
}
|
{
log
D
B
P
D
B
P
W
e
=
−
(7)
식 (6), (7)은 각각 positive weights of evidence, 
negative weights of evidence라고 한다. 
3. 연구지역
최근 세계적인 기후변동으로 인하여 우리나라에
는 국지성 호우와 장마가 증가하였고, 이로 인해 대
규모의 재해와 재난이 발생하였다. 2006년도에는 태
풍 에위니아, 빌리스 및 개미에 의한 영향으로 평년
보다 두 배 이상의 강우(758 mm)로 7월 한달간 전
국적으로 1조 천억원의 재산피해가 발생한 것으로 
파악되었다. 특히 2006년 전국 피해액의 95.4%를 차
지한 강원도는 약 2일간에 걸쳐 675 mm의 집중호
우가 내려 강원도 인제군 및 평창군을 중심으로 수
많은 산사태가 발생하였다. 또한 평창군은 3시간 연
속 최대 강우량이 209 mm로 500년에 한 번 있을 정
Fig. 2. DEM of study areas with landslide location.


160
오현주
도의 강우가 발생하였고, 본 연구에서는 산사태가 
가장 많이 발생한 진부면을 연구지역으로 선정하였
다. 연구지역은 지리좌표상으로 위도 37° 35' 2"~37° 
40' 26"N, 경도 128° 29' 49"~128° 35' 36"E 사이에 
위치하고, 지질도는 1:50,000 축척의 하진부 도폭에 
해당된다(그림 2).
4. 공간 데이터베이스 구축
지공간에서 발생하는 산사태는 여러 요인들의 복
합적인 상호작용에 의해 발생한다. 따라서 산사태 
취약성 분석을 위해 산사태와 관련있는 요인들을 
GIS 기반의 공간데이터베이스로 구축해야 한다. 진
부면 지역의 산사태 취약성 분석을 위해 수집된 자
료는 표 1과 같이 산사태 분포도, 지형도, 지질도, 토
지이용도, 임상도, 토양도이다. 산사태 발생 위치는 
산사태 발생 전후의 아날로그 항공사진과 디지털 항
공사진을 비교 후 현장조사를 통하여 확인하였다(그
림 3). 지형도에서는 경사, 경사면, 곡률 및 선구조밀
도를, 토양도에서는 지형, 모재, 유효토심 및 토질을, 
임상도에서는 경급, 임상, 밀도 및 영급을, 지질도에
서는 암상을 추출하였다. 산사태와 관련있는 모든 
요인들은 입력자료의 축척을 고려하여 10 m × 10 m 
격자로 설정하여 공간 데이터베이스로 구축하였다
(그림 4). 연구지역의 공간자료 구축은 ArcGIS 9.0
을 이용하였고, 격자수는 행과 열이 923 × 1,053으로 
총 597,884개로 설정하였다. 
4.1 산사태 위치 선정
2006년도에 발생한 연구지역의 산사태 위치는 산
사태 발생 전후의 항공사진을 비교·탐지하여 선정
하였고, 산사태 위치의 정확성을 판단하기 위하여 
현지답사를 실시하였다. 산사태 발생 전의 항공사진
은 국토지리정보원(National Geographic Information 
Institute, NGII)에서 발행하는 1:20,000 축척의 아
날로그 항공사진(촬영일 : 2005. 04. 04)을, 산사태 
발생 후의 항공사진은 Daum에서 제공하는 50 cm
급 디지털 항공사진(촬영일 : 2008. 03. 04)을 수집하
였다. 두 항공사진을 비교하여 파악된 산사태 위치
는 현장의 산사태 위치와 정확하게 일치하였다(그림 3). 
이러한 작업 절차를 통하여 총 1,803개의 산사태 위
치는 GPS 자료 및 1:5,000 수치지형도를 이용하여 
GIS 기반의 점 형태로 구축하였다(그림 2).
4.2 지형요인
자연사면의 형태는 지형에 의해 결정되고, 침식 
및 퇴적작용을 받는 지형은 토양의 물리화학적 특
성, 지표수, 지하수의 집중과 이동 등에 영향을 미치
므로 다양한 환경변수에 영향을 주는 중요한 요소이
다. 그러므로 지형의 요인들은 집중호우시 산사태 
발생에 영향을 준다(Johnes et al., 1983; Griffiths 
and Hearn, 1990). 산사태와 관련있는 지형 요인들
은 국토지리정보원 발행의 1:5,000 수치지형도를 이
용하여 작성한 수치표고모델 (DEM)로부터 경사도, 
경사면, 곡률을 추출하였다. 평균적으로 45도 이상
Table 1. Data layer related to landslide of study area.
Category
Factors
Data Type
Scale
Geological hazard map
Landslide
Point
1:5,000
Topographic map
Slope
Aspect
Curvature
Lineament
GRID
1:5,000
Forest map
Timber diameter
Timber type
Timber density
Timber age
Polygon
1:25,000
Soil map
Topography
Soil material
Soil thickness
Soil texture
Polygon
1:25,000
Geological map
Geology
Polygon
1:50,000
Land use map
Land use
Polygon
1:5,000


GIS와 Weight of Evidence를 이용한 산사태 취약성 분석 및 검증
161
의 사면의 경사(그림 4a)에서는 토층이 발달하지 않
으므로 토사 산사태 발생 가능성이 오히려 낮다. 경
사면은 방향(그림 4b)에 따라 지표의 함수량, 식생의 
종류 및 토양의 강도가 다를 수 있으므로 산사태에 
취약한 정도도 다를 수 있다. 사면의 곡률(그림 4c)
은 오목형, 평형, 볼록형 사면으로 구분할 수 있다. 
우기동안 오목한 사면은 볼록한 사면 혹은 평탄한 
사면보다 더 많은 수분을 함유할 수 있기 때문에 오
목형 사면이 산사태에 더 취약할 수 있다. 
4.3 임상도
식생은 사면위에 떨어지는 비의 충격을 완충하여 
사면위의 침식을 막으며, 식생의 뿌리는 토양의 전
단강도를 증가시켜 사면의 안정성을 높여준다. 그러
므로 식생의 유무는 산사태 발생에 중요한 요인이 
된다. 산사태와 관련있는 임상 요인들은 국립산림과
학원 발행의 4차 1:25,000 수치임상도로부터 임상, 
경급, 영급, 밀도를 추출하였다. 연구지역의 임상은 
소나무림(D), 활엽수혼효림(H), 경작지(L), 침활혼
Fig. 3. Selection of landslide occurrence: a) analog aerial photograph by NGII, b) digital aerial photograph by DAUM
and c) field survey photo.


162
오현주
(a)
(b)
(c)
(d)
(e)
(f)
(g)
(h)
(i)
(j)
(k)
(l)
(m)
(n)
Fig. 4. Constructed spatial database for landslide susceptibility analysis.


GIS와 Weight of Evidence를 이용한 산사태 취약성 분석 및 검증
163
효림(M), 소나무 공림(PD), 포루라림(PH), 잣나무
림(PK), 낙엽송림(PL), 포푸라림(Po), 제지(R)로 구
분되어 있다. 경급(그림 4e)은 항공사진 상에서 측정
한 수목의 수관직경(樹冠直徑)과 현지조사시 측정한 
수목의 가장 높은 부위직경과의 관계를 따져서 치
수, 대경목, 중경목, 소경목으로 구분한다. 영급(그림 
4f)은 구획한 산림의 평균적인 나이를 나타내는 것
으로 10년 단위로 1~6영급으로 구분한다. 소밀도(그
림 4g)는 일정한 임지에서 각 수관을 투영한 면적과 
해당 산림면적과의 비로써 소, 중, 밀의 세 단계로 구
분한다(김철민, 2008). 
4.4 토양도
일반적으로 토층은 암반층보다 산사태의 발생 빈
도가 훨씬 높다. 토양은 토양의 종류 및 성분에 따라
서 강우에 의해 포화되는 속도가 다르므로 포화된 
토양은 전단응력의 감소로 인하여 산사태가 일어날 
수 있다. 따라서 산사태와 관련있는 토양 요인들은 
농촌진흥청 발행의 1:25,000 정밀토양도로부터 지
형, 모재, 유효토심 및 토질을 추출하였다. 땅의 생긴 
모양이나 형세를 나타내는 지형(그림 4h)은 산악지, 
산록경사지(산기슭의 경사진 곳에 붕적된 토양), 선
상지, 하성평탄지(하천의 충적층을 모재로 하여 형
성된 넓은 평탄지역), 곡간지(산과 산사이 골짜기에 
퇴적된 토양), 구릉지(해발고도 200-600 m의 완만한 
기복을 이루고 있는 지형), 홍적대지(강 또는 하천에 
접해있는 평탄 내지 약한 경사지)로 구분된다. 유효
토심(그림 4i)은 작물 뿌리가 땅속으로 충분히 뻗을 
수 있는 깊이로 토양 단면중 집적층까지를 말한다. 
유효토심의 등급은 매우 얕음(0~20 cm), 얕음(20~50 cm), 
보통(50~100 cm), 깊음(100~150 cm)으로 구분된다. 
모재(그림 4j)의 속성은 회색혈암 잔적층, 화강암 잔
적층, 산성암 잔적층, 산성암 붕적층, 산성암 충적층, 
산성암 충적 붕적층, 하성 충적층, 석회암 잔적층, 잔
적층, 홍적층으로 구분된다. 토질(그림 4k)은 모래, 
미사, 점토의 상대적인 비율로 구분되고, 지역명, 토
질 및 경사정보가 들어간 코드로 구분되었다. 경사
의 기호는 A (0-2%, 평탄지), B (2-7%, 매우 약한 경
사지), C (7-15%, 약한 경사지), D (15-30%, 경사지), E 
(30- 60%, 심한 경사지), F (>60%, 매우 심한 경사지)
로 구분된다. 
4.5 지질 및 선구조 분포도
연구지역의 지질은 남서부에 분포된 선캠브리아
기의 흑운모 편마암을 기반으로 하고 있고, 그 위에 
부정합으로 놓여있는 조선계 석회암층과 평안계 녹
암층은 광범위한 임계화강암의 관입을 받고 임계화
강암은 연구지역에 가장 넓게 분포하고 있다(그림 
4l). 지질도의 지층명은 태백산지구지하자원조사단 
(1962)에서 정한 것에 따른다. 진부면을 통과하는 
NNE-SSW 방향의 주단층은 좌수향 주향이동 단층
이며, 약 4 km 간격으로 4개조로 이루어져 있다. 그
중 2개조가 연구지역을 통과하고 있고, 주 단층 사이
에는 전단단층이 수개조로 통과하고 있다(그림 4o). 
음형기복도에서 추출한 선구조는 ArcGIS 9.0의 Linedensity 
기능을 이용하여 선구조밀도로 변화하였다(그림 4m).
4.6 토지이용도
토지이용 자료는 국토지리정보원 발행의 1:25,000 
토지이용도로부터 추출하였다. 토지이용도의 속성
값은 SPOT 영상으로부터 중분류 되었고, 주거, 공
업, 상업, 교통, 공공시설, 논, 밭, 기타재배지, 낙엽활
엽수림, 침엽수림, 혼효림, 자연초지, 기타초지 및 내
륙습지로 구분되어 있다(그림 4n).
5. 분석 결과
WOE를 이용한 상관관계 분석은 우도비에 자연
로그를 취한 W+와 W-의 가중치를 적용한다. Studentized 
value인 C/S(C)는 가중치의 차 C값과 C값의 표준
편차(S(C))로 나눈값으로 정의한다(Bonham-Cater, 
1994). 요인들은 C/S(C)의 최대값을 가지는 등급의 
W+ 가중치와 W- 가중치로 이분화되고, 이분화된 
요인들의 중첩분석을 통하여 산사태 취약성도가 작
성된다(표 2, 식 8). WOE의 가중치는 0의 값을 가지
면 상관관계가 없고, (-) 값을 가지면 음의 상관관계
를, (+) 값을 가지면 양의 상관관계를 나타낸다. 본 
분석에서 연속형 혹은 범주형의 요인들은 이분형으
로 변형되기 때문에 원자료의 특성이 손실되는 취약
점을 가지고 있다. 하지만 산사태에 취약한 인자들
의 특정범위만 강조하므로 사전에 파악되지 않았던 
산사태 취약 지역에 대한 시각적인 정보를 제공한다.
WOE 분석시 1,803개의 산사태를 70:30의 비율로 
각각 1,261:542개의 분석 및 검증자료를 랜덤 추출


164
오현주
Table 2. WOE between landslide and related factors.
Factor
Class
No. of 
landslide
% of 
landslide
No. of 
pixels in 
domain
% of 
pixels in 
domain
Likelihood 
ratio
W+
W-
C
C/S(C)
Slope
(degree)
0-3
4-9
10-14
15-19
20-23
24-26
27-29
30-33
34-37
38-78
9
42
84
136
162
144
153
212
172
147
0.71
3.33
6.66
10.79
12.85
11.42
12.13
16.81
13.64
11.66
60930
68637
62206
68832
69067
55044
57515
67003
48303
40347
10.19
11.48
10.40
11.51
11.55
9.21
9.62
11.21
8.08
6.75
0.07
0.29
0.64
0.94
1.11
1.24
1.26
1.50
1.69
1.73
-2.66
-1.24
-0.45
-0.07
0.11
0.22
0.23
0.41
0.52
0.55
0.10
0.09
0.04
0.01
-0.01
-0.02
-0.03
-0.07
-0.06
-0.05
-2.76
-1.33
-0.49
-0.07
0.12
0.24
0.26
0.47
0.59
0.60
-8.25
-8.45
-4.31
-0.81
1.44
2.71
3.02
6.25
7.14
6.84
Aspect
Flat A.
N
NE
E
SE
S
SW
W
N
0
90
108
145
210
213
206
182
107
0.00
7.14
8.56
11.50
16.65
16.89
16.34
14.43
8.49
29049
68322
78853
81330
79432
67250
67857
63988
61803
4.86
11.43
13.19
13.60
13.29
11.25
11.35
10.70
10.34
0.00
0.62
0.65
0.85
1.25
1.50
1.44
1.35
0.82
NaN
-0.47
-0.43
-0.17
0.23
0.41
0.36
0.30
-0.20
0.05
0.05
0.05
0.02
-0.04
-0.07
-0.06
-0.04
0.02
NaN
-0.52
-0.48
-0.19
0.27
0.47
0.42
0.34
-0.22
NaN
-4.73
-4.80
-2.18
3.51
6.28
5.54
4.26
-2.16
Curvature
Concave(-)
Flat
Convex(+)
472
135
654
37.43
10.71
51.86
243609
118660
235615
40.75
19.85
39.41
0.92
0.54
1.32
-0.08
-0.62
0.27
0.05
0.11
-0.23
-0.14
-0.73
0.50
-2.39
-7.96
8.95
Timber
typea
Non-forest
D
H
L
M
PD
PH
PK
PL
Po
R
105
885
25
6
73
2
3
46
116
0
0
8.33 
70.18 
1.98 
0.48 
5.79 
0.16 
0.24 
3.65 
9.20 
0.00 
0.00 
185619 
259111 
34181 
3472 
59609 
1060 
1027 
11225 
41180 
144 
1255 
31.05 
43.34 
5.72 
0.58 
9.97 
0.18 
0.17 
1.88 
6.89 
0.02 
0.21 
0.27 
1.62 
0.35 
0.82 
0.58 
0.89 
1.39 
1.94 
1.34 
0.00 
0.00 
-1.32
0.48
-1.06
-0.20
-0.54
-0.11
0.33
0.66
0.29
NaN
NaN
0.28
-0.64
0.04
0.00
0.05
0.00
0.00
-0.02
-0.03
0.00
0.00
-1.60
1.12
-1.10
-0.20
-0.59
-0.11
0.33
0.68
0.31
NaN
NaN
-15.70
18.25
-5.43
-0.49
-4.88
-0.16
0.56
4.54
3.23
NaN
NaN
Timber
diameter
Non-forest
Very small 
Small
Medium
Large
111
106
223
765
56
8.80 
8.41 
17.68 
60.67 
4.44 
190346 
28120 
67740 
274967 
36710 
31.84 
4.70 
11.33 
45.99 
6.14 
0.28 
1.79 
1.56 
1.32 
0.72 
-1.29
0.58
0.45
0.28
-0.32
0.29
-0.04
-0.07
-0.32
0.02
-1.58
0.62
0.52
0.59
-0.34
-15.86
6.11
7.04
10.3
-2.50
Timber
age
Non-forest
1st age
2nd age
3rd age
4th age
5th age
6th age
111
106
73
150
501
264
56
8.80 
8.41 
5.79 
11.90 
39.73 
20.94 
4.44 
190346 
28120 
28104 
39780 
161109 
114265 
36159 
31.84 
4.70 
4.70 
6.65 
26.95 
19.11 
6.05 
0.28 
1.79 
1.23 
1.79 
1.47 
1.10 
0.73 
-1.29
0.58
0.21
0.58
0.39
0.09
-0.31
0.29
-0.04
-0.01
-0.06
-0.19
-0.02
0.02
-1.58
0.62
0.22
0.64
0.58
0.11
-0.33
-15.86
6.11
1.82
7.34
10.08
1.65
-2.38
Timber
density
Non-forest
Loose
Moderate
Dense
217
22
276
746
17.21 
1.74 
21.89 
59.16 
218466 
4583 
147713 
227121 
36.54 
0.77 
24.71 
37.99 
0.47 
2.28 
0.89 
1.56 
-0.75
0.82
-0.12
0.44
0.27
-0.01
0.04
-0.42
-1.02
0.83
-0.16
0.86
-13.65
3.87
-2.32
15.01
Topo-
graphy
Mountainous A.
Piedmont slope A.
Alluvial Fan
River
Fluvial plains
Valley A.
Hilly A.
Diluvium A.
1088
129
37
0
7
0
0
0
86.28
10.23
2.93
0.00
0.56
0.00
0.00
0.00
380390
113041
60083
8838
32471
1461
56
1542
63.62
18.91
10.05
1.48
5.43
0.24
0.01
0.26
1.36
0.54
0.29
0.00
0.10
0.00
0.00
0.00
0.30
-0.61
-1.23
NaN
-2.28
NaN
NaN
NaN
-0.98
0.10
0.08
0.01
0.05
0.00
0.00
0.00
1.28
-0.72
-1.31
NaN
-2.33
NaN
NaN
NaN
15.63
-7.7
-7.83
NaN
-6.15
NaN
NaN
NaN
Soil 
thickness
(cm)
River
0∼20
20∼50
50∼100
100∼150
0
100
148
979
34
0.00
7.93
11.74
77.64
2.70
8838
68325
114964
345144
60611
1.48
11.43
19.23
57.73
10.14
0
0.69
0.61
1.34
0.27
NaN
-0.37
-0.49
0.3
-1.32
0.01
0.04
0.09
-0.64
0.08
NaN
-0.4
-0.58
0.93
-1.4
NaN
-3.88
-6.65
13.8
-8.07
Soil 
material
River
Gray shale R.
0
153
0
12.13
8838
72003
1.48
12.04
0.00
1.01
NaN
0.01
0.01
0.00
NaN
0.01
NaN
0.10


GIS와 Weight of Evidence를 이용한 산사태 취약성 분석 및 검증
165
Granite R.
Acidic C.
Acidic A.
Acidic alluvial C.
River A.
Acidic R.
Limestone R.
R.
Diluvium
890
127
34
3
7
16
25
6
0
70.58
10.07
2.70
0.24
0.56
1.27
1.98
0.48
0.00
274938
105686
56611
4209
33679
22104
16036
2236
1542
45.99
17.68
9.47
0.70
5.63
3.70
2.68
0.37
0.26
1.53
0.57
0.28
0.34
0.10
0.34
0.74
1.27
0.00
0.43
-0.56
-1.26
-1.08
-2.32
-1.07
-0.30
0.24
NaN
-0.61
0.09
0.07
0.00
0.05
0.02
0.01
0.00
0.00
1.04
-0.65
-1.33
-1.09
-2.37
-1.09
-0.31
0.24
NaN
16.75
-6.95
-7.64
-1.88
-6.25
-4.35
-1.53
0.59
NaN
Soil 
texture
Water
Gbd
MuC
MuD
MuE
MtD
MtE
Bo
Sod
SoE
SpC
SiC
SlC
SiD
SlD
SlE
OdE
OdF
UgC
UgE
WjE
WjF
ImB
ImC
Jd
JsE
JsF
ChD
ChE
CsE
CsF
PaC
HgB
HgC
Hr
RL
RC
Gt
Gz
GpB
Ng
NkB
Dq
DEB
DEC
DED
SlB
SlC
PuB
HjN
0
0
72
6
0
2
0
0
0
0
0
18
7
12
6
6
5
11
0
0
797
68
7
23
0
5
18
12
13
55
98
0
1
0
0
6
0
0
5
0
2
0
0
0
0
0
0
4
2
0
0.00
0.00
5.71
0.48
0.00
0.16
0.00
0.00
0.00
0.00
0.00
1.43
0.56
0.95
0.48
0.48
0.40
0.87
0.00
0.00
63.2
5.39
0.56
1.82
0.00
0.40
1.43
0.95
1.03
4.36
7.77
0.00
0.08
0.00
0.00
0.48
0.00
0.00
0.40
0.00
0.16
0.00
0.00
0.00
0.00
0.00
0.00
0.32
0.16
0.00 
8838
148
39413
10193
469
2387
126
276
56
507
230
14275
7256
19879
8258
5610
18451
3653
484
185
232568
31720
20058
20832
888
1993
10990
5362
5232
13390
54126
540
2203
857
7056
2236
4912
4013
5818
1080
7143
724
2365
199
3152
1136
7580
7404
1149
462 
1.48
0.02
6.59
1.70
0.08
0.40
0.02
0.05
0.01
0.08
0.04
2.39
1.21
3.32
1.38
0.94
3.09
0.61
0.08
0.03
38.9
5.31
3.35
3.48
0.15
0.33
1.84
0.90
0.88
2.24
9.05
0.09
0.37
0.14
1.18
0.37
0.82
0.67
0.97
0.18
1.19
0.12
0.40
0.03
0.53
0.19
1.27
1.24
0.19
0.08 
0.00
0.00
0.87
0.28
0.00
0.40
0.00
0.00
0.00
0.00
0.00
0.60
0.46
0.29
0.34
0.51
0.13
1.43
0.00
0.00
1.62
1.02
0.17
0.52
0.00
1.19
0.78
1.06
1.18
1.95
0.86
0.00
0.22
00.0
0.00
1.27
0.00
0.00
0.41
0.00
0.13
0.00
0.00
0.00
0.00
0.00
0.00
0.26
0.83
0.00 
NaN
NaN
-0.14
-1.28
NaN
-0.92
NaN
NaN
NaN
NaN
NaN
-0.51
-0.78
-1.25
-1.07
-0.68
-2.05
0.36
NaN
NaN
0.49
0.02
-1.80
-0.65
NaN
0.17
-0.25
0.06
0.16
0.67
-0.15
NaN
-1.54
NaN
NaN
0.24
NaN
NaN
-0.90
NaN
-2.02
NaN
NaN
NaN
NaN
NaN
NaN
-1.36
-0.19
NaN
0.01
0.00
0.01
0.01
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.01
0.01
0.02
0.01
0.00
0.03
0.00
0.00
0.00
-0.51
0.00
0.03
0.02
0.00
0.00
0.00
0.00
0.00
-0.02
0.01
0.00
0.00
0.00
0.01
0.00
0.01
0.01
0.01
0.00
0.01
0.00
0.00
0.00
0.01
0.00
0.01
0.01
0.00
0.00
NaN
NaN
-0.15
-1.29
NaN
-0.93
NaN
NaN
NaN
NaN
NaN
-0.52
-0.79
-1.28
-1.07
-0.68
-2.08
0.36
NaN
NaN
0.99
0.02
-1.83
-0.66
NaN
0.17
-0.26
0.06
0.17
0.69
-0.17
NaN
-1.54
NaN
NaN
0.24
NaN
NaN
-0.90
NaN
-2.03
NaN
NaN
NaN
NaN
NaN
NaN
-1.37
-0.19
NaN
NaN
NaN
-1.26
-3.15
NaN
-1.31
NaN
NaN
NaN
NaN
NaN
-2.21
-2.08
-4.4
-2.63
-1.67
-4.64
1.18
NaN
NaN
16.99
0.14
-4.82
-3.16
NaN
0.39
-1.08
0.21
0.59
4.99
-1.58
NaN
-1.54
NaN
NaN
0.59
NaN
NaN
-2.02
NaN
-2.87
NaN
NaN
NaN
NaN
NaN
NaN
-2.74
-0.27
NaN
Geology
Qr
Jigr
TRn2
Oj
Pcebgn
0
1151
84
26
0
0
91.28
6.66
2.06
0
61120
460000
56695
14727
5342
10.22
76.94
9.48
2.46
0.89
0.00
1.19
0.70
0.84
0.00
NaN
0.17
-0.35
-0.18
NaN
0.11
-0.97
0.03
0
0.01
NaN
1.14
-0.38
-0.18
NaN
NaN
11.45
-3.40
-0.92
NaN
Distance 
from 
lineament
(m)
0
1-172
173-672
673-1321
1322-1996
1997-2607
2608-3079
3080-3382
276
87
102
99
103
106
108
109
21.89
6.9
8.09
7.85
8.17
8.41
8.56
8.64
229110
41043
41022
40969
40968
41013
40957
40949
38.32
6.86
6.86
6.85
6.85
6.86
6.85
6.85
0.57
1.01
1.18
1.15
1.19
1.23
1.25
1.26
-0.56
0.01
0.16
0.14
0.18
0.20
0.22
0.23
0.24
0
-0.01
-0.01
-0.01
-0.02
-0.02
-0.02
-0.8
0.01
0.18
0.15
0.19
0.22
0.24
0.25
-11.69
0.05
1.72
1.40
1.85
2.17
2.40
2.52


166
오현주
하였다. 우도비(likelihood ratio)는 WOE 계산에 사
용되며 각 요인의 등급별 산사태 발생 면적의 비율
을 의미한다. 그래서 우도비가 1이면 평균을, 1보다 
크면 산사태 발생 확률이 높다는 것을, 1보다 작으면 
산사태 발생 확률이 작다는 것을 의미한다. 따라서 
우도비를 통하여 산사태에 취약한 각 요인의 등급을 
알 수 있다. 분석 결과, 경사가 증가할수록 우도비가 
증가하는 양의 상관관계를 보이고 있다. 이는 경사
가 증가할수록 산사태 발생 확률이 높아짐을 의미한
다. 하지만 45°이상에서 산사태 발생이 1%이하로 
3383-4451
4452-8642
124
147
9.83
11.66
40942
40911
6.85
6.84
1.44
1.7
0.36
0.53
-0.03
-0.05
0.39
0.59
4.17
6.67
Land use
Residential A.
Industrial A.
Commercial A.
Transportation
Utilities
Paddy field
Field
Other agricultural L.
Deciduous forest
Coniferous forest
Mixed forest L.
Natural grasses
Other grasses
Inalnd wetland
Mixed barren L.
Inalnd water
3
0
0
2
0
0
65
0
29
1079
68
0
15
0
0
0
0.24
0.00
0.00
0.16
0.00
0.00
5.15
0.00
2.3
85.57
5.39
0.00
1.19
0.00
0.00
0.00
12575
816
615
8220
176
5859
140117
658
35038
331997
42963
4
5852
2647
5791
4556
2.10
0.14
0.10
1.37
0.03
0.98
23.44
0.11
5.86
55.53
7.19
0.00
0.98
0.44
0.97
0.76
0.11
0.00
0.00
0.12
0.00
0.00
0.22
0.00
0.39
1.54
0.75
0.00
1.22
0.00
0.00
0.00
-2.18
NaN
NaN
-2.16
NaN
NaN
-1.51
NaN
-0.94
0.43
-0.29
NaN
0.20
NaN
NaN
NaN
0.02
0.00
0.00
0.01
0.00
0.01
0.21
0.00
0.04
-1.13
0.02
0.00
0.00
0.00
0.01
0.01
-2.20
NaN
NaN
-2.17
NaN
NaN
-1.73
NaN
-0.97
1.56
-0.31
NaN
0.20
NaN
NaN
NaN
-3.80
NaN
NaN
-3.07
NaN
NaN
-13.57
NaN
-5.18
19.43
-2.46
NaN
0.76
NaN
NaN
NaN
a Timber type: Pine(D), Broad-leaved tree(H), Cultivated land(L), Mixed broad-leaf tree(M), Artici Pinus tree(PD), Poplar 
tree(PH), Pinus Koraiensis(PK), Larch(PL), Poplar tree(Po), R; A., Area; R., Residuum; C., Colluvium; L., Land.
Fig. 5. Landslide susceptibility map based on WOE.


GIS와 Weight of Evidence를 이용한 산사태 취약성 분석 및 검증
167
발생하였다. 경사면의 경우 SE, S, SW, W 방향에서 
1이상의 우도비를 보인 바 산사태에 취약한 사면으
로 나타났다. 곡률의 경우 볼록한 사면에서 산사태 
발생 확률이 더 높게 나타났다. 우기동안 오목한 사
면은 볼록한 사면 사면보다 더 많은 수분을 함유할 
수 있고 토양의 전단강도가 감소하면서 오목한 사면
보다 산사태가 더 진행될 수 있다(Lessing and Erwin, 
1977). 하지만 경사 분포나 토양의 물성변화, 분석의 
격자 크기 등과 같은 복합적 특성에 의해 오목한 사
면보다 평형 또는 볼록형 사면에서도 산사태 발생 
확률이 높을 수 있다(Ohlmacher, 2007). 임상의 경
우 소나무림(D), 포루라림(PH), 잣나무림(PK), 낙엽
송림(PL)이 분포하는 지역에는 1이상의 우도비를 
가지며 산사태에 취약한 지역으로 나타났다. 경급은 
직경이 작을수록 우도비가 증가하였고, 치수영역에
서 산사태 발생 확률이 높게 나타났다. 임상의 영급
에서는 전체적으로 1~5 영급에서는 1이상의 우도비
를 보였지만, 6영급에서 1이하의 우도비를 보인 바 
산사태 발생확률이 낮게 나타났다. 임상의 밀도는 
소밀한 지역에서 가장 높은 우도비를 보인 바 산사
태에 가장 취약한 지역으로 나타났다. 지형의 경우 
산악지역에서 산사태 발생 확률이 높게 나타났다. 
유효토심의 경우 50~100 cm 등급에서 산사태 발생 
확률이 높게 나타났다. 모재는 화강암 잔적층에서 
산사태 발생 확률이 가장 높았다. 토질은 30~60°경
사를 가지는 월정사양토에서 산사태 발생 확률이 높
게 나타났다. 연구지역은 90%이상 화강암으로 분포
하고 있으며, 이 등급에서 91%이상의 산사태가 발
생하였다. 선구조밀도는 산사태 발생과 음의 상관관
계를 보이고 있다. 이는 선구조밀도가 높을수록 산
사태 발생 확률이 높다는 것을 의미한다. 토지이용
은 침엽수림 지역에서 산사태 발생 확률이 가장 높
았다.
경사는 9th 등급인 34~37°에서 최대의 C/S(C)를 
보이며 9th 등급만 W+ 값을, 그 밖의 등급은 9th 등
급의 W- 값을 부여하였다. 경사면은 S 방향, 곡률 요
인은 볼록면, 임상의 요인들은 소나무림(D), 중경목, 
4영급, 소밀지역, 지형은 산악지역, 유효토심은 50~ 
100 cm, 모재는 화강암잔적층, 토질은 경사가 30~ 
60°인 월정 사양토, 지질은 화강암, 선구조밀도는 10th 
등급, 토지이용은 침염수림 등에서 최대 C/S(C) 값
을 보여 이들의 등급만 W+ 값으로 가중되었다. 그
밖에 모든 등급은 W- 값으로 입력하여 산사태 취약
지수(Landslide Susceptibility Index)를 계산하였
다. 계산된 취약지수는 시각적 해석을 위해 상위 10%, 
20%, 30%, 40%로 등급화하여 산사태 취약성도를 
작성하였다(그림 5). 취약지수의 최소값은 -2.98, 최대
값은 3.46, 평균값은 -0.65, 표준편차는 1.69로 나타
났다.
Table 3. Calculated X2 values for testing conditional independence between all pairs of binary patterns with each
factor related to landslide.
S.
A.
C.
D.L.
G.
L.
D.
Type
Den.
Age
Topo.
M.
Th.
A.
2.67
C.
6.89
1.72
D.L.
0.24
0.04
1.85
G.
37.4
0.00
0.89
15.9
L.
9.75
5.16
7.02
0.00 219.47
D.
10.19
2.93
1.24 13.14 25.04
5.32
Type
0.29
0.85
0.06
0.86
45.9 62.48 362.78
Den.
0.59
0.18
0.74
8.20
0.13 33.51 293.07 687.53
Age
2.02
0.07
0.98
0.18 26.36 15.43 782.38 166.49 277.79
Topo.
4.41
0.58
0.6
7.63 15.99
0.04 59.88 33.28
5.58 14.86
M.
14.36
0.12
6.15
4.70 339.28 92.14
6.44 81.15
2.66 17.22 652.21
Th.
19.31
1.32
9.23 12.63 477.62 127.59
0.62 45.09
0
5.06 108.34 1245.09
Tex.
17.45
0.89
7.33
6.58 287.49 86.15
5.33 48.77
3.91 49.64 463.77 1280.66 885.36
S., Slope; A., Aspect; C., Curvature; D.L., Density of lineament; G., Geology; L., Lanuse, D., Diameter; Den., Density;
Topo., Topography; M., Material; Th., Thickness; Tex., Texture.


168
오현주
LSIWOE = ∑WOE                                               (8)
(WOE; 각 요인의 W+와 W-)
WOE 방법에서는 요인들간의 독립성을 가정하기 
때문에 본 연구에서는 요인들간의 독립성 검증을 수
행하였다. 각 요인들간의 독립성 검정은 99%의 신
뢰도 하에 자유도가 1일 때 카이제곱 6.63값을 기준
으로 설정하여 수행하였다(표 3). 만약 요인별 카이
제곱 값이 6.63값보다 크다면 상관관계의 존재를 고
려하여 산사태 취약성 분석시 상관성있는 요인들은 
제거하였고, 이들의 새로운 조합을 만들어 산사태 
취약성도를 작성 및 검증하였다. 
6. 취약성도 검증
WOE 방법을 이용하여 도출된 산사태 취약지수
는 추정(assessment)값에 해당되므로 검증이 필요
하다. 이를 위해 Success Rate Curve (SRC)와 Area 
Under the Curve (AUC) 방법을 이용하였다(Lee, 
2005). 취약성도의 검증은 분석에 사용되지 않은 산
사태 자료를 이용하여 비교·검증하였다. SRC 그래
프의 X축은 산사태 취약지수를 상위 퍼센트로 등급
화한 값이고, Y축은 검증용 산사태 누적 퍼센트의 
등급값이다. 독립성 검증을 통하여 상관성있는 요인
들을 제거하고 표 4와 같이 요인들을 조합하였다. 그 
중 경사, 경사면, 곡률, 선구조밀도, 토지이용, 임상, 
영급, 모재 등의 조합이 가장 높은 72.90%의 예측 정
확도를 보였다.
Table 4. Combination of factors related to landslide by testing conditional independence.
No. Standard 
factor
Independent factor
Validation 
accuracy(%)
1
Slope
Aspect, Lineament, Timber type, Timber density, Timber age, Topography
65.76
2
Aspect
Slope, Curvature, Lineament, Geology, Land use, Timber diameter, 
Timber type, Timber density, Timber age, Topography, Soil material, Soil 
thickness, Soil  texture
71.97
3
Curvature
Aspect, Lineament, Geology, Timber diameter, Timber type, 
Timber density, Timber age, Topography, Soil material
68.79
4
Lineament
Slope, Aspect, Curvature, Land use, Timber type, Timber age, Soil material
72.90
5
Geology
Aspect, Curvature, Timber density
61.20
6
Land use
Aspect, Lineament, Timber diameter, Topography
72.28
7
Timber diameter Aspect, Curvature, Land use, Soil thickness, Soil  texture
70.83
8
Timber type
Slope, Aspect, Curvature, Lineament
70.40
9
Timber density
Slope, Aspect, Curvature, Geology, Topography, Soil material, 
Soil thickness, Soil  texture
70.13
10
Timber age
Slope, Aspect, Curvature, Lineament, Soil thickness
68.62
11
Topography
Slope, Aspect, Curvature, Land use, Timber density
70.51
12
Soil material
Aspect, Curvature, Lineament, Timber density
67.07
13
Soil thickness
Aspect, Timber diameter, Timber density, Timber age
63.31
14
Soil  texture
Aspect, Timber diameter, Timber density
68.00
0
10
20
30
40
50
60
70
80
90
100
0
10
20
30
40
50
60
70
80
90
100
Rank(%) of landslide susceptibility index
Culmulative percentage of landslide occurrence
Combination 4 (72.90%)
Fig. 6. Illustration of cumulative frequency diagram 
showing landslide susceptibility index rank (x-axis) 
occurring in cumulative percent of landslide occurrence
(y-axis).


GIS와 Weight of Evidence를 이용한 산사태 취약성 분석 및 검증
169
7. 결론 및 토의
 
진부면지역의 산사태는 산사태 발생 전후의 항공
사진을 이용하여 접근이 어려운 지역과 규모가 작은 
산사태까지 판독하였다. WOE 기법을 이용한 산사
태 취약성 분석에서는 산사태 개수의 70%만 사용하
였고, 나머지 30%는 취약성도 검증 위해 사용하였
다. 취약성도는 각 요인들간의 독립성 검증을 통해 
14개의 조합으로 작성되었고, 최대 정확도를 보이는 
조합은 경사, 경사면, 곡률, 선구조밀도, 토지이용, 
임상, 영급, 모재로써 72.90%의 예측 정확도를 보였다. 
일반적으로 예측도의 검증자료는 다른 시기의 사
건자료가 사용된다. 하지만 연구지역의 산사태는 동
일 시기의 발생이었고, 동일 지역에서 다른 시기의 
산사태가 발생하지 않는 한 검증자료의 획득은 어려
움이 있다. 따라서 산사태 취약성 검증을 위해 분석
에 사용하지 않은 산사태 위치를 검증용으로 사용하
였다. 강우는 산사태 발생 매우 큰 영향을 미치는 중
요 요인이며, 연구지역 역시 집중강우에 의해 많은 
산사태가 발생하였다. 그러나 평창군 진부면지역의 
시간별 강우량 변화 혹은 누적 강우량 자료는 수집
하기가 어렵기 때문에 진부면의 강우량은 동일하다
는 전제 하에 취약성 분석을 수행하였다. 만약 본 분
석의 지역을 행정구역단위로 확장한다면 기상청 강
우자료의 사용이 가능할 것이다.
WOE 기법에서의 입력자료는 "연속형-등급형-이
분형" 자료의 형태로 변형되어 최대 가중치를 가지
는 등급을 제외한 나머지 등급은 음의 가중치로 대
체되기 때문에 예측 정확도를 향상시키기에는 어느 
정도 한계를 가지고 있다. 하지만 각 요인별 최대 가
중치를 가지는 등급간의 중첩분석은 우리가 사전에 
인지할 수 없었던 매우 취약한 지역의 패턴을 제시
해준다. 따라서 본 자료는 토지계획과 매우 관련있
는 자료로써 토지이용 정책의 의사결정에 매우 중요
한 자료로 사용될 수 있을 것이다. 
사 사
이 논문은 한국지질자원연구원의 기본 연구사업
인 "GIS 기반 국토지질정보시스템 실용화 기술 개발" 
과제의 일환으로 수행되었다.
참고문헌
 
태백산지구지하자원조사단, 1962, 태백산 지구 지질도
(1:50,000), 하진부 도폭. 대한지질학회.
김철민, 2008, 산림자원정보 인벤토리 구축과 활용. 농업환
경자원 인벤토리 구축과 활용 전략 국제 워크숍, 농촌진
흥청, 6월 26일, 320 p.
Bonham-Carter, G.F., 1994, Geographic Information Systems 
for geoscientists, modeling with GIS. (Oxford: Pergamon 
Press). 
Bonham-Carter, G.F., Agterberg, F.P. and Wright, D.F., 
1989, Weights of evidence modeling: A new approach 
to mapping mineral potential, In: Agterberg, F. P. and 
Bonham-Carter, G.F., (eds.), Statistical Applications in 
the Earth Sciences. Geological Survey of Canada, 989, 
171-183.
Griffiths, J.S. and Hearn, G.J., 1990, Engineering geo-
morphology: a UK perspective. Bullein of the International 
Association of Engineering Geology, Vol 42, p. 39-44.
Johnes, D.K., Brunsden, D. and Goudie, A.S., 1983, A pre-
liminarly geomorphological assessment of part of the 
Karakoram highway. The Q. J. of Engineering Geology, 
16, 331-355.
Koret, George B., 1997, The GIS book: Understanding the 
value and implementation of geographic information 
systems. Onword Press 4ed.
Lee, S. and Choi, J.W., 2004, Application of a weight- 
of-evidence model to landslide susceptibility analysis. 
International Journal of Geographic Information Science, 
18, 789-814.
Lee, S. and Min, K.D., 2001, Statistical analysis of land-
slide susceptibility at Yongin, Korea. Environmental 
Geology, 40, 1095-111.
Lee, S., 2005, Application and cross-validation of spatial 
logistic multiple regression for landslide susceptibility 
analysis. Geosciences Journal, 9, 63-71.
Lee, S., Choi, J.W. and Min, K.D., 2002, Landslide sus-
ceptibility analysis and verification using the Bayesian 
Probability model. Environmental Geology, 43, 120- 
131. 
Lee, S., Ryu, J.-H., Lee, M-J. and Won, J.-S., 2003b, 
Landslide susceptibility analysis using artificial neural 
network at Boun, Korea. Environmental Geology, 44, 
820-833.
Lee, S., Ryu, J.-H., Min, K.D. and Won, J.-S., 2003a, 
Landslide Susceptibility Analysis using GIS and Artificial 
neural network. Earth Surface Processes and Landforms, 
27, 1361-1376.
Lessing, P. and Erwin, R.B., 1977, Landslides inWest 
Virginia. In: Coates, D.R. (Ed.), Landslides. Geological 
Society of America, Boulder, CO, Reviews in Engineering 


170
오현주
Geology, 3, 245-254.
Ohlmacher, G. C., 2007, Plan curvature and landslide 
probability in regions dominated by earth flows and  
earth slides. Engineering Geology, 91, 117-134.
Spiegelhater, D. and Kill-Jones, R.P., 1984, Statistical and 
knowledge approaches to clinical decision-support systems, 
with an application in gastroenterology. Journal of the 
Royal Statistical Society, 147, 35-77.
━━━━━━━━━━━━━━━━━━━━━━━━
투    고    일   :   2010년     1월    31일
심    사    일   :   2010년     2월      1일
심사완료일   :   2010년     2월    26일
