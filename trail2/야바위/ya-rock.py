n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]
a, b, c = zip(*moves)
a, b, c = list(a), list(b), list(c)

# Please write your code here.
ans = 0
# 조약돌 초기 위치 가정
for start in range(1, 4):
    pos = start
    score = 0
    for i in range(n):
        # a[i]번과 b[i]번 컵 교환 → 조약돌이 그 컵에 있었다면 같이 이동
        if pos == a[i]:
            pos = b[i]
        elif pos == b[i]:
            pos = a[i]

        # c[i]번 컵을 열었을 때 조약돌이 있으면 점수
        if pos == c[i]:
            score += 1
    ans = max(ans, score)

print(ans)
