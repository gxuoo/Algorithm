# [D2] 간단한 369게임 - 1926 

[문제 링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PTeo6AHUDFAUq) 

### 성능 요약

메모리: 52,352 KB, 시간: 64 ms, 코드길이: 293 Bytes

### 제출 일자

2026-07-27 13:37



> 출처: SW Expert Academy, https://swexpertacademy.com/main/code/problem/problemList.do
## 문제 요약
1부터 N까지 수를 차례로 말하되, 3·6·9가 들어간 수는 그 개수만큼 박수(-)로 바꿔 출력한다.

## 접근 방법
- 각 수를 문자열로 바꿔 자릿수마다 '3','6','9'의 개수를 센다.
- 개수가 0이면 수를 그대로, 1 이상이면 개수만큼 '-'를 출력한다.
- 각 출력은 공백으로 구분해 이어 붙인다.

## 복잡도
- 시간: O(N·log N) — 수마다 자릿수만큼 확인한다.
- 공간: O(1).

## 알고리즘 유형
구현, 문자열
