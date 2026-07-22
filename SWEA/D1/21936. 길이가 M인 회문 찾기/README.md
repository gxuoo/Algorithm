# [D1] 길이가 M인 회문 찾기 - 21936 

[문제 링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AZFkKmLa1zEDFAQW) 

### 성능 요약

메모리: 52,352 KB, 시간: 59 ms, 코드길이: 304 Bytes

### 제출 일자

2026-07-21 17:50



> 출처: SW Expert Academy, https://swexpertacademy.com/main/code/problem/problemList.do

### 문제 요약

길이 N인 문자열에서 **길이가 정확히 M인 부분 문자열 중 가장 먼저 나오는 회문**을 찾는다.
없으면 `NONE`을 출력한다.

### 접근 방법

- 문자열의 왼쪽부터 길이 M짜리 윈도우를 한 칸씩 옮기며(`i = 0 … N-M`) 부분 문자열 `s[i:i+M]`을 잘라낸다.
- 각 부분 문자열을 뒤집은 것(`sub[::-1]`)과 비교해 회문인지 확인하고,
  처음 발견되는 순간 `break`로 탐색을 멈춰 **가장 앞선 회문**을 답으로 삼는다.
- 끝까지 못 찾으면 초기값 `'NONE'`이 그대로 출력된다.

### 복잡도

- 시간: `O(N × M)` — 최대 `N-M+1`개의 윈도우 각각을 뒤집어 비교(M).
- 공간: `O(M)` — 부분 문자열과 그 뒤집은 사본.

### 알고리즘 유형

완전탐색, 문자열