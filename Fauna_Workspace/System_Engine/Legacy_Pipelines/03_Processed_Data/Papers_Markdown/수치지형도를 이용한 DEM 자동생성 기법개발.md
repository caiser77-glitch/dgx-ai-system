--- 
source: 수치지형도를 이용한 DEM 자동생성 기법개발.pdf
--- 

한국지리정보학회지 10권 3호 : 113～122(2007)
―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
수치지형도를 이용한 DEM 자동 생성 기법의 개발
박찬수1·이성규2·서용철3※1)
Development of an Automatic Generation 
Methodology for Digital Elevation Models using 
a Two-Dimensional Digital Map
Chan-Soo PARK1·Seong-Kyu LEE2·Yong-Cheol SUH3※
요    약
최근 항공측량과 위성정보 기술의 급속한 발전은 방대한 지리정보 데이터의 신속한 취득을 가능
케 하고 있다. 취득된 지리정보를 정확하게 표현하고 분석하기 위해서는 대용량 데이터를 실시간
으로 시각화하는 기술을 필요로 하며, 실시간 시각화를 위해 LOD(Lovel of Detail) 알고리즘을 핵
심 요소로 적용하고 있다.
본 연구는 다양한 지리정보 데이터 중 수치지형도에 포함된 등고선 데이터를 활용하여 정규화 
된 고도정보를 생성하는 방법으로써 TIN 생성기법을 적용하였고, 정규화 된 고도 정보를 생성하기 
위해서 본 연구에서는 2단계의 작업으로 구분하여 생성하였다. 먼저 수치지형도를 활용하여 TIN 
데이터를 생성하고, 생성된 TIN 데이터를 이용하여 정규화 된 고도정보를 생성하고자 하는 지역 
크기의 2차원적 격자 배열을 생성하고, 격자 배열의 각 점과 생성된 불규칙 삼각망의 교차점을 구
하여 정규화 된 고도정보를 생성할 수 있다.
본 연구에서는 각 단계 별로 제한된 딜로니 삼각분할(CDT, Constrained Delaunay Triangulation) 
알고리즘과 생성된 TIN 데이터와 2차원적 격자 배열 각 점의 교차점을 구하기 위해 Ray-Triangle 
Intersection 알고리즘을 선택하였다. 또한, DirectX API 라이브러리, Quad-Tree LOD 알고리즘 그
리고 프로그램 개발언어인 Microsoft Visual C++ 6.0을 이용하여 정규화된 고도정보를 3차원 지형 
실시간 시각화를 통해 3차원 지형 시뮬레이션을 하였다.
주요어 : DEM, CDT, Ray-Triangle Intersection, 등고선, 지형, 수치지형도, LOD
ABSTRACT
The rapid growth of aerial survey and remote sensing technology has enabled the rapid 
acquisition of very large amounts of geographic data, which should be analyzed using real-time
   2007년 8월 21일 접수 Received on August 21, 2007 / 2007년 9월 21일 심사완료 Accepted on September 21, 2007
 1 부경대학교 위성정보과학과 석사과정 Dept. of Satellite Information Sciences,  Pukyong National University
 2 부경대학교 위성정보과학과 학부과정 Dept. of Satellite Information Sciences,  Pukyong National University
 3 부경대학교 위성정보과학과 조교수 Dept. of Satellite Information Sciences,  Pukyong National University
※ 연락저자 E-mail : suh@pknu.ac.kr


Development of an Automatic Generation Methodology for Digital Elevation Models using a Two-Dimensional Digital Map
―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
114
visualization technology. The level of detail(LOD) algorithm is one of the most important 
elements for realizing real-time visualization. We chose the triangulated irregular network 
(TIN) method to generate normalized digital elevation model(DEM) data. First, we generated 
TIN data using contour lines obtained from a two-dimensional(2D) digital map and created a 
2D grid array fitting the size of the area. Then, we generated normalized DEM data by 
calculating the intersection points between the TIN data and the points on the 2D grid array. 
We used constrained Delaunay triangulation(CDT) and ray-triangle intersection algorithms to 
calculate the intersection points between the TIN data and the points on the 2D grid array in 
each step. In addition, we simulated a three-dimensional(3D) terrain model based on normalized 
DEM data with real-time visualization using a Microsoft Visual C++ 6.0 program in the 
DirectX API library and a quad-tree LOD algorithm.
KEYWORDS : DEM, CDT, Ray-Triangle Intersection, Contour Line, Terrain, 2D Digital Map, LOD
서  론
최근 컴퓨터 그래픽스 기술의 발전은 대용
량 지리정보 데이터의 실시간적 3차원 모델화 
구현을 가능케 하였다. 실시간적 3차원 모델화 
구현을 위해서는 일반적으로 규칙적인 격자 
행렬(gridded matrix)을 통해 공간상에 나타나
는 지형기복의 변화를 연속적으로 표현하는 
모형(Burrough, 1986)인 DEM 데이터가 필요
하다.
DEM 데이터는 3차원 지형 가시화를 통해 
비행 시뮬레이션, 가상현실 등을 구현하는데 
많이 이용되고 있다. 또한, 한반도 지형의 경
사도 분석, 도시경관의 지형적 특성 분석 등 
지형 특성을 분석 연구하는 지리학 연구(이금
산 등, 2000; 한갑수, 2003), 수문학, 지구과학, 
토목, 천연자원 관리, 군사적 목적 그리고 폐
기물 매립지의 적지분석 등과 같은 분야에서
도 
광범위하게 
이용되고 
있다.(김성준 
등, 
2005; 이진덕 등, 2000). 3차원으로 구현된 지
형도는 시각적으로 형상화 되어 있으므로, 무
기 유도 체계 등의 특수 목적을 위해 그 활용
도가 증가되고 있는 추세이다. 현재 넓은 지역
의 대용량 3차원 지형정보 가시화를 위해 많
은 연구가 진행 되고 있으며, 적용분야에 따라 
경제적이고 정확한 지형정보를 구축하기 위한 
연구가 지속적으로 이루어질 필요가 있다.
DEM 데이터의 취득방법에는 LiDAR 데이
터, 고해상도 위성영상 등을 이용한 방법과 수
치지형도를 이용한 방법 등이 있다. 그러나 
LiDAR 데이터, 고해상도 위성영상을 이용한 
DEM 데이터 취득방법은 정확도 높은 데이터
를 취득할 수 있으나, 데이터 취득의 어려움과 
데이터 취득에 따른 고비용 발생으로 인해 넓
은 지역을 대상으로 한 3차원 모델화 구현을 
하기에는 적절한 방법이라고 할 수 없다. 따라
서 본 연구에서는 다양한 지리정보 데이터 중 
수치지형도에 포함된 등고선 데이터를 이용하
여 TIN 방법으로 DEM 데이터를 생성하였다. 
또한, 단순히 등고선의 점 정보만을 이용하지 
않고 선분 정보를 더하여 선분을 따라 강제로 
분할하는 CDT 알고리즘을 채택하여, TIN의 
생성에 있어 등고선 데이터의 손실을 최소화
하고 대용량의 DEM 데이터를 생성하고자 하
였다.
불규칙 삼각망(TIN, Triangulated Irregular 
Networks)은 불규칙하게 분포된 등고선의 점
을 추출하여 이들의 위치를 삼각형의 형태로 
표현하는 방법으로 적은 양의 자료를 사용하
여 복잡한 지형을 상세하게 나타낼 수 있다는 
장점이 있다. 삼각형을 구성하는 선분의 길이
는 다양하므로 복잡한 지형의 경우 작은 면적


수치지형도를 이용한 DEM 자동 생성 기법의 개발 / 박찬수・이성규・서용철
―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
115
레이어코드
내     용
1
2
3
4
5
6
7
8
9
철도
하천
도로
건물
지류
시설물
지형
행정경계 및 지형경계
주기
TABLE 1. NGIS 수치지형도의 레이어코드
레이어코드
내    용
7111
7112
7113
7114
주곡선
간곡선
조곡선
계곡선
볼록지
7211
7212
7213
7214
주곡선
간곡선
조곡선
계곡선
오목지
TABLE 2. NGIS 수치지형도의 지형코드
FIGURE 1. DEM 생성 흐름도
의 
삼각형을 
사용하여 
자료의 
밀도가 
높은 
TIN을 구성할 수가 있고 계곡이나 골짜기 등
은 자료의 밀도를 높임으로써 지표면의 형태
를 비교적 정확하게 나타낼 수 있다.(김계현, 
1998). 이와 같이 TIN 방법은 등고선에서 직
접 DEM을 추출하는 방식에 비해 비교적 정
확하게 지표면을 나타낼 수 있으므로 TIN 생
성 과정을 거쳐 생성된 TIN을 이용하여 DEM
을 만드는 것이 가장 이상적이라 할 수 있다.
DEM 생성
수치지형도 DXF 형식은 3차원 좌표계를 이
용 있으며, 등고선의 경우에는 polyline으로 정
의되어 있다. 이 등고선 데이터를 활용해 3차
원 DEM 데이터를 생성하기 위해서는 선분으
로 이루어진 polyline 각 선분의 X, Y좌표를 
활용해 CDT 알고리즘으로 TIN을 생성하여 3
차원 좌표를 가진 삼각형의 집합을 구성한다. 
생성된 삼각형의 집합을 이용하여 DEM 데이
터를 생성하고자 하는 영역에 대해 정규화 된 
2차원적 배열의 DEM 격자(grid)를 생성하고, 
2차원 평면상의 X좌표와 Y좌표를 일정한 간
격으로 변형하면서 각 점들을 TIN 방법으로 
생성된 3차원 삼각형에 수직 정사하여 Z값을 
구함으로써 DEM 격자의 고도값을 생성할 수 
있다.
본 논문에서 사용된 TIN 생성을 위한 CDT 
알고리즘은 단순히 등고선의 표고 데이터를 
이용하여 삼각분할 하는 방법보다, polyline을 
이루는 각각의 선분을 강제로 분할하여 등고
선의 
원시정보를 
최대한 
보장하게 
되므로 
DEM의 정확도를 높일 수 있다.
CDT(Constrained Delaunay 
Triangulation)를 이용한 TIN 생성 
1. 지형데이터 추출
기본 지형 데이터는 1：5,000 수치지형도 데
이터를 사용하였다. 수치지형도는 표1과 같이 
등고선 정보뿐만 아니라 다양한 지형정보를 
포함하고 있다. DEM 데이터를 구축하기 위해
서는 수치지형도에서 레이어 코드 7번에 해당
하는 지형데이터만을 추출하여야 한다. TIN 
방법에 의해 DEM을 생성하기 위해서는 지형


Development of an Automatic Generation Methodology for Digital Elevation Models using a Two-Dimensional Digital Map
―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
116
 FIGURE 2. 등고선이 존재하지 않는 데이터              FIGURE 3. 표고점의 보정
        (a) Delaunay Triangulation               (b) Constrained Delaunay Triangulation
FIGURE 4. DT 알고리즘과 CDT 알고리즘의 TIN 생성 비교
데이터의 등고선과 표고점을 이용하여 TIN을 
형성해야 하고 등고선을 추출함에 있어 3차원 
점 
정보가 
아닌 
선분정보가 
포함된 
3차원 
polyline 형태의 데이터를 생성하는 과정을 필
요로 한다.
2. Constrained Delaunay Triangulation
DEM이 만들어지고 저장되는 방식은 크게 
2가지 방식으로 나눌 수 있는데, 일정크기의 
격자로 저장되는 DEM, 불규칙한 삼각형에 의
한 TIN 방식이 그것이다. 이밖에 등고선에 의
한 방식이나 단층에 의한 방식도 있으나, 3차
원 
지형 
모델링을 
가시화 
하는데 
있어서 
DEM이나 TIN방식에 비해 잘 사용되지 않는
다. 등고선에서 TIN을 구성하지 않고 DEM을 
생성할 경우 그림 2와 같은 지역은 그림 3과 
같이 표고점 보정을 해주어야 되는데, CDT 
알고리즘으로 TIN을 구성할 경우, 그림 2의 
데이터가 없는 지역은 자동으로 높이 값이 같
은 3차원 공간상의 삼각형으로 생성되어, 고도
값이 동일한 DEM 데이터로 생성된다.
딜로니 삼각분할(DT, Delaunay Triangulation) 
이론이란 삼각형이 세 정점 모두에서 볼 수 
있는 새로운 점을 삼각형의 외접원 내부에 포
함하지 않도록 하는 것이다. 제한된 딜로니 삼
각분할(CDT, Constrained Delaunay Triangulation) 
이론은 포함될 선분 집합 일부가 미리 명시되
고 가능한 DT 이론에 만족하는 삼각분할을 


수치지형도를 이용한 DEM 자동 생성 기법의 개발 / 박찬수・이성규・서용철
―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
117
FIGURE 5. 수치지형도의 등고선                 FIGURE 6. CDT에 의해 구성된 TIN
말한다. CDT를 구하는 최적의 알고리즘은 분
할된 정복 기법을 사용한 것으로 O(nlogn)의 
시간 복잡도를 가진다. 여기서, DEM 생성을 
위해 CDT를 사용하는 것은 등고선에 있는 모
든 선분이 포함되도록 딜로니 삼각분할을 수
행한다는 의미이다.
딜로니 삼각분할 알고리즘으로 단순히 점 
데이터만을 이용하여 TIN 생성을 하면, 그림 
3(a)와 같이 등고선이 지나가는 선상에서 왜곡된 
삼각분할이 일어날 수 있는데 반해, 제한된 딜
로니 삼각분할 알고리즘은 그림 3(b)와 같이 
등고선의 선분 정보를 그대로 표현하면서 TIN
을 생성하기 때문에 등고선이 가지고 있는 지
형 데이터의 손실 없이 삼각분할이 가능하다.
그림 4는 1：5,000 수치지형도에서 지형정보를 
가진 등고선과 표고점을 추출한 지형 데이터
이고, 그림 5는 추출한 지형 데이터를 제한된 
딜로니 삼각분할 알고리즘을 이용하여 생성된 
TIN 데이터이다. 그림 5와 같이 생성된 TIN 
데이터는 2차원적으로 삼각 분할된 데이터의 
집합이지만, 삼각형을 이루는 각각의 점들은 
실제 고도 값을 가진 3차원 점 데이터이다.
기하학적 기법에 의한 DEM 고도 값 생성
앞 장에서 생성된 TIN을 바탕으로 DEM생
성할 영역 크기의 정규화 된 2차원적 격자 배
열을 생성하였다. 여기서, DEM의 격자 간격은 
원시 데이터 수치지형도의 등고선 간격으로 
하는 것이 적당하며 더 정밀한 격자 간격을 
부여하는 
것은 
무의미하다. 
따라서 
1：5,000 
수치지형도의 경우 등고선간격이 5m 이므로 
DEM 격자 간격을 5m로 하였다. 격자 형식의 
2차원 배열은 수치지형도의 영역과 동일하고 
각각의 점들은 고도 값이 없는 3차원 좌표로 
생성되어 져야 한다. TIN을 이루는 3차원 공
간의 삼각형들과 DEM 2차원 격자 배열을 이
루는 각각의 점들에서 Z값이 무한대인 점으로 
이루어진 선분의 교차점을 GRID 3차원 좌표
의 표고 값으로 입력하였다. 삼각 분할된 삼각
형과 선분의 교차점으로 얻어진 고도 값은 수
치지형도의 등고선과 등고선 사이 지형 사면
의 DEM 고도 값을 표현하게 된다. 
3차원 선분과 삼각형의 교차점을 계산하
기 위해서 Ray-Triangle Intersection 알


Development of an Automatic Generation Methodology for Digital Elevation Models using a Two-Dimensional Digital Map
―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
118
FIGURE 7. 2차원 격자 배열 생성               FIGURE 8. DEM 고도값 생성
고리즘(Möller 등, 1997)을 이용하였다. 여
기에서, 3차원 선분은 DEM 각 점의 X, 
Y좌표와 Z값이 무한대인 점으로 이루어
진 선분(ray)을 나타내고 있다.
1. DEM 고도 데이터 생성
앞에서 생성된 TIN 데이터(그림 5)는 2차
원적 좌표로 삼각분할을 수행하였지만, TIN
을 구성하는 삼각형들의 각 점들은 등고선
의 높이 값을 모두 가지고 있다. DEM 고도
데이터를 
생성하기 
위해 
그림 
7과 
같이 
TIN 영역에 DEM 격자의 크기에 맞는 2차
원적 가상의 격자 배열을 생성하였다. 그림 
8과 같이 2차원 격자 배열의 각 점들을 포
함하는 TIN 데이터 상의 3차원 삼각형에 
Ray-Triangle Intersection 알고리즘을 적용
하여 그리드 각 셀의 고도 값을 구한다. 이
러한 작업은 1：5,000 수치지형도 한 도엽을 
작업하는데 수십 초의 시간이 소요된다. 따
라서 서로 인접하거나 혹은 인접하지 않은 
많은 양의 도엽 작업일 경우, 도엽의 수와 
DEM의 통합시간에 비례하는 생성 시간을 
가지게 된다.
DEM 자동 생성과 3차원 지형 가시화
DEM 생성 자동화 시스템에 사용된 대상 
수치지형도는 서로 인접한 1:5,000 수치지형
도 699개의 도엽을 비메모리 방식의 특정영
역의 DEM으로 변환하여 하나의 DEM으로 
통합하는 과정을 거친 후, 프로그램 개발언어
인 
Microsoft 
Visual 
C++ 
6.0 
환경 
하에 
DirectX 그래픽 라이브러리, 음영기복도 생성 
모듈, Quad-Tree LOD 알고리즘을 이용하여 
3차원 지형을 실시간 가시화하였다.
1. DEM 생성에 수치지도 인덱스
DEM생성에 사용된 수치지도는 2001년도 
정사영상지도 1：5,000(GRS)으로 그림 9와 
같이 보령지역 일대 신온, 홍성, 예산, 고남, 
보령, 청양, 연도, 서천, 한산, 지역 총 699도
엽을 
사용하였고, 
DEM 
간격은 
5미터를 
기준으로 가로 67,010m, 세로 83,330m 영역
을 DEM 격자 가로 13,402개, 세로 16,666개
의 DEM 격자수를 가지는 DEM을 생성하
였다.


수치지형도를 이용한 DEM 자동 생성 기법의 개발 / 박찬수・이성규・서용철
―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
119
FIGURE 9. DEM 생성 자동화 테스트에 사용된 수치지도 인덱스
2. DEM 생성 자동화와 음영 기복도 생성
시스템에 사용된 699도엽의 수치지형도 모
두를 
제한된 
시스템의 
메모리에 
상주 
시켜 
DEM 생성 작업을 하는 것은 불가능하다.
FIGURE 10. DEM 자동 생성 시스템 
따라서, 수치지형도 각각의 영역에 해당하는 
인덱스들만 메모리에 상주시키며 일정한 영역
에 포함되는 인덱스의 등고선을 메모리에 상
주 시키고 이미 사용된 수치지도의 인덱스 내
에 포함되는 등고선의 ployline 데이터는 메모
리에서 제거 하는 방식을 사용함으로 메모리
의 
효율성을 
최대화 
하였다. 
그림 
10 
에서 
DEM을 자동생성하기 전에 자동 생성에 DEM
을 생성하고자 하는 영역을 지정하고, DEM의 
격자크기를 조절 하며, 시스템을 사용하는 컴
퓨터의 사양에 따라 메모리 상주 량을 조절 
할 
수 
있는 
메모리 
CUT_SIZE를 
입력하여 
DEM의 생성 조건을 요구에 따라 설정하였다.
DEM 생성이 끝난 후 DEM 을 이루는 각 
점 들의 Normal 벡터를 주위 8개의 점들로 8
개의 삼각형을 구성하여 각 면들의 Normal 벡
터의 합으로 구하고 와 임의의 태양 각을 입
력하여 그림 11과 같이 음영기복도를 생성해 
DEM의 정확성을 가시적으로 확인하였다.
3. Quad-Tree LOD 처리와 3차원 지형 실
시간 가시화
LOD(Level of Detail)는 대용량의 데이터를 
실시간에 자연스러운 처리를 위해서 사용되는 
기법으로 3차원 지형을 표현하기 위한 기술 
중 중요한 기술로 부각 되고 있다. 위에서 자
동 생성된 DEM을 실시간으로 가시화하기 위
해서 기존에 연구된 4진 트리 방식인 Quad- 


Development of an Automatic Generation Methodology for Digital Elevation Models using a Two-Dimensional Digital Map
―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
120
FIGURE 11. DEM에서 도출된 음영기복도
   
   
FIGURE 12. 생성된 DEM을 이용한 실시간 가시화


수치지형도를 이용한 DEM 자동 생성 기법의 개발 / 박찬수・이성규・서용철
―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
121
Tree 알고리즘을 채택하였다. Rottger et al. 
(1997) 은 Quad-Tree 구조의 top-down 방식
을 사용하여 렌더링 되는 각 프레임에서 전
체 지형 중 일부분만을 다루게 하여 많은 
양의 지형에도 높은 프레임 속도를 가능하
게 방식을 제안하였다. 이 방식은 쿼드트리 
행렬에 의해 구성된 삼각형이 지형에 대응
되는 행렬의 요소가 1로 되어 있는 부분만
을 재귀적으로 쿼드트리를 순회하면서 트라
이앵글 팬(triangle fan)을 사용하여 렌더링 
하는 방식이다.
본 시스템에서는 Quad-Tree LOD 알고리즘
과 Microsoft DirectX 그래픽 API를 사용하여 
자동 생성된 DEM을 3차원 지형으로 실시간 
가시화 하였다.
결  론
본 연구는 단순히 수치지형도에서 추출한 
등고선의 점만을 이용하는 것이 아니라, 등고
선의 선분 정보도 함께 이용하는 제한적 딜로
니 삼각분할 알고리즘을 이용하여 TIN을 생
성하고, 생성된 불규칙 삼각망(TIN)과 2차원
적 격자 배열 각 점의 교차점을 구하는 Ray- 
Triangle Intersection 알고리즘으로 계산된 고
도값을 이용하여 DEM을 자동 생성하였다.
DEM 데이터는 수치지형도의 등고선 높이 
값에 기인되어 생성된다. 수치지형도의 등고선
에 포함된 등고선 오류를 수정하지 않고 작업
할 경우, DEM 데이터의 정확도에 영향을 줄 
수 있으므로, 수치지형도에서 지형데이터 추출 
후 등고선 오류를 보정하는 작업이 필요하다.
또한, 수치지형도의 각 도엽별로 DEM을 생
성하고, 서로 인접한 도엽의 DEM 격자를 재
배치하는 방식으로 대용량의 DEM 데이터 생
성이 가능하다. 이 때 인접한 도엽간의 접합지
역에 있어서 각각의 TIN 데이터를 생성할 때 
생기는 오차를 줄일 수 있는 방안이 필요하다.
LiDAR, 위성영상 등 고정밀도의 측량장비
로 추출한 DEM 데이터와는 비교대상이 될 
수 없다. 그러나 제한적 딜로니 삼각분할과 
Ray-Triangle Intersection 알고리즘을 이용한 
DEM 생성방법은 고가의 측량장비 없이 저비
용으로 경제적이면서 빠르게 DEM 데이터를 
추출할 
수 
있다. 
또한 
본 
연구에서 
개발한 
DEM 생성 자동화 소프트웨어는 DEM 데이터 
생성 절차를 단축하여 기존에 소요된 시간과 
비용을 절감할 뿐만 아니라, 넓은 지역의 대용
량 지형 데이터를 생성하는데 보다 효율적이
고 경제적으로 DEM 데이터를 생성할 수 있
었다.
또한 생성된 3차원 지형 데이터인 DEM 데
이터는 경사도, 사면방향, 지형단면 등과 같이 
한 지역의 기본적 지형 특성을 분석 연구하는 
지리학 연구, 산사태, 홍수 등을 예측하고 시
뮬레이션 하는 방재 분야, 비행 시뮬레이션, 
가상현실 등과 같은 3D 시뮬레이션, 그리고 
군사적 목적, 도시계획·단지설계 및 폐기물처
리, 온라인 게임 등 지형 데이터를 활용하는 
모든 분야에서 광범위하게 적용되어 활용될 
수 있을 것으로 기대된다. 
참고 문헌
김계현. 1998. GIS 개론(자료분석편, ‘도형자료와 
속성자료의 
통합 
분석’, 
206-265쪽). 
大英社, 
서울.
김성수, 김경호, 이종훈. 2001. 등고선 데이터를 
이용한 3차원 지형 렌더링. 한국정보과학회지 
28(1B):625-627.
김성준, 김대식, 김철, 배덕효, 신사철, 조명희, 조
기성. 2005. GIS 개념과 기법(수치지형 모델링
편, ‘수치지형모형의 응용’, 411-417쪽). 시그마
프레스(주), 서울.
Tomas Akenine-Moller, Eric Haines. 2003. 리
얼-타임 렌더링 2판(교차 검사 방법들편, ‘광
선/삼각형 교차’). 정보문화사, 서울.
유병현, 한순흥. 2002. 비행 시뮬레이션을 위한 
실시간 지형 데이터의 구축. 한국CAD/CAM학
회 2002학술발표논문집. 267-274쪽.


Development of an Automatic Generation Methodology for Digital Elevation Models using a Two-Dimensional Digital Map
―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
122
이근상, 채효석, 조기성. 2003. DEM 표준오차를 
고려한 TIN 구축의 효용성 분석에 관한 연구. 
한국GIS학회지 11(1):23-31.
이금산, 조화룡. 2000. DEM 을 이용한 한반도 
지형의 경사도 분석. 한국지리정보학회지 3(1): 
35-43.
이진덕, 연상호, 김성길. 2000. GIS를 활용한 폐
기물 매립지의 적지분석 사례연구. 한국지리정
보학회지 3(4):33-49.
한갑수. 2003. GIS와 원격탐사를 이용한 경관
유형의 특성분석. 한국지리정보학회지 6(3): 
117-128
Badouel, Didier. 1990. An Efficient Ray-Polygon 
Intersection, in Graphics Gems, ed. Andrew 
S. Glassner, Academic Press. pp 390-393.
F. Aurenhammer and R. Klein. 2000. Voronoi 
diagrams. In J.-R. Sack and J. Urrutia, 
editors, 
Handbook 
of 
Computational 
Geometry. 201pp.
G. E. Blelloch, G. L. Miller, J. C. Hardwick, and 
D. Talmor. 1990. Design and implementation 
of a practical parallel Delaunay algorithm. 
Algorithmica
Haines, Eric. 1994. Point in Polygon Strategies. 
Graphics Gems IV, Academic Press. pp 22-46.
K. Mehlhorn, S. NAaher. 2000. LEDA: A Platform 
for Combinatorial and Geometric Computing. 
Cambridge University Press, Cambridge, UK
Overview of Quadtree-based Terrain Triangulation 
and Visualization Renato Pajarola UCI-ICS 
Technical Report No. 02-01 Department of 
Information & Computer Science, University 
of California, Irvine January 2002
Röttger, S. Wolfgang Heidrich, Philipp Slusallek, 
and 
Hans-Peter 
Seidel, 
1997. 
Real-Time 
Generation of Continuous Levels of Detail for 
Height Fields. Technical Report, Universitat 
Erlangen-Nurnberg.
Tomas 
Möller, 
Ben 
Trumbore. 
1997. 
Fast, 
Minimum Storage Ray-Triangle Intersection, 
journal of graphics tools 2(1):21-28 
