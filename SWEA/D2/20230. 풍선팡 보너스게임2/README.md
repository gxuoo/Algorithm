# [D2] 풍선팡 보너스게임2 - 20230 

[문제 링크](https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AY3FFOTaN7EDFAXh) 

### 성능 요약

메모리: 59,008 KB, 시간: 73 ms, 코드길이: 463 Bytes

### 제출 일자

2026-07-28 17:42



> 출처: SW Expert Academy, https://swexpertacademy.com/main/code/problem/problemList.do
## 문제 요약
N×N 격자에서 한 칸을 고른 뒤, 그 칸이 속한 행 전체와 열 전체(십자 모양)의 값을 모두
더했을 때 나올 수 있는 최댓값을 구한다.

## 접근 방법
- 모든 칸 `(row, col)`을 터뜨릴 후보로 놓고 완전탐색한다.
- 후보마다 `sum(arr[row])`(행 전체)과 `sum(arr[r][col])`(열 전체)을 더한다.
- 교차점 `arr[row][col]`이 두 번 더해지므로 한 번 빼준다.
- 이렇게 구한 값들 중 최댓값을 갱신해 출력한다.

## 복잡도
- 시간: O(N³) — 칸마다 행·열 합을 매번 다시 계산한다.
  (행별·열별 합을 미리 구해두면 O(N²)로 줄일 수 있다)
- 공간: O(N²) — 격자 저장.

## 알고리즘 유형
구현, 완전탐색
