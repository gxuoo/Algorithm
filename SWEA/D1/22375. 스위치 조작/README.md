# [D1] 스위치 조작 - 22375 

[문제 링크](https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AZHA7Cn6ZgsDFAQP) 

### 성능 요약

메모리: 52,480 KB, 시간: 69 ms, 코드길이: 528 Bytes

### 제출 일자

2026-07-22 16:30



> 출처: SW Expert Academy, https://swexpertacademy.com/main/code/problem/problemList.do
## 문제 요약
0/1 스위치 배열의 현재 상태를 목표 상태로 바꾸려 한다. 한 번의 조작은 위치 i를 골라
i부터 끝까지의 스위치를 모두 뒤집는 것(접미사 반전)이며, 필요한 최소 조작 횟수를 구한다.

## 접근 방법
- 왼쪽부터 훑으며 `cur[i] != res[i]`인 첫 지점을 찾으면 그 위치부터 끝까지 뒤집고 횟수를 1 늘린다.
- 접미사 반전은 반전 지점 왼쪽(이미 맞춰둔 부분)에 영향을 주지 않으므로,
  매번 가장 왼쪽 불일치를 해소하는 것이 최적이다.
- 뒤집은 뒤 `i=0`으로 되돌려 처음부터 다시 확인한다.

## 복잡도
- 시간: O(N²) — 조작은 최대 N번, 각 조작마다 배열을 한 번씩 훑는다.
- 공간: O(N)

## 알고리즘 유형
그리디, 구현/시뮬레이션
