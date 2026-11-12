N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
ans = float('inf')
for i in range(N - T + 1):
    cost = sum(abs(h - H) for h in arr[i:i + T])
    ans = min(ans, cost)

print(ans)
