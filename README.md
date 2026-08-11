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
    │       ├── 문제이름.java          # Java 제출 코드
    │       └── 문제이름.py            # Python 제출 코드
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
| 21936 | [길이가 M인 회문 찾기](SWEA/D1/21936.%20%EA%B8%B8%EC%9D%B4%EA%B0%80%20M%EC%9D%B8%20%ED%9A%8C%EB%AC%B8%20%EC%B0%BE%EA%B8%B0) | D1 | 완전탐색, 문자열 | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="16" height="16" alt="Python"/> |      | [문제 보기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AZFkKmLa1zEDFAQW) |
| 23795 | [우주 괴물](SWEA/D1/23795.%E2%80%85%EC%9A%B0%EC%A3%BC%E2%80%85%EA%B4%B4%EB%AC%BC) | D1 | 구현, 시뮬레이션 | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="16" height="16" alt="Python"/> |      | [문제 보기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AZU7flp6n8XHBIRK) |
| 22375 | [스위치 조작](SWEA/D1/22375.%E2%80%85%EC%8A%A4%EC%9C%84%EC%B9%98%E2%80%85%EC%A1%B0%EC%9E%91) | D1 | 그리디, 구현 | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="16" height="16" alt="Python"/> |      | [문제 보기](https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AZHA7Cn6ZgsDFAQP) |
| 8702 | [당근 수확](SWEA/D1/8702.%E2%80%85%EB%8B%B9%EA%B7%BC%E2%80%85%EC%88%98%ED%99%95) | D1 | 그리디, 구현 | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="16" height="16" alt="Python"/> |      | [문제 보기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AW2ZiPcaPQ8DFAWg) |
| 10760 | [우주선착륙2](SWEA/D2/10760.%E2%80%85%EC%9A%B0%EC%A3%BC%EC%84%A0%EC%B0%A9%EB%A5%992) | D2 | 구현, 완전탐색 | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="16" height="16" alt="Python"/> |      | [문제 보기](https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AXSHJueab1oDFAQT) |
| 12712 | [파리퇴치3](SWEA/D2/12712.%20%ED%8C%8C%EB%A6%AC%ED%87%B4%EC%B9%983) | D2 | 구현, 완전탐색 | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="16" height="16" alt="Python"/> |      | [문제 보기](https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AXuARWAqDkQDFARa) |
| 1926 | [간단한 369게임](SWEA/D2/1926.%20%EA%B0%84%EB%8B%A8%ED%95%9C%20369%EA%B2%8C%EC%9E%84) | D2 | 구현, 문자열 | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="16" height="16" alt="Python"/> |      | [문제 보기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PTeo6AHUDFAUq) |
| 1959 | [두 개의 숫자열](SWEA/D2/1959.%20%EB%91%90%20%EA%B0%9C%EC%9D%98%20%EC%88%AB%EC%9E%90%EC%97%B4) | D2 | 구현, 완전탐색 | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="16" height="16" alt="Python"/> |      | [문제 보기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpoFaAS4DFAUq) |
| 1979 | [어디에 단어가 들어갈 수 있을까](SWEA/D2/1979.%20%EC%96%B4%EB%94%94%EC%97%90%20%EB%8B%A8%EC%96%B4%EA%B0%80%20%EB%93%A4%EC%96%B4%EA%B0%88%20%EC%88%98%20%EC%9E%88%EC%9D%84%EA%B9%8C) | D2 | 구현, 완전탐색 | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="16" height="16" alt="Python"/> |      | [문제 보기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PuPq6AaQDFAUq) |
| 20230 | [풍선팡 보너스게임2](SWEA/D2/20230.%20%ED%92%8D%EC%84%A0%ED%8C%A1%20%EB%B3%B4%EB%84%88%EC%8A%A4%EA%B2%8C%EC%9E%842) | D2 | 구현, 완전탐색 | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="16" height="16" alt="Python"/> |      | [문제 보기](https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AY3FFOTaN7EDFAXh) |
| 25052 | [등산로](SWEA/D2/25052.%20%EB%93%B1%EC%82%B0%EB%A1%9C) | D2 | DFS, 그리디, 완전탐색 | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="16" height="16" alt="Python"/> | 🔁 | [문제 보기](https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AZiyl6OKpUjHBIP9) |
| 25985 | [숫자열의 최대 곱](SWEA/D2/25985.%E2%80%85%EC%88%AB%EC%9E%90%EC%97%B4%EC%9D%98%E2%80%85%EC%B5%9C%EB%8C%80%E2%80%85%EA%B3%B1) | D2 | 구현, 완전탐색 | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="16" height="16" alt="Python"/> |      | [문제 보기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AZvmEUAqG6LHBIQE) |
| 26045 | [부분 수열 판별](SWEA/D2/26045.%20%EB%B6%80%EB%B6%84%20%EC%88%98%EC%97%B4%20%ED%8C%90%EB%B3%84) | D2 | 그리디, 투 포인터, 구현 | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="16" height="16" alt="Python"/> |      | [문제 보기](https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AZwe0FZaG1bHBIPa) |
| 26059 | [과일 등급 분류](SWEA/D2/26059.%20%EA%B3%BC%EC%9D%BC%20%EB%93%B1%EA%B8%89%20%EB%B6%84%EB%A5%98) | D2 | 정렬, 완전탐색, 구현 | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="16" height="16" alt="Python"/> |      | [문제 보기](https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AZwl9ifa3dLHBIT3) |
| 1289 | [원재의 메모리 복구하기](SWEA/D3/1289.%20%EC%9B%90%EC%9E%AC%EC%9D%98%20%EB%A9%94%EB%AA%A8%EB%A6%AC%20%EB%B3%B5%EA%B5%AC%ED%95%98%EA%B8%B0) | D3 | 그리디, 문자열, 구현 | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="16" height="16" alt="Python"/> |      | [문제 보기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV19AcoKI9sCFAZN) |
| 3499 | [퍼펙트 셔플](SWEA/D3/3499.%20%ED%8D%BC%ED%8E%99%ED%8A%B8%20%EC%85%94%ED%94%8C) | D3 | 구현, 시뮬레이션 | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="16" height="16" alt="Python"/> |      | [문제 보기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWGsRbk6AQIDFAVW) |
| 11315 | [오목 판정](SWEA/D3/11315.%20%EC%98%A4%EB%AA%A9%20%ED%8C%90%EC%A0%95) | D3 | DFS, 완전탐색, 구현 | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="16" height="16" alt="Python"/> |      | [문제 보기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXaSUPYqPYMDFASQ) |
| 14555 | [공과 잡초](SWEA/D3/14555.%20%EA%B3%B5%EA%B3%BC%20%EC%9E%A1%EC%B4%88) | D3 | 문자열, 구현 | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="16" height="16" alt="Python"/> |      | [문제 보기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AYGtoa3qARcDFARC) |

> 언어: <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="16" height="16" alt="Python"/> Python ·
> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg" width="16" height="16" alt="Java"/> Java
> &nbsp;|&nbsp; 복습: 🔁 다시 풀어볼 문제

## 🔁 다시 풀어볼 문제

복습이 필요하다고 표시한 문제를 모아둡니다.

- [ ] [25052. 등산로](SWEA/D2/25052.%20%EB%93%B1%EC%82%B0%EB%A1%9C) — 가장 낮은 한 칸만 따라가는 그리디 방식이라, 여러 갈래를 모두 탐색하는 일반 DFS + 백트래킹으로도 풀어보기

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

> 💡 커밋 컨벤션: 백준허브는 `[D1] Title: ..., -BaekjoonHub` 형식으로 자동 커밋하고,
> `/polish` 정리 커밋은 `polish: <문제번호들>` (예: `polish: 21936, 1859`)을 사용합니다.
