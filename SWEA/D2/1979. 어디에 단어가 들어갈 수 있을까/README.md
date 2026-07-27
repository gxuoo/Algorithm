# [D2] 어디에 단어가 들어갈 수 있을까 - 1979 

[문제 링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PuPq6AaQDFAUq) 

### 성능 요약

메모리: 53,888 KB, 시간: 70 ms, 코드길이: 805 Bytes

### 제출 일자

2026-07-27 13:38



> 출처: SW Expert Academy, https://swexpertacademy.com/main/code/problem/problemList.do
## 문제 요약
N×N 퍼즐판에서 벽(0)으로 막혀 길이가 정확히 K인 빈칸(1) 연속 구간이 가로·세로로 몇 군데 있는지 센다.

## 접근 방법
- 각 행을 훑으며 1의 연속 길이를 세고, 0을 만나거나 행이 끝날 때 그 길이가 정확히 K이면 카운트한다.
- 같은 방식으로 각 열도 세로로 확인한다.
- 길이가 K보다 길거나 짧은 구간은 세지 않는다.

## 복잡도
- 시간: O(N²) — 가로·세로 각각 전체 칸을 한 번씩 훑는다.
- 공간: O(N²) — 퍼즐판 저장.

## 알고리즘 유형
구현, 완전탐색
