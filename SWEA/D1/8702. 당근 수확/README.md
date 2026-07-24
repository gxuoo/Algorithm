# [D1] 당근 수확 - 8702 

[문제 링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AW2ZiPcaPQ8DFAWg) 

### 성능 요약

메모리: 52,608 KB, 시간: 58 ms, 코드길이: 1,098 Bytes

### 제출 일자

2026-07-23 16:29



> 출처: SW Expert Academy, https://swexpertacademy.com/main/code/problem/problemList.do
## 문제 요약
당근 밭을 두 구역으로 나눌 때 경계를 옮겨 가며 양쪽 당근 수 차이를 최소로 만드는 문제.
경계 위치와 그때의 최소 차이를 출력한다.

## 접근 방법
- 배열을 중앙(N//2)에서 좌/우로 나누고 두 합의 차이를 기준값으로 삼는다.
- 왼쪽 합이 더 작으면 오른쪽 원소를 하나씩 왼쪽으로 넘기고, 크면 왼쪽 원소를 오른쪽으로 넘긴다.
- 차이가 줄어드는 동안만 경계를 이동하고, 더 이상 줄지 않으면 멈추는 그리디 방식.

## 복잡도
- 시간: O(N²) — 경계 이동마다 슬라이싱과 sum으로 합을 다시 계산한다.
- 공간: O(N)

## 알고리즘 유형
그리디, 구현
