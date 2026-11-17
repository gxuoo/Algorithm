X, Y = map(int, input().split())

# Please write your code here.
total = 0
for i in range(X, Y + 1):
    cnt = [0] * 10
    num = i
    while num > 0:
        cnt[num % 10] += 1
        num //= 10

    kinds = [c for c in cnt if c > 0]
    if len(kinds) == 2 and 1 in kinds:
        total += 1

print(total)
