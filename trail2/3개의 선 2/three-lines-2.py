n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.
# 후보 선: (0, k) = 세로선 x=k, (1, k) = 가로선 y=k
lines = [(0, k) for k in range(11)] + [(1, k) for k in range(11)]

def covered(idx, line):
    kind, k = line
    if kind == 0:
        return x[idx] == k   # 세로선 위에 있는지
    return y[idx] == k       # 가로선 위에 있는지

ans = 0
L = len(lines)
for i in range(L):
    for j in range(i, L):
        for k in range(j, L):
            ok = True
            for idx in range(n):
                if not (covered(idx, lines[i]) or covered(idx, lines[j])
                        or covered(idx, lines[k])):
                    ok = False   # 이 점을 덮는 선이 없음
                    break
            if ok:
                ans = 1

print(ans)
