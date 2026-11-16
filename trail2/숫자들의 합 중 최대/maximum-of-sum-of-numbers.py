X, Y = map(int, input().split())

# Please write your code here.
ans = 0
for i in range(X, Y + 1):
    num = i
    res = 0
    while num:
        res += num % 10
        num //= 10

    ans = max(ans, res)

print(ans)
