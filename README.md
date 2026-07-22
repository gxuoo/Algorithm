# 🧩 Algorithm — SWEA 문제 풀이 기록

SWEA에서 푼 문제들을 기록하는 저장소입니다.

[백준허브(BaekjoonHub)](https://chromewebstore.google.com/detail/ccammcjdkpgjmcpijpahlehmapgmphmk)로 풀이가 자동 업로드되고,
결과물을 Claude가 다듬어 풀이 설명과 아래 인덱스 표를 채웁니다.

## 📁 폴더 구조

백준허브 규칙에 따라 **플랫폼 → 난이도 → 문제** 순으로 정리됩니다.

```
Algorithm/
├── README.md                          # 현재 파일 — 전체 인덱스 & 운영 규칙
└── SWEA/
    ├── D2/
    │   └── 1234. 문제이름/
    │       ├── README.md              # 지문(백준허브) + 풀이 보강(Claude)
    │       ├── Solution.java          # Java 제출 코드
    │       └── Solution.py            # Python 제출 코드
    ├── D3/
    ├── D4/
    ├── D5/
    ├── D6/
    └── Unrated/
```

- **난이도**는 폴더로 구분됩니다. (백준허브가 자동 생성)
- **유형**(DP·BFS·완전탐색 등)은 폴더 대신 아래 **인덱스 표의 컬럼**으로 관리합니다.
  → 난이도와 유형을 둘 다 검색·정렬할 수 있습니다.

## 📋 전체 문제 목록

| 번호 | 문제 이름 | 난이도 | 유형 | 언어 | 복습 | 링크 |
|:----:|-----------|:------:|------|:----:|:----:|------|
| —    | _아직 없음_ | —    | —    | —    |      | —    |

> 언어: <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="16" height="16" alt="Python"/> Python ·
> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg" width="16" height="16" alt="Java"/> Java
> &nbsp;|&nbsp; 복습: 🔁 다시 풀어볼 문제

## 🔁 다시 풀어볼 문제

복습이 필요하다고 표시한 문제를 모아둡니다.

- [ ] _아직 없음_

## ⚙️ 저장소 운영 방식

이 저장소는 세 주체가 역할을 나눠 굴러갑니다.

- 🔵 **백준허브** (자동) — 문제 폴더 생성, 코드 업로드, 지문 README 생성, 커밋 & 푸시
- 🤖 **Claude** (로컬 `/polish` 명령어) — 지문뿐인 README에 **풀이·접근·복잡도** 보강, **유형 분류**, 위 **인덱스 표** 갱신
- 🙋 **나** — 문제 풀기, 마무리할 때 `/polish` 실행, **복습 대상 표시(🔁)**

### 작업 흐름
1. SWEA에서 문제를 풀고 제출하면 → 백준허브가 자동으로 폴더·코드·README를 커밋한다.
2. 하루를 마무리할 때 Claude Code에서 `/polish`를 실행한다.
   → Claude가 새로 올라온 문제들의 README를 보강하고, 유형을 분류해 인덱스 표를 갱신한 뒤 커밋/푸시한다.
3. 나는 복습하고 싶은 문제에 🔁만 표시한다.

> 💡 커밋 메시지는 백준허브와 `/polish`가 자동 생성하므로 별도의 커밋 컨벤션은 두지 않습니다.
