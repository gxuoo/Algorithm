---
description: 백준허브가 올린 새 문제들의 README를 보강하고 인덱스 표를 갱신한다
---

SWEA 풀이 기록 정리를 수행하라.

1. `git pull` 로 백준허브가 올린 최신 커밋을 받는다.
2. 루트 README.md의 "전체 문제 목록" 표를 읽고, `SWEA/` 아래 문제 폴더 중 표에 없는 문제를 모두 찾는다.
3. 새 문제 폴더마다 README.md(백준허브가 만든 지문만 있는 상태)에 아래 섹션을 보강한다.
   이미 보강된 문제는 건드리지 않는다.
   - **문제 요약** — 한두 줄
   - **접근 방법** — 제출 코드를 읽고 풀이 흐름 설명
   - **복잡도** — 시간/공간 복잡도
   - **알고리즘 유형** — DP, BFS/DFS, 완전탐색, 그리디, 구현, 문자열, 수학 등
4. 루트 README.md의 "전체 문제 목록" 표에 문제마다 한 행씩 추가한다.
   - 번호·문제 이름: 폴더명 `<번호>. <이름>` 에서 추출
   - 난이도: 상위 폴더명 (D2~D6, Unrated)
   - 유형: 3번에서 판단한 유형
   - 언어: 폴더의 코드 파일 기준 —
     Python: `<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="16"/>`
     Java: `<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg" width="16"/>`
   - 복습: 빈칸으로 둔다 (사용자가 직접 🔁 표시)
   - 링크: 해당 문제 폴더로의 상대 경로 (공백·특수문자는 URL 인코딩)
   - `_아직 없음_` 플레이스홀더 행이 남아 있으면 제거한다
   - 이미 표에 있는 문제는 중복 추가하지 않는다
5. 바꾼 내용을 짧게 요약해 보여준 뒤, 아래 메시지로 커밋하고 push 한다.
   `docs: polish READMEs & update index`
