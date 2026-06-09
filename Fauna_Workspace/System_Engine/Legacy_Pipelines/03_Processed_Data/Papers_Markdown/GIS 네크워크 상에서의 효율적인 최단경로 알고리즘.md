--- 
source: GIS 네크워크 상에서의 효율적인 최단경로 알고리즘.pdf
--- 

GIS 네트워크 상에서의 효율적인 최단경로 알고리즘
(Efficient Shortest Path Algorithms on a Network in GIS)
이 신 준 1      양 성 봉 2
(Shin-Jun Lee)   (Sung-Bong Yang)
요 약
최단경로탐색은 GIS(Geographic Information System)의 네트워크분석에서 가장 기본적인 기능으로서, 주어진 시작노드에
서 목표노드까지의 최소비용을 갖는 경로를 찾아준다. 여기서, 네트워크란 노드(node)와 두 노드를 연결하는 링크(link)들의 집합이
며, 각 링크에 비용(cost)이 부가되어진다. GIS에서 네트워크의 대표적인 예로써 도로망, 통신망 등을 들 수 있다. 본 논문에서는 
두 지점간의 최단경로를 탐색하는 4가지 알고리즘들을 제시하고자 한다. 제시된 알고리즘들은 네트워크에서 링크의 비용뿐만 아니
라, 추가적인 요소로 노드의 좌표를 필요로 한다. 제시된 알고리즘들의 특징은 노드의 좌표 정보를 이용함으로써 시작노드에서 목표
노드까지의 방향성을 이용하며, 내부적으로 탐색과정의 매 진행 상태에서의 경로트리(path tree)를 유지한다. 이 경로트리를 이용하
여 매 단계마다 이전 단계의 경로를 향상시켜가며, 최단경로를 찾는다. 제시된 알고리즘들은 탐색공간을 줄이기 위해 현재 최단경로 
비용을 이용하여 탐색한다. 본 논문에서 제시된 최단경로 알고리즘들은 크게 두 부류로 나누어진다. 하나는 단방향 탐색방법(1-way 
search method)이고, 다른 하나는 양방향 탐색방법(2-way search method)이다. 단방향 탐색방법으로는 단방향 깊이우선탐색 후 깊이
우선탐색 알고리즘(1-way search by DFS-DFS)과 단방향 깊이우선탐색 후 너비우선탐색 알고리즘(1-way search by DFS-BFS)이 있고, 
양방향 탐색방법으로는 양방향 깊이우선탐색 후 깊이우선탐색 알고리즘(2-way search by DFS-DFS)과 양방향 깊이우선탐색 후 너비우
선탐색 알고리즘(2-way search by DFS-BFS)이 있다. 본 논문에서는 제시된 알고리즘들의 성능을 각각 비교하였고, Dijkstra의 알고
리즘과도 비교하였다. 양방향 깊이우선탐색 후 너비우선탐색 알고리즘(2-way search by DFS-BFS)이 일반적으로 제일 좋은 성능을 보
여 주었다.
주요어: 최단경로탐색, 지리정보시스템, 네트워크분석, 좌표 정보, 깊이우선탐색, 너비우선탐색
Abstract  Finding a shortest route from a point to another is one of the basic functions provided in the network analysis 
of a geographic information system(GIS). A network in GIS consists of the set of nodes and the set of links. A link 
connects two nodes and is assigned a positive number called the weight (or cost) of the link. There are many examples for 
geographical networks such as streets, highways, railways, communication lines, electric lines, pipelines, rivers, etc. In 
this paper, we present four efficient algorithms for finding a shortest path in a network. Each algorithm utilizes the 
coordinates of nodes to reduce the search space and keeps a tree-like data structure, called a path tree, to find a better 
route than the path found in the previous step of the algorithm. Our algorithms  can be classified into two types depending 
on the search directions used in the algorithms: one-way search and two-way search methods. Each search method can be 
further divided into two methods depending on whether the depth-first search(DFS) or the breadth-first search(BFS) is used. 
Overall, we have four methods: one-way DFS-DFS, one-way DFS-BFS, two-way DFS-DFS, and two-way DFS-BFS. Each method has been 
compared with each other along with Dijkstra's algorithm. The experimental results have shown that two-way DFS-BFS 
outperformed others in almost all the cases.
Key words: Shortest path, Geographic Information System, Network analysis, Coordinates, Depth first search, Breadth first 
search
ꠏꠏꠏꠏꠏꠏꠏꠏꠏꠏꠏꠏꠏꠏꠏꠏꠏꠏꠏꠏꠏꠏꠏꠏꠏꠏꠏꠏꠏꠏꠏꠏꠏꠏꠏꠏꠏꠏꠏꠏꠏ
1 연세대학교 컴퓨터과학과, shinjun@mythos.yonsei.ac.kr
2 연세대학교 컴퓨터과학과 조교수, yang@mythos.yonsei.ac.kr


1. 서론
  최단경로탐색(shortest path search)은 지리정보시스템(GIS: Geographic 
Information System)의 네트워크 분석(network analysis)에서 기본적인 기
능이다. GIS란 컴퓨터를 기반으로, 지리적 데이터 조작을 위해 입력, 관리, 
조작과 분석, 출력의 기능들을 제공하는 시스템이다. 대부분의 GIS에서는 
자료 관리를 위해서 DBMS(Database Management System)를 사용한다. 그리
고, DBMS에 의해 저장되는 데이터로는 공간데이터(spatial data)와 비공간
데이터(non-spatial data)가 있다. GIS에서는 주어진 데이터에 대해서, 검
색과 분석 기능이 제공되는데 예를 들면, 개체의 위치를 찾는다든지, 두 개
체간의 관계에서, 두 도시가 도로상으로 연결되어 있는지, 또는 두 도시간
의 최단경로가 어떻게 되는지 등에 대한 분석 기능들이 제공된다. GIS에서 
제공되는 주요한 공간데이터 분석 기능 중 하나가 네트워크 분석이다[1,4].
  GIS에서는 저장되는 공간데이터에서 대부분의 공간적 관계를 네트워크로 
표현한다. 네트워크의 예로는 도로망, 상하수도망, 통신망 등이 있다. 이러
한 것들을 네트워크로 모델링하여 검색과 분석을 할 수 있다. 네트워크 분
석에서 제공되는 기능들로는 경로탐색(path finding), 자원할당(resource 
allocation), 적지선정(location allocation), 연결성(connectivity), 네트
워크유량문제(network flow problem) 등이 있다[3]. 본 논문에서는 GIS에서 
제공되는 네트워크 분석 기능 중에서 최단경로탐색 문제에 대해서 살펴보
고, 새로운 최단경로 알고리즘들을 제시한다.
  네트워크 상에서 최단경로를 찾는 알고리즘 중에서, 일반적으로 널리 알
려진 알고리즘이 Dijkstra 알고리즘이다. Dijkstra 알고리즘은 네트워크에
서 단일 시작노드에서 모든 다른 노드간의 최단경로를 찾아준다. Dijkstra 
알고리즘의 time complexity는 사용되는 자료구조에 따라 O(M log N) 과 
O(N 2) 이다[6]. 기존의 최단경로 알고리즘인 경우에는, 수행 형태가 너비우
선탐색(BFS: Breadth First Search)이다. 따라서, 수행이 이루어지는 네트
워크의 규모가 상당히 크고, 시작노드와 목표노드의 거리가 먼 상황에서 최
단경로탐색은 상당한 시간을 요구하게 된다.
  본 논문에서 제안된 알고리즘은 처음 경로 설정 시, 노드의 좌표들을 이
용한 방향성을 갖는 깊이우선탐색(DFS: Depth First Search)을 수행한다. 
그후에 이전 경로보다 나은 경로가 있는지 알아보기 위해 경로탐색을 반복 
수행한다. 이렇게 반복 수행을 하고 나서, 더 나은 경로가 발견되지 않는다
면, 최단경로를 얻게 된다. 그래서, 본 논문에서 제시하는 알고리즘들은 목
표노드까지의 탐색 경로가 점점 나아지는 방식으로 수행이 된다.
  본 논문에서는 탐색수행방향에 따라 또 탐색방법(DFS 또는 BFS)에 따라 
네가지 알고리즘을 제안한다: 단방향 깊이우선탐색 후 깊이우선탐색 알고리
즘(1-way search by DFS-DFS: 1DDS)과 단방향 깊이우선탐색 후 너비우선탐
색 알고리즘(1-way search by DFS-BFS: 1DBS)이 있고, 양방향 탐색방법으로
는 양방향 깊이우선탐색 후 깊이우선탐색 알고리즘(2-way search by 
DFS-DFS: 2DDS)과 양방향 깊이우선탐색 후 너비우선탐색 알고리즘(2-way 
search by DFS-BFS: 2DBS). 제안된 알고리즘들은 Dijkstra의 알고리즘과 비
교되었으며 그 중에서 2DBS가 대부분의 경우 우수함을 보였다.
  본 논문은 2장에서 제안하는 알고리즘들을 설명하고, 3장에서는 실험결과
를 보여준다.
2. 최단경로 알고리즘
2.1 네트워크 정의
  네트워크란 노드(node)와 링크(link)의 집합이며, 각 노드나 링크에 수치
요소(parameter)가 부가되어진다. 링크의 양끝에는 두 노드가 연결된다. 본 
논문에서 사용하는 네트워크는
G = (V,E,W, X,Y) 로 표현한다.
  여기서, V 는 G 에 있는 노드의 집합이고, E 는 G 에 있는 링크의 집합
이다. W는 G 에 있는 링크들의 수치요소인, 비용(cost)의 집합이다. X
는 G 에 있는 노드들의 X 좌표의 집합이고, Y 는 G 에 있는 노드들의 Y
좌표의 집합이다. G 에 있는 노드의 개수는 N 으로 하고 링크의 개수는 
M 으로 한다. 즉, |V| =N, |E| =M이다.
2.2 좌표를 이용한 DFS방법
  좌표를 이용한 DFS 수행 시, 현재 노드가 A , 목표노드가 Z 이고, A 의 
인접 노드들이 
B1,B 2,
,Bk
 , k
1 일 때, 다음 방문하게되는 노드 
Bnext 는 A 의 인접 노드들 중에서 Z 까지의 Euclidean 거리가 최소가 되는 
노드이다. 즉, de(B next,Z ) 값은 de(B i,Z) , 1
i
k , 값들 중 최소이다. 
여기서, de(I, J) 는 노드 I 와 노드 J 의 Euclidean 거리로de(I, J)
= √
(xI −xJ)2 + (y I −yJ )2 이고, I 의 좌표는 (x I, y I) 이고, J 의 좌표는 
(xJ,y J) 이다.
2.3 새로운 최단경로 알고리즘
  본 논문에서 제안하는 알고리즘들은 단방향 탐색방법과 양방향 탐색방법
으로 나눌 수 있다. 단방향 탐색방법은 시작노드에서 목표노드 방향으로만 
탐색을 수행하는 방법이다. 그리고, 양방향 탐색방법은 시작노드와 목표노
드 양쪽에서 반대편 노드로 탐색을 동시에 수행하는 방법이다.
  제안하는 4가지 알고리즘은 다음과 같다.
2.3.1 1DDS
  1DDS 알고리즘은 다음과 같다.
  초기 counter 값은 0이다.
 1) 좌표를 이용한 DFS로 시작노드에서 목표노드로 stack을 이용하여 탐색
 2) 목표노드 도달 시, counter 1증가, min_path_distance 설정
 3) 새로운 경로를, 좌표를 이용한 DFS를 통해서 목표노드까지 stack을 이
용하여 탐색하며, 탐색은 min_path_distance 범위 안에서 이루어진다.
 4) 목표노드 도달 시 즉, 목표노드까지 더 나은 새로운 경로 발견 시, 
counter 1증가, min_path_distance 갱신
 5) stack이 비어있지 않고 counter가 반복 회수보다 작으면 3)으로
 6) 목표노드에서 시작노드까지 거슬러서, 방문한 노드들을 가져옴으로 최
단경로를 구한다. 그리고, 종료한다.
  DFS 수행을 위해, 1개의 stack을 사용한다. 입력은 시작노드와 목표노드
이다. 결과는 s_path로 최단경로 상의 방문노드들을 저장하는 stack이다. 
tree는 (노드, 거리, 이전 노드)의 list로 된 자료구조이다. push() 함수는 
stack의 top에 노드를 push한다. pop() 함수는 stack의 top 노드를 꺼내온
다. 여기서 사용하는 stack은 원하는 노드를 삭제할 수 있고, bottom에도 
삽입을 할 수 있다고 전제한다. dist()함수는 tree에 있는 노드의 거리를 
가져온다. counter는 최단경로의 갱신 반복 회수를 지정한다. v_node는 현
재 방문 노드를 의미한다. min_path_distance는 시작노드에서 목표노드까지
의 현재까지 알고리즘이 찾은 최단경로의 거리를 의미하고, 초기 경로가 설
정되어 있지 않은 상태에서는 수치의 최대값을 갖는다. 인접 링크 buffer는 
인접 링크들을 저장하는 stack이다. adj_link는 하나의 인접 링크를 의미한
다. cost() 함수는 링크의 비용을 가져온다. s_path는 최단경로의 노드들을 
저장하는 stack으로, 최종의 결과인 최단경로를 갖게 된다. pre_node는 이
전노드를 저장한다. c_node는 최단경로를 얻기 위해서 사용하는 임시노드이
다. get_pre()함수는 tree에서 한 노드의 이전노드를 가져온다. 상세한 
1DDS 알고리즘은 <부록 1>을 참조한다.
2.3.2 1DBS
  1DBS 알고리즘은 다음과 같다.
  초기 counter 값은 0이다.
 1) 좌표를 이용한 DFS로 시작노드에서 목표노드로 queue를 이용하여 탐색
 2) 목표노드 도달 시, counter 1증가, min_path_distance 설정
 3) 새로운 경로를, BFS를 통해서 목표노드까지 queue들 이용하여 탐색하
며, 탐색은 min_path_distance 범위 안에서 이루어진다.
 4) 목표노드 도달 시 즉, 목표노드까지 더 나은 새로운 경로 발견 시, 
counter 1증가, min_path_distance 갱신
 5) queue가 비어있지 않고 counter가 반복 회수보다 작으면 3)으로 
 6) 목표노드에서 시작노드까지 거슬러서, 방문한 노드들을 가져옴으로 최
단경로를 구한다. 그리고, 종료한다.
  1DBS는 1DDS와 비슷하게 수행되는데, 다른 점은 queue를 사용하여 BFS로 
탐색을 한다.  BFS 수행을 위해, 1개의 queue를 사용한다. 여기서 사용하는 
queue는 노드를 front로도 집어넣을 수 있음을 전제한다. 초기 경로 설정 
시, queue를 이용하여 DFS를 수행하는 데, 방법은 목표노드와의 Euclidean 


거리가 가까운 인접노드를 queue의 front에 집어넣음으로 수행된다.
  입력은 시작노드와 목표노드이다. 결과는 s_path로 최단경로 상의 방문노
드들을 저장하는 stack이다. addq()함수는 queue의 rear에 노드를 삽입한
다. deleteq()함수는 queue의 front의 노드를 꺼내온다. push()함수, pop()
함수, dist()함수, cost()함수, get_pre()함수는 1DDS에서와 같은 기능을 
갖는다. 그리고, tree, v_node, min_path_distance, 인접 링크 buffer, 
adj_link, pre_node, c_node도 1DDS에서와 같은 의미를 갖는다. 상세한 
1DBS 알고리즘은 <부록 2>을 참조한다.
2.3.3 2DDS
  2DDS 알고리즘은 다음과 같다.
  초기 counter 값은 0이다.
 1) 좌표를 이용한 DFS로 시작노드에서 목표노드로 목표노드에서 시작노드
로 stack1, stack2를 이용하여 번갈아 가며 탐색
 2) 중간노드 발견 시, counter 1증가, min_path1, min_path2, min_node 설
정
 3) 새로운 경로를, 좌표를 이용한 DFS로 하나는 목표노드로 또 하나는 시
작노드로 stack1, stack2를 이용하여 번갈아 가며 탐색하며, 탐색은 
min_path1, min_path2 범위 안에서 이루어진다.
 4) 새로운 중간노드 발견 시 즉, 더 나은 새로운 경로 발견 시, counter 1
증가, min_path1, min_path2, min_node 갱신
 5) stack1과 stack2 모두 비어있지 않고 counter가 반복 회수보다 작으면 
3)으로 간다.
 6) 중간노드에서 시작노드와 목표노드까지 거슬러서, 방문한 노드들을 가
져옴으로 최단경로를 구한다. 그리고, 종료한다.
  양방향의 DFS 수행을 위해, 2개의 stack을 사용한다. 입력은 시작노드와 
목표노드이다. 결과는 s_path로 최단경로 상의 방문노드들을 저장하는 
stack이다. 양방향 탐색을 위해서 2개의 stack과 2개의 tree를 사용한다. 
즉, stack1, stack2, tree1, tree2를 사용한다. min_path1은 시작노드에서 
중간노드까지의 현재까지 알고리즘이 찾은 탐색 경로의 거리를 의미하고, 
초기 경로가 설정되어 있지 않은 상태에서는 수치의 최대값을 갖는다. 
min_path2는 목표노드에서 중간노드까지의 현재까지 알고리즘이 찾은 탐색 
경로의 거리를 의미하고, 초기 경로가 설정되어 있지 않은 상태에서는 수치
의 최대값을 갖는다. 양방향 탐색 중에 중간에서 경로가 설정되면, 그 중간
의 위치에 있는 노드를 mid_node로 설정한다. adds()함수는 stack의 bottom
에 노드를 삽입한다. push()함수, pop()함수, dist()함수, cost()함수, 
get_pre()함수는 1DDS에서와 같은 기능을 갖는다. 그리고, v_node, 인접 링
크 buffer, adj_link, pre_node, c_node는 1DDS에서와 같은 의미를 갖는다. 
상세한 2DDS 알고리즘은 <부록 3>을 참조한다.
2.3.4 2DBS
  2DBS 알고리즘은 다음과 같다.
  초기 counter 값은 0이다.
1) 좌표를 이용한 DFS로 시작노드에서 목표노드로 목표노드에서 시작노드로 
queue1, queue2를 이용하여 번갈아 가며 탐색
2) 중간노드 발견 시, counter 1증가, min_path1, min_path2, min_node 설
정
3) 새로운 경로를, BFS로 하나는 목표노드로 또 하나는 시작노드로 queue1, 
queue2를 이용하여 번갈아 가며 탐색하며, 탐색은 min_path1, 
min_path2 범위 안에서 이루어진다.
4) 새로운 중간노드 발견 시 즉, 더 나은 새로운 경로 발견 시, counter 1
증가, min_path1, min_path2, min_node 갱신
5) queue1과 queue2 모두 비어있지 않고 counter가 반복 회수보다 작으면 
3)으로 간다.
6) 중간노드에서 시작노드와 목표노드까지 거슬러서, 방문한 노드들을 가져
옴으로 최단경로를 구한다. 그리고, 종료한다.
  양방향의 BFS 수행을 위해, 2개의 queue를 사용한다. 입력은 시작노드와 
목표노드이다. 결과는 s_path로 최단경로 상의 방문노드들을 저장하는 
stack이다. 양방향 탐색을 위해서 2개의 queue와 2개의 tree를 사용한다. 
즉, queue1, queue2, tree1, tree2를 사용한다. min_path1, min_path2, 
mid_node는 2DDS에서와 같은 의미를 갖는다. addq()함수, deleteq()함수는 
1DBS에서와 같은 기능을 갖는다. adds()함수는 2DDS에서와 같은 기능을 갖
는다. push()함수, pop()함수, dist()함수, cost()함수, get_pre()함수는 
1DDS에서와 같은 기능을 갖는다. 그리고, v_node, 인접 링크 buffer, 
adj_link, pre_node, c_node는 1DDS에서와 같은 의미를 갖는다. 상세한 
2DBS 알고리즘은 <부록 4>을 참조한다.
2.4 새로운 알고리즘들의 특성
  1DDS와 2DDS에서는 좌표를 이용한 DFS 이후, 계속해서 좌표를 이용한 DFS
를 수행하므로 stack을 사용한다. 1DDS는 1개의 stack을 2DDS는 2개의 
stack을 사용한다. 1DBS와 2DBS에서는 좌표를 이용한 BFS 이후, 좌표를 이
용한 BFS를 수행하므로 queue을 사용한다. 1DBS는 1개의 queue을 2DBS는 2
개의 queue을 사용한다.
  DFS나 BFS로 경로탐색 시, stack이나 queue가 방문할 노드들을 저장하게 
된다. 그래서, 방문할 노드가 하나도 존재하지 않으면, 탐색은 끝나게 되
고, 결과로 최단경로를 구하게 된다.
  탐색 과정에서 (key, value, pre_node)의 list인 tree라는 자료구조를 사
용한다. 그래서, tree는 key가 주어지면, 그에 해당하는 value와 pre_node
를 반환한다.
  tree가 하는 역할은 탐색 과정 중에, 현재 상태에서 탐색되어진 노드들의 
최단경로 거리를 갖게된다. key는 노드를 value는 거리를 pre_node는 이전
노드를 저장한다. 그래서, 탐색이 진행되어가다 더 나은 경로가 발견이 되
면, 탐색 노드의 거리가 갱신이 된다. 그리고, 탐색 중에 현재 tree에 저장
되어 있는 거리보다 큰 거리의 경로탐색 시에는 그 경로를 무시하고, 그 경
로의 노드는 stack이나 queue에 집어넣지 않고 그 경로의 탐색을 중지한다.
  즉, tree의 확장은 탐색된 노드가 tree에 없을 때, 그 노드와 거리를 
(key, value, pre_node)의 형태로 집어넣는다. 그리고, 탐색된 노드가 tree
에 있을 때는, 그 노드의 거리가 tree에 저장되어 있는 거리보다 작을 때 
갱신이 이루어진다.
  그리고, 노드의 거리는 tree에 있는 노드의 거리하고 비교가 되지만, 현
재 최단경로의 거리와도 비교가 이루어진다. 현재 최단경로의 거리는, 초기 
경로 설정 시, 좌표를 이용한 DFS를 수행하는데, 이때는 알 수가 없으므로 
비교가 이루어지지 않고, 탐색이 목표노드까지 처음에 도달해서 초기 경로
가 설정이 되면 현재 최단경로를 알 수 있으므로, 이후의 경로탐색 시, 각 
노드의 거리가 현재 최단경로의 거리보다 작은 범위에서만 탐색이 이루어진
다. 탐색이 이루어지다가 목표노드까지의 더 나은 경로가 발견이 돼서, 현
재 최단경로의 거리가 갱신이 이루어진 후에도, 경로탐색 시에는 각 노드의 
거리가 현재 최단경로의 거리보다 작은 범위에서만 탐색이 이루어진다. 이
렇게 하므로, 네트워크의 탐색 크기를 줄이게 된다.
  초기 경로탐색 시, 목표노드 방향으로만 DFS가 이루어지므로, 기존 알고
리즘에 비해서, 초기 경로 설정 시간은 무척 빠르다. 초기 경로 설정 이후
에는 계속해서 새로운 경로탐색이 일어나게 되는데, 현재 최단경로 거리를 
이용하고, tree에 탐색 노드들의 거리를 저장하므로 네트워크의 탐색 크기
를 줄이고 또한 수행시간을 줄이게 된다. 결국 빠른 시간 안에 최단경로를 
찾아주게 된다. 탐색이 끝난 후에는 시작노드와 목표노드간에 최단경로를 
구하게 된다. 1DDS와 1DBS에서는 탐색이 1방향으로만 이루어지므로 1개의 
tree를 사용하고, 2DDS와 2DBS에서는 탐색이 2방향에서 이루어지므로 2개의 
tree가 사용된다. 2방향 탐색에서는 2개의 stack이나 queue와 함께 2개의 
tree를 사용하는데, 탐색은 한번은 시작노드에서 목표노드 방향으로, 또 한
번은 목표노드에서 시작노드 방향으로 번갈아 가면서 탐색이 수행된다.
  탐색은 DFS에서 방향성을 부여하기 위해서, 노드의 좌표를 사용한다. 그
래서, 현재 방문 노드에서 인접 노드들을 구하고, 그 인접 노드들과 목표노
드간의 거리를 계산해서 작은 수치를 갖는 노드를 다음 방문 노드로 만든
다. BFS에서는 초기 경로 설정까지만, 방향성을 갖고 DFS를 수행하고, 경로
설정 이후에는 방향성 없이 DFS를 수행한다.
  4가지 알고리즘에서 필요한 자료구조는 1DDS에서 stack, tree, 1DBS에서 
queue, tree, 2DDS에서 stack1, stack2, tree1, tree2, 2DBS에서 queue1, 
queue2, tree1, tree2이다.
2.5 Counter
  경로탐색은 목표노드 방향으로 탐색이 이루어지고, 목표노드에 매번 도달
할 때마다 그 회수를 계산할 수 있다. 초기 경로 설정 시에, 회수가 1이 되
고, 그 이후에 더 나은 새로운 경로 발견 시, 즉, 또 다시 목표노드까지 탐
색이 도달하면 회수가 1증가된다. 계속해서 최단경로의 갱신이 이루어질 때


마다 회수는 1씩 증가하게 되고, 더 이상 회수의 증가가 없이 탐색이 끝나
게 되면, 결국 시작노드에서 목표노드까지의 최단경로를 얻게 된다. 
Dijkstra 알고리즘인 경우에, 단 하나의 최단경로를 얻는 것은 한참의 수행 
시간이 걸린 이후이다.
  본 논문에서 제시한 4가지 알고리즘의 경우에는 두 노드간의 경로는 회수
가 증가할수록 더 나은 경로이지만 수행 시간은 같이 증가하게 된다. 따라
서, 사용자가 최적의 경로는 아니지만 빠른 시간 안에 최적의 경로에 근접
한 경로를 찾고자 한다면, 경로탐색 회수를 낮출 수 있다. 그렇지 않고, 시
간에 상관없이 최적의 경로를 원한다면 경로탐색 회수의 증가가 없을 때까
지 수행시키면 된다.
  입력 네트워크의 측면을 고려할 때, 모든 링크의 비용이 각 링크의 크기
에 비례하는 네트워크라면, counter 값이 작을 때, 탐색 경로가 최단경로에 
상당히 근접하게 된다. 그리고, 실세계에서의 네트워크도 대부분의 지리적 
거리가 비용으로 사용되는데, 이러한 경우에 본 논문에서 제시한 알고리즘
들은 상당한 효율성을 갖게 된다. 그렇지 않은 네트워크에서는, counter 값
이 작을 때, 탐색 경로가 최단경로에 비해 차이가 좀 있더라도, 탐색 수행 
회수를 늘려 나감으로 일정의 시간 안에서의 탐색을 수행할 수 있고, 최적
에 가까운 경로를 얻을 수 있다. 탐색 수행 회수를 counter라 두고, 원하는 
탐색 반복 회수만큼 수행이 이루어진다.
3. 실험 결과
  본 논문에서 제시한 알고리즘들은 Sun의 Ultra Sparc1 워크스테이션에서 
수행이 되었고, Laser Scan사의 Gothic 3.0 System상에서 lull code로 구현
하였다[2,5]. O(N 2)  Dijkstra 알고리즘 수행 시간이 너무 오래 걸리는 경
우에는 비교를 하지 않았고, O(M log N)  Dijkstra 알고리즘 즉, priority 
queue를 이용한 Priority First Search(PFS)의 방법과만 비교하였다.
  사용한 네트워크는 노드가 1000개이고 링크가 1260개이다. 링크의 비용은 
무작위로 1에서 20까지의 정수 값을 갖는다. 최단경로탐색 수행 시간의 단
위는 초이다. 표 1에서는 최단경로를 구할 때까지의 각각의 성능 비교이다. 
Dist는 최단경로의 거리이다. 표 2에서는 네트워크의 끝점간에서 최단경로
탐색 수행 결과를 보여준다. 표 3에서 표6까지는 각각의 경우를 counter에 
따른 결과를 보여준다. count 또는 c는 counter의 값을 의미한다. 수행 시
간들을 초 단위로 나타내었고 수행 결과, 탐색된 경로의 거리를 괄호 안에 
나타내었다.
표 2 The result of searches in many cases
Dist
Dijkstra
PFS 1DDS 1DBS 2DDS 2DBS
1
52
18.36
0.45
0.69
0.47
0.58
0.50
2
62
29.65
2.59
3.12
2.93
2.91
1.83
3
24
39.43
0.58
0.62
0.68
0.37
0.36
4
76
1:31.19
1.54
1.44
1.44
1.00
1.04
5
126
-
2.40
2.98
2.90
3.94
3.93
6
167
-
14.95 32.30
32.27
6.60
6.54
7
137
-
9.14
9.89
9.84
25.18
25.11
8
146
-
10.66 20.94
20.65
6.03
6.03
9
133
-
7.92
27.81
27.80
19.96
17.06
10
178
-
9.07
26.26
26.29
23.06
22.77
표 3 The result of searches between end points
Dist
PFS
1DDS
1DBS
2DDS
2DBS
1
94
9.61
5.33
5.43
2.00
1.99
2
115
12.65
40.08
40.04
4.21
4.25
3
249
4.24
7.15
7.13
2.97
2.98
4
279
23.15
7:46.71
57.98
4:25.06
23.19
표 4 The result of search with counter <1>
count
PFS
1DDS
1DBS
2DDS
2DBS
MAX 9.61(94)
5.33(94)
5.43(94)
2.00(94)
1.99(94)
1
0.41(94)
0.43(94)
0.44(94)
0.41(94)
2
5.33(94)
5.43(94)
2.00(94)
1.99(94)
  표 3의 경우에는 끝점간의 경로탐색에서 초기 경로가 최적이 된 경우로, 
count가 1일 때, 최단경로를 구했고, 이 후는 나머지 공간 탐색에 걸린 시
간이다.
표 5 The result of search with counter <2>
count
PFS
1DDS
1DBS
2DDS
2DBS
MAX 4.24(249) 7.15(249) 7.13(249) 2.97(249) 2.98(249)
1
0.29(253) 0.29(253) 0.29(251) 0.28(251)
2
1.79(249) 1.70(249) 0.48(249) 0.48(249)
3
7.15(249) 7.13(249) 2.97(249) 2.98(249)
  표 4는 count가 2일 때, 최적의 경로를 얻은 경우이다. 초기 경로 설정에
서 최적에 근접한 값을 가져왔다.
표 6 The result of search with counter <3>
c
PFS
1DDS
1DBS
2DDS
2DBS
MA
X
12.65
(115) 40.08(115) 40.04(115)
4.21(115)
4.25(115)
1
0.59(404)
0.61(404)
0.50(222)
0.50(222)
2
11.38(363) 11.18(363)
0.51(222)
0.50(222)
3
22.77(305) 22.56(305)
0.56(219)
0.55(219)
4
27.18(272) 27.28(272)
0.67(199)
0.65(199)
5
28.84(222) 28.84(222)
1.06(189)
1.11(189)
6
32.88(199) 32.86(199)
2.83(182)
2.93(182)
7
37.01(189) 36.98(189)
3.19(180)
3.26(180)
8
39.06(182) 39.07(182)
3.63(169)
3.54(169)
9
39.52(169) 39.27(169)
4.13(115)
4.09(115)
10
39.86(115) 39.95(115)
4.21(115)
4.25(115)
11
40.08(115) 40.04(115)
  표 5는 단방향 방법의 수행 결과가 좋지 못한 경우로, 초기 경로 설정시 
단방향 방법은 최적의 거리에 4배나 되는 경로를 구했고, 양방향 방법은 최
적의 거리에 2배 정도 되는 경로를 구했다. 양방향 방법의 수행 결과는 다
른 방법들에 비해서 아주 좋은 결과를 가져왔다.
표 7 The result of search with counter <4>
c
PFS
1DDS
1DBS
2DDS
2DBS
MA
X
6.60
(91)
9.59(91)
9.59(91)
3.86(91)
3.86(91)
1
0.20(224)
0.20(224)
0.20(218)
0.21(218)
2
1.32(194)
1.32(194)
0.27(171)
0.27(171)
3
4.59(141)
4.59(141)
0.53(165)
0.54(165)
4
7.85(119)
7.85(119)
0.90(153)
0.90(153)
5
9.02(91)
9.05(91)
0.93(141)
0.93(141)
6
9.59(91)
9.59(91)
1.54(128)
1.55(128)
7
1.61(125)
1.61(125)
8
1.84(104)
1.83(104)
9
2.08(103)
2.08(103)
10
2.68(102)
2.69(102)
11
3.00(101)
3.00(101)
12
3.43(91)
3.40(91)
13
3.86(91)
3.86(91)
표 6의 경우는 표 5와 비슷한 경우로, 양방향 방법이 다른 방법들에 비해서 
나은 결과를 가져왔다. 단방향 방법의 초기 경로 설정은 최적의 2배 이상이 
되는 경로를 구했고, 양방향 방법의 초기 경로 설정도 최적의 2배 이상이 
되는 경로를 가져왔다.


  위 결과들에서 일반적으로 1DDS와 1DBS가 비슷한 수행 시간을, 2DDS와 
2DBS가 비슷한 수행 시간을 가짐을 볼 수 있다. 그렇지만, 표 2의 4번째 경
우처럼, 1DDS가 1DBS에 비해, 2DDS가 2DBS에 비해 좋지 못한 경우도 볼 수 
있어서, 일반적으로 DBS가 DDS에 비해 비슷하거나 나은 결과를 가져왔다.
4. 결론 및 향후 연구방향
  본 논문에서 새로운 4가지의 최단경로 알고리즘을 제안하였다. 초기 경로 
설정은 DFS로 빠른 수행 시간 안에 이루어졌고, 최단경로탐색은 일정 시간
이 걸린 후에 얻을 수 있었다.
  제안된 알고리즘들은 Dijkstra 알고리즘보다는 나은 결과를 가져왔지만, 
PFS보다 항상 나은 결과를 가져오지는 못했다. 일반적으로 네트워크가 
triangle inequality 원칙이 지켜지는 경우에는 PFS보다 나은 결과를 보였
다. DBS방법이 DDS방법보다 나은 결과를 보였고, 양방향 방법이 단방향 방
법보다 좋은 결과를 가져왔다. 앞으로 좌표를 이용한 최단경로탐색의 성능
을 향상시킬 수 있는 새로운 방법에 대한 연구가 이루어 질 것이다.
 
참고 문헌
[1] 박기석, GIS 지리정보시스팀, 동서, 1995.
[2] Karen Sutherland, Gothic Concepts Tranining Course, Laser-Scan 
LTD, 1995.
[3] Michael F. Goodchild, "SPATIAL ANALYSIS and GIS," 1997 ESRI USER 
CONFERENCE Pre-Conference Seminar, 1997.
[4] Michael F. Worsboys, GIS: A Computing Perspective, Taylor & 
Francis, 1995.
[5] S. G. Hancock, Writing and developing applications using GOTHIC 
ADE, Laser-Scan LTD, 1995.
[6] Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, 
Introduction to Algorithms, McGraw-Hill, 1990.
부록
<부록 1> 1DDS(1-way search by DFS-DFS)
(1) push(stack, 시작노드);
(2) tree에 (시작노드, 0, NULL)을 첨가
(3) stack이 비거나 탐색 반복 회수가 counter 값과 같으면 
(22)로 간다.
(4) v_node := pop(stack);
(5) dist(tree, v_node)가 min_path_distance보다 크거나 같으면 
(3)으로 간다.
(6) v_node에 인접한 링크들을 인접 링크 buffer에 삽입한다.
(7) 인접 링크 buffer가 비면 (21)으로 간다.
(8) adj_link := pop(buffer);
(9) dist(tree, v_node) + cost(adj_link)가
 min_path_distance보다 크거나 같으면 (7)로 간다.
(10) adj_node := adj_link에 연결된 인접 노드;
(11) adj_node가 tree에 있으면 (16)으로 간다.
(12) tree에 
(adj_node, 
dist(tree, 
v_node) 
+ 
cost(adj_link), 
v_node)를 첨가한다.
(13) adj_node == 목표노드이면 counter를 1증가시키고,
  min_path_distance := dist(tree, v_node) + cost(adj_link); 수
행. 그리고, (7)로 간다.
(14) push(stack, adj_node);
(15) adj_node에서 목표노드까지의 Euclidean 거리를 계산하고, 
v_node의 인접 노드들 중 목표노드까지의 Euclidean 거리가 
최소이면 best_adj_node는 adj_node를 갖는다. 그리고, (7)로 
간다.
(16) dist(tree, v_node) + cost(adj_link)가 dist(tree, adj_node)
보다 크거나 같으면 (7)로 간다.
(17) adj_node를 tree에서 찾아 (adj_node, dist(tree, v_node) + 
cost(adj_link), v_node)로 갱신한다.
(18) adj_node == 목표노드이면 counter를 1증가시키고,
  min_path_distance := dist(tree, v_node) + cost(adj_link); 수
행. 그리고, (7)로 간다.
(19) push(stack, adj_node);
(20) adj_node에서 목표노드까지의 Euclidean 거리를 계산하고, 
v_node의 인접 노드들 중 목표노드까지의 Euclidean 거리가 
최소이면 best_adj_node는 adj_node를 갖는다. 그리고, (7)로 
간다.
(21) stack에서 
best_adj_node를 
delete하고, 
push(stack, 
best_adj_node); 수행, (3)으로 간다.
(22) c_node := 목표노드;
(23) push(s_path, c_node);
(24) c_node == 시작노드이면 (28)로 간다.
(25) pre_node := get_pre(tree, c_node);
(26) push(s_path, pre_node);
(27) c_node := pre_node; 수행, (24)로 간다.
(28) s_path에 저장된 노드들을 하나씩 pop함으로 최단경로 상
의 방문 노드들을 알 수 있다. 종료한다.


<부록 2> 1DBS(1-way search by DFS-BFS)
(1) addq(queue, 시작노드);
(2) tree에 (시작노드, 0, NULL)을 첨가
(3) queue가 비거나 탐색 반복 회수가 counter 값과 같으면 
(22)로 간다.
(4) v_node := deleteq(queue);
(5) dist(tree, v_node)가 min_path_distance보다 크거나 같으면 
(3)으로 간다.
(6) v_node에 인접한 링크들을 인접 링크 buffer에 삽입한다.
(7) 인접 링크 buffer가 비면 (21)으로 간다.
(8) adj_link := pop(buffer);
(9) dist(tree, v_node) + cost(adj_link)가
 min_path_distance보다 크거나 같으면 (7)로 간다.
(10) adj_node := adj_link에 연결된 인접 노드;
(11) adj_node가 tree에 있으면 (16)으로 간다.
(12) tree에 
(adj_node, 
dist(tree, 
v_node) 
+ 
cost(adj_link), 
v_node)를 첨가한다.
(13) adj_node == 목표노드이면 counter를 1증가시키고,
  min_path_distance := dist(tree, v_node) + cost(adj_link); 수
행, (7)로 간다.
(14) addq(queue, adj_node);
(15) adj_node에서 목표노드까지의 Euclidean 거리를 계산하
고, v_node의 인접 노드들 중 목표노드까지의 Euclidean 거
리가 최소이면 best_adj_node는 adj_node를 갖는다. 그리고, 
(7)로 간다.
(16) dist(tree, v_node) + cost(adj_link)가 dist(tree, adj_node)
보다 크거나 같으면 (7)로 간다.
(17) adj_node를 tree에서 찾아 (adj_node, dist(tree, v_node) 
+ cost(adj_link), v_node)로 갱신한다.
(18) adj_node == 목표노드이면 counter를 1증가시키고,
  min_path_distance := dist(tree, v_node) + cost(adj_link); 수
행, 그리고, (7)로 간다.
(19) addq(queue, adj_node);
(20) adj_node에서 목표노드까지의 Euclidean 거리를 계산하
고, v_node의 인접 노드들 중 목표노드까지의 Euclidean 거
리가 최소이면 best_adj_node는 adj_node를 갖는다. 그리고, 
(7)로 간다.
(21) tree에 
목표노드가 
없으면, 
queue에서 
best_adj_node를 
delete하고 queue의 front에 best_adj_node를 삽입하고 나서, 
(3)으로 간다. 그렇지 않고, tree에 목표노드가 있으면 (3)으
로 간다.
(22) c_node := 목표노드;
(23) push(s_path, c_node);
(24) c_node == 시작노드이면 (28)로 간다.
(25) pre_node := get_pre(tree, c_node);
(26) push(s_path, pre_node);
(27) c_node := pre_node; 수행, (24)로 간다.
(28) s_path에 저장된 노드들을 하나씩 pop함으로 최단경로 상
의 방문 노드들을 알 수 있다. 종료한다.


<부록 3> 2DDS(2-way search by DFS-DFS)
(1) push(stack1, 시작노드); push(stack2, 목표노드);
(2) tree1에 (시작노드, 0, NULL)을 첨가, tree2에 (목표노드, 
0, NULL)을 첨가
(3) stack1과 stack2가 모두 비거나 탐색 반복 회수가 counter 
값과 같으면 (54)로 간다.
(4) stack1이 비면, (29)로 간다.
(5) v_node := pop(stack1);
(6) dist(tree1, v_node)가 min_path1보다 크거나 같으면 (29)
로 간다.
(7) v_node에 인접한 링크들을 인접 링크 buffer에 삽입한다.
(8) 인접 링크 buffer가 비면 (28)로 간다.
(9) adj_link := pop(buffer);
(10) adj_node := adj_link에 연결된 인접 노드;
(11) adj_node가 tree2에 있으면 (21)로 간다.
(12) dist(tree1, v_node) + cost(adj_link)가
 min_path1보다 크거나 같으면 (8)로 간다.
(13) adj_node가 tree1에 없으면 (18)로 간다.
(14) dist(tree1, 
v_node) 
+ 
cost(adj_link)가 
dist(tree1, 
adj_node)보다 크거나 같으면 (8)로 간다.
(15) adj_node를 
tree1에서 
찾아 
(adj_node, 
dist(tree1, 
v_node) + cost(adj_link), v_node)로 갱신한다.
(16) push(stack1, adj_node);
(17) adj_node에서 목표노드까지의 Euclidean 거리를 계산하
고, v_node의 인접 노드들 중 목표노드까지의 Euclidean 거
리가 최소이면 best_adj_node는 adj_node를 갖는다. 그리고, 
(8)로 간다.
(18) tree1에 (adj_node, dist(tree1, v_node) + cost(adj_link), 
v_node)를 첨가한다.
(19) push(stack1, adj_node);
(20) adj_node에서 목표노드까지의 Euclidean 거리를 계산하
고, v_node의 인접 노드들 중 목표노드까지의 Euclidean 거
리가 최소이면 best_adj_node는 adj_node를 갖는다. 그리고, 
(8)로 간다.
(21) dist(tree1, 
v_node) 
+ 
cost(adj_link) 
+ 
dist(tree2, 
adj_node)가 min_path1+min_path2보다 크거나 같으면 (8)로 
간다.
(22) min_path1 := dist(tree1, v_node) + cost(adj_link); 수행, 
min_path2 
:= 
dist(tree2, 
adj_node); 
수행, 
mid_node 
:= 
adj_node; 수행.
(23) adj_node가 tree1에 없으면 (26)로 간다.
(24) adj_node를 
tree1에서 
찾아 
(adj_node, 
dist(tree1, 
v_node) + cost(adj_link), v_node)로 갱신한다.
(25) push(stack1, adj_node); 수행, (8)로 간다.
(26) tree1에 (adj_node, dist(tree1, v_node) + cost(adj_link), 
v_node)를 첨가한다.
(27) push(stack1, adj_node); 수행, (8)로 간다.
(28) stack1에서 
best_adj_node를 
delete하고 
push(stack1, 
best_adj_node); 수행한다.
(29) stack2가비면(54)로간다
<부록 3> 계속
(1) v_node에 인접한 링크들을 인접 링크 buffer에 삽입한다.
(2) 인접 링크 buffer가 비면 (53)으로 간다.
(3) adj_link := pop(buffer);
(4) adj_node := adj_link에 연결된 인접 노드;
(5) adj_node가 tree1에 있으면 (46)으로 간다.
(6) dist(tree2, v_node) + cost(adj_link)가
 min_path2보다 크거나 같으면 (33)로 간다.
(7) adj_node가 tree2에 없으면 (43)으로 간다.
(8) dist(tree2, 
v_node) 
+ 
cost(adj_link)가 
dist(tree2, 
adj_node)보다 크거나 같으면 (33)로 간다.
(9) adj_node를 tree2에서 찾아 (adj_node, dist(tree2, v_node) 
+ cost(adj_link), v_node)로 갱신한다.
(10) push(stack2, adj_node);
(11) adj_node에서 시작노드까지의 Euclidean 거리를 계산하
고, v_node의 인접 노드들 중 시작노드까지의 Euclidean 거
리가 최소이면 best_adj_node는 adj_node를 갖는다. 그리고, 
(33)으로 간다.
(12) tree2에 (adj_node, dist(tree2, v_node) + cost(adj_link), 
v_node)를 첨가한다.
(13) push(stack2, adj_node);
(14) adj_node에서 시작노드까지의 Euclidean 거리를 계산하
고, v_node의 인접 노드들 중 시작노드까지의 Euclidean 거
리가 최소이면 best_adj_node는 adj_node를 갖는다. 그리고, 
(33)으로 간다.
(15) dist(tree2, 
v_node) 
+ 
cost(adj_link) 
+ 
dist(tree1, 
adj_node)가 min_path1+min_path2보다 크거나 같으면 (33)
로 간다.
(16) min_path2 := dist(tree2, v_node) + cost(adj_link); 수행, 
min_path1 
:= 
dist(tree1, 
adj_node); 
수행, 
mid_node 
:= 
adj_node로 설정한다.
(17) adj_node가 tree2에 없으면 (51)로 간다.
(18) adj_node를 
tree2에서 
찾아 
(adj_node, 
dist(tree2, 
v_node) + cost(adj_link), v_node)로 갱신한다.
(19) push(stack2, adj_node); 수행, (33)으로 간다.
(20) tree2에 (adj_node, dist(tree2, v_node) + cost(adj_link), 
v_node)를 첨가한다.
(21) push(stack2, adj_node); 수행, (33)으로 간다.
(22) stack2에서 
best_adj_node를 
delete하고 
push(stack2, 
best_adj_node); 수행한다.
(23) c_node := mid_node;
(24) push(s_path, c_node);
(25) c_node == 시작노드이면 (60)으로 간다.
(26) pre_node := get_pre(tree1, c_node);
(27) push(s_path, pre_node);
(28) c_node := pre_node; 수행, (56)으로 간다.
(29) c_node := mid_node;
(30) c_node == 목표노드이면 (65)로 간다.
(31) pre_node := get_pre(tree2, c_node);
(32) adds(s_path, pre_node);
(33) c_node := pre_node; 수행, (61)로 간다.


<부록 4> 2DBS(2-way search by DBS-BFS)
(1) addq(queue1, 시작노드); addq(queue2, 목표노드);
(2) tree1에 (시작노드, 0, NULL)을 첨가, tree2에 (목표노드, 
0, NULL)을 첨가
(3) queue1과 
queue2가 
모두 
비거나 
탐색 
반복 
회수가 
counter 값과 같으면 (54)로 간다.
(4) queue1이 비면, (29)로 간다.
(5) v_node := pop(queue1);
(6) dist(tree1, v_node)가 min_path1보다 크거나 같으면 (29)
로 간다.
(7) v_node에 인접한 링크들을 인접 링크 buffer에 삽입한다.
(8) 인접 링크 buffer가 비면 (28)로 간다.
(9) adj_link := pop(buffer);
(10) adj_node := adj_link에 연결된 인접 노드;
(11) adj_node가 tree2에 있으면 (21)로 간다.
(12) dist(tree1, v_node) + cost(adj_link)가
 min_path1보다 크거나 같으면 (8)로 간다.
(13) adj_node가 tree1에 없으면 (18)로 간다.
(14) dist(tree1, 
v_node) 
+ 
cost(adj_link)가 
dist(tree1, 
adj_node)보다 크거나 같으면 (8)로 간다.
(15) adj_node를 
tree1에서 
찾아 
(adj_node, 
dist(tree1, 
v_node) + cost(adj_link), v_node)로 갱신한다.
(16) addq(queue1, adj_node);
(17) adj_node에서 목표노드까지의 Euclidean 거리를 계산하
고, v_node의 인접 노드들 중 목표노드까지의 Euclidean 거
리가 최소이면 best_adj_node는 adj_node를 갖는다. 그리고, 
(8)로 간다.
(18) tree1에 (adj_node, dist(tree1, v_node) + cost(adj_link), 
v_node)를 첨가한다.
(19) addq(queue1, adj_node);
(20) adj_node에서 목표노드까지의 Euclidean 거리를 계산하
고, v_node의 인접 노드들 중 목표노드까지의 Euclidean 거
리가 최소이면 best_adj_node는 adj_node를 갖는다. 그리고, 
(8)로 간다.
(21) dist(tree1, 
v_node) 
+ 
cost(adj_link) 
+ 
dist(tree2, 
adj_node)가 min_path1+min_path2보다 크거나 같으면 (8)로 
간다.
(22) min_path1 := dist(tree1, v_node) + cost(adj_link); 수행, 
min_path2 
:= 
dist(tree2, 
adj_node); 
수행, 
mid_node 
:= 
adj_node; 수행.
(23) adj_node가 tree1에 없으면 (26)로 간다.
(24) adj_node를 
tree1에서 
찾아 
(adj_node, 
dist(tree1, 
v_node) + cost(adj_link), v_node)로 갱신한다.
(25) addq(queue1, adj_node); 수행, (8)로 간다.
(26) tree1에 (adj_node, dist(tree1, v_node) + cost(adj_link), 
v_node)를 첨가한다.
(27) addq(queue1, adj_node); 수행, (8)로 간다.
(28) tree1에 mid_node가 없으면, queue1에서 best_adj_node
를 delete하고 queue1의 front에 best_adj_node를 삽입한다. 
(1)
<부록 4> 계속
(1) v_node에 인접한 링크들을 인접 링크 buffer에 삽입한다.
(2) 인접 링크 buffer가 비면 (53)으로 간다.
(3) adj_link := pop(buffer);
(4) adj_node := adj_link에 연결된 인접 노드;
(5) adj_node가 tree1에 있으면 (46)으로 간다.
(6) dist(tree2, v_node) + cost(adj_link)가
 min_path2보다 크거나 같으면 (33)로 간다.
(7) adj_node가 tree2에 없으면 (43)으로 간다.
(8) dist(tree2, 
v_node) 
+ 
cost(adj_link)가 
dist(tree2, 
adj_node)보다 크거나 같으면 (33)로 간다.
(9) adj_node를 tree2에서 찾아 (adj_node, dist(tree2, v_node) 
+ cost(adj_link), v_node)로 갱신한다.
(10) addq(queue2, adj_node);
(11) adj_node에서 시작노드까지의 Euclidean 거리를 계산하
고, v_node의 인접 노드들 중 시작노드까지의 Euclidean 거
리가 최소이면 best_adj_node는 adj_node를 갖는다. 그리고, 
(33)으로 간다.
(12) tree2에 (adj_node, dist(tree2, v_node) + cost(adj_link), 
v_node)를 첨가한다.
(13) addq(queue2, adj_node);
(14) adj_node에서 시작노드까지의 Euclidean 거리를 계산하고, 
v_node의 인접 노드들 중 시작노드까지의 Euclidean 거리가 
최소이면 best_adj_node는 adj_node를 갖는다. 그리고, (33)
으로 간다.


<부록 4> 계속
(1) dist(tree2, 
v_node) 
+ 
cost(adj_link) 
+ 
dist(tree1, 
adj_node)가 min_path1+min_path2보다 크거나 같으면 (33)
로 간다.
(2) min_path2 := dist(tree2, v_node) + cost(adj_link); 수행, 
min_path1 
:= 
dist(tree1, 
adj_node); 
수행, 
mid_node 
:= 
adj_node로 설정한다.
(3) adj_node가 tree2에 없으면 (51)로 간다.
(4) adj_node를 tree2에서 찾아 (adj_node, dist(tree2, v_node) 
+ cost(adj_link), v_node)로 갱신한다.
(5) addq(queue2, adj_node); 수행, (33)으로 간다.
(6) tree2에 (adj_node, dist(tree2, v_node) + cost(adj_link), 
v_node)를 첨가한다.
(7) addq(queue2, adj_node); 수행, (33)으로 간다.
(8) tree2에 mid_node가 없으면, queue2에서 best_adj_node를 
delete하고 queue2의 front에 best_adj_node를 삽입한다.
(9) c_node := mid_node;
(10) addq(s_path, c_node);
(11) c_node == 시작노드이면 (60)으로 간다.
(12) pre_node := get_pre(tree1, c_node);
(13) addq(s_path, pre_node);
(14) c_node := pre_node; 수행, (56)으로 간다.
(15) c_node := mid_node;
(16) c_node == 목표노드이면 (65)로 간다.
(17) pre_node := get_pre(tree2, c_node);
(18) adds(s_path, pre_node);
(19) c_node := pre_node; 수행, (61)로 간다.
(20) s_path에 저장된 노드들을 하나씩 pop함으로 최단경로 상
의 방문 노드들을 알 수 있다. 종료한다.
