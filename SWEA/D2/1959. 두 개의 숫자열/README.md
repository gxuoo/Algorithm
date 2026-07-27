# [D2] 두 개의 숫자열 - 1959 

[문제 링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpoFaAS4DFAUq) 

### 성능 요약

메모리: 49,792 KB, 시간: 59 ms, 코드길이: 573 Bytes

### 제출 일자

2026-07-27 13:37



> 출처: SW Expert Academy, https://swexpertacademy.com/main/code/problem/problemList.do
## 문제 요약
길이가 다른 두 숫자열을 겹쳐 놓고 겹치는 원소끼리 곱해 더할 때, 나올 수 있는 합의 최댓값을 구한다.

## 접근 방법
- 짧은 수열을 긴 수열 위에서 한 칸씩 밀며 겹치는 구간의 원소 곱의 합을 계산한다.
- n<m / n≥m 경우를 나눠 항상 짧은 쪽 길이만큼만 곱해 더한다.
- 가능한 모든 위치에서의 합 중 최댓값을 출력한다.

## 복잡도
- 시간: O(|n−m|·min(n,m)) — 위치 수 × 겹침 길이.
- 공간: O(|n−m|) — 각 위치의 합 저장 (누적 최댓값만 두면 O(1)).

## 알고리즘 유형
구현, 완전탐색
