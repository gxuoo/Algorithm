A, B, C = map(int, input().split())

# Please write your code here.
ans = 0
for i in range(C // A + 1):           # A를 i번 사용
    for j in range(C // B + 1):       # B를 j번 사용
        total = A * i + B * j
        if total <= C:
            ans = max(ans, total)

print(ans)
