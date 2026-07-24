# [D2] 우주선착륙2 - 10760 

[문제 링크](https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AXSHJueab1oDFAQT) 

### 성능 요약

메모리: 60,928 KB, 시간: 128 ms, 코드길이: 829 Bytes

### 제출 일자

2026-07-24 14:05



> 출처: SW Expert Academy, https://swexpertacademy.com/main/code/problem/problemList.do
## 문제 요약
N×M 높이 격자에서, 주변 8칸 중 자신보다 낮은 칸이 4개 이상인 칸을 착륙 가능 지점으로 센다.

## 접근 방법
- 모든 칸을 순회하며 8방향 이웃을 확인한다.
- 격자 범위 안이면서 현재 칸보다 낮은 이웃의 개수를 센다.
- 그 개수가 4 이상이면 착륙 가능 지점으로 카운트한다.

## 복잡도
- 시간: O(N·M) — 각 칸마다 이웃 8칸을 상수 번 확인한다.
- 공간: O(N·M) — 높이 격자 저장.

## 알고리즘 유형
구현, 완전탐색(그리드 탐색)
