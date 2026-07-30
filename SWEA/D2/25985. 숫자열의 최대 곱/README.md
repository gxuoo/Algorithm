# [D2] 숫자열의 최대 곱 - 25985 

[문제 링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AZvmEUAqG6LHBIQE) 

### 성능 요약

메모리: 52,352 KB, 시간: 62 ms, 코드길이: 489 Bytes

### 제출 일자

2026-07-30 16:17



> 출처: SW Expert Academy, https://swexpertacademy.com/main/code/problem/problemList.do
## 문제 요약
길이 N인 숫자열 A와 길이 M인 숫자열 B를 한 칸씩 밀며 겹쳐 놓고,
겹친 자리끼리 곱해 더한 값(내적) 중 가장 큰 값을 구한다. 한쪽이 삐져나온 부분 겹침도 허용된다.

## 접근 방법
- 부분 겹침을 예외 처리하지 않기 위해 **B의 앞뒤에 0을 N-1개씩 덧붙인다.**
  삐져나온 칸은 0과 곱해져 합에 영향을 주지 않으므로, 모든 겹침을 "완전히 포갠 상태"로 통일할 수 있다.
- 패딩된 B에서 시작 위치 `i`를 `0`부터 `M+N-2`까지 옮기며
  (한쪽 끝 1칸만 겹치는 상태 → 반대쪽 끝 1칸만 겹치는 상태)
  `sum(a[j] * b[i+j])`를 계산해 `res`에 모은다.
- `max(res)`가 답. 음수가 섞여 있어도 최댓값만 고르면 되므로 별도 처리가 필요 없다.

## 복잡도
- 시간: O(N × (M+N)) — 시작 위치 M+N-1개 × 위치마다 N번의 곱셈.
- 공간: O(M+N) — 패딩된 B와 결과 리스트.

## 알고리즘 유형
구현, 완전탐색
