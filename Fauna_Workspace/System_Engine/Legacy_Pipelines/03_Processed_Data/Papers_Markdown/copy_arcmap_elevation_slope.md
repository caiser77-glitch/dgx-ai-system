--- 
source: copy_arcmap_elevation_slope.pdf
--- 

ArcGIS를 이용한 경사도별 면적 구하기 예제 
http://recall.tistory.com 
1. 3D Analyst 와 Spatial Analyst 익스텐션을 체크합니다. 
 
 
2. TIN 생성을 위한 레이어를 추가합니다(표고점, 등고선, 경계레이어). 
 
 
 
 


ArcGIS를 이용한 경사도별 면적 구하기 예제 
http://recall.tistory.com 
3. TIN 을 생성버튼을 클릭합니다. 
 
 
4. 경계가 될 레이어(clip 할 레이어)를 선택하고 그림과 같이 설정합니다. 
 
 
 
 


ArcGIS를 이용한 경사도별 면적 구하기 예제 
http://recall.tistory.com 
5. 생성된 TIN 보기 
 
 
6. Surface Analysis->Slope 을 클릭합니다. 
 


ArcGIS를 이용한 경사도별 면적 구하기 예제 
http://recall.tistory.com 
7. Output cell size 를 5m 로 설정합니다. 
 
 
8. 생성된 경사도 분석 보기 
 


ArcGIS를 이용한 경사도별 면적 구하기 예제 
http://recall.tistory.com 
9. Reclassify 를 선택합니다. 
 
 
10. Classify 버튼을 클릭합니다. 
 


ArcGIS를 이용한 경사도별 면적 구하기 예제 
http://recall.tistory.com 
11. Defined Interval 을 선택합니다. 
 
 
12. Interval size 를 10 으로 입력합니다. 
 


ArcGIS를 이용한 경사도별 면적 구하기 예제 
http://recall.tistory.com 
13. Reclassify 된 결과를 봅니다. 
 
 
14. Open Attribute Table 을 클릭합니다. 
 


ArcGIS를 이용한 경사도별 면적 구하기 예제 
http://recall.tistory.com 
15. Options -> Export 메뉴를 클릭합니다. 
 
 
16. Output table 을 지정합니다. 
 


ArcGIS를 이용한 경사도별 면적 구하기 예제 
http://recall.tistory.com 
17. 결과를 가지고 Excel 에서 면적을 계산합니다. 
 
 
