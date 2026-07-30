# [D2] 부분 수열 판별 - 26045 

[문제 링크](https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AZwe0FZaG1bHBIPa) 

### 성능 요약

메모리: 52,480 KB, 시간: 60 ms, 코드길이: 478 Bytes

### 제출 일자

2026-07-30 17:21



> 출처: SW Expert Academy, https://swexpertacademy.com/main/code/problem/problemList.do
## 문제 요약
길이 N인 수열 A와 길이 M인 수열 B가 주어질 때, B가 A의 **부분 수열**
(순서를 지키며 일부만 골라낸 수열)인지 판별해 YES / NO를 출력한다.

## 접근 방법
- A를 앞에서부터 소비한 위치 `index`를 들고, B의 원소를 순서대로 하나씩 맞춰 나가는 그리디.
- `arr = a[index:]`로 아직 쓰지 않은 뒷부분만 남긴 뒤, 거기에 `b[i]`가 있으면
  **가장 앞에 있는 위치**(`arr.index(b[i])`)에서 매칭하고 `index`를 그 다음 칸으로 옮긴다.
- 남은 구간에 `b[i]`가 없으면 순서를 지켜 맞출 방법이 없으므로 `flag = False`.
- 항상 가장 이른 위치에서 끊는 것이 최적이다. 뒤에 올 원소들에게 남겨주는 구간이 가장 넓어지므로,
  이 선택으로 실패했다면 더 뒤에서 매칭하는 어떤 선택으로도 실패한다.
- B를 끝까지 소화했으면 YES, 아니면 NO.

## 복잡도
- 시간: O(N × M) — B의 원소마다 `a[index:]` 슬라이스 복사와 탐색이 각각 최대 N번.
  슬라이싱 없이 두 포인터로 A를 한 번만 훑으면 O(N + M)까지 줄일 수 있다.
- 공간: O(N) — 매 반복에서 새로 만들어지는 슬라이스.

## 알고리즘 유형
그리디, 투 포인터, 구현
