# [D2] 파리퇴치3 - 12712 

[문제 링크](https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AXuARWAqDkQDFARa) 

### 성능 요약

메모리: 60,160 KB, 시간: 94 ms, 코드길이: 982 Bytes

### 제출 일자

2026-07-27 13:22



> 출처: SW Expert Academy, https://swexpertacademy.com/main/code/problem/problemList.do
## 문제 요약
N×N 격자에서 크기 M의 '+' 또는 'x' 모양 살충제를 한 칸을 중심으로 뿌릴 때 잡을 수 있는 최대 파리 수를 구한다.

## 접근 방법
- 모든 칸을 살충제 중심으로 놓고 두 가지 모양의 합을 각각 계산한다.
- '+' 모양: 상하좌우 네 방향으로 M−1칸까지 더한다.
- 'x' 모양: 대각선 네 방향으로 M−1칸까지 더한다.
- 격자 범위 안의 칸만 더하고, 모든 중심·모양에 대한 최댓값을 답으로 한다.

## 복잡도
- 시간: O(N²·M) — 각 칸마다 8방향으로 최대 M−1칸씩 합산한다.
- 공간: O(N²) — 격자 저장.

## 알고리즘 유형
구현, 완전탐색
