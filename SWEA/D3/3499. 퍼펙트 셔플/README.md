# [D3] 퍼펙트 셔플 - 3499 

[문제 링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWGsRbk6AQIDFAVW) 

### 성능 요약

메모리: 59,264 KB, 시간: 85 ms, 코드길이: 522 Bytes

### 제출 일자

2026-08-10 16:59



> 출처: SW Expert Academy, https://swexpertacademy.com/main/code/problem/problemList.do
## 문제 요약
카드 N장을 앞쪽 절반과 뒤쪽 절반으로 나눈 뒤(홀수면 앞쪽이 한 장 더 많다),
앞·뒤 뭉치에서 **한 장씩 번갈아** 뽑아 만든 새 순서를 출력한다.

## 접근 방법
- `N // 2`를 기준으로 자르되, 홀수면 앞쪽에 한 장을 더 준다 (`arr[:N // 2 + 1]`).
  이렇게 하면 `left`는 항상 `right`와 같거나 한 장 많다.
- `left` → `right` 순으로 `pop(0)`하며 번갈아 출력한다.
- 종료 조건이 요점이다. `left`를 먼저 뽑아 출력한 **직후에** `right`가 비었는지 확인해
  `break`하므로, N이 홀수여서 마지막에 `left`만 한 장 남는 경우도
  그 한 장이 정확히 한 번 출력되고 끝난다.
- `left`가 항상 같거나 많으므로 `left.pop(0)`이 빈 리스트를 건드릴 일은 없다.

## 복잡도
- 시간: O(N²) — 리스트의 `pop(0)`이 매번 나머지 원소를 앞으로 당겨 O(N)이다.
  `deque`를 쓰거나 인덱스 두 개로 훑으면 O(N)까지 줄일 수 있다.
- 공간: O(N) — 반으로 나눈 두 리스트.

## 알고리즘 유형
구현, 시뮬레이션
