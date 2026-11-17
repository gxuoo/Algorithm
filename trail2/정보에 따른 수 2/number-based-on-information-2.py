T, a, b = map(int, input().split())
c = []
x = []
for _ in range(T):
    char, pos = input().split()
    c.append(char)
    x.append(int(pos))

# Please write your code here.
cnt = 0
for k in range(a, b + 1):
    d1 = float('inf')
    d2 = float('inf')
    for i in range(T):
        dist = abs(k - x[i])
        if c[i] == 'S':
            d1 = min(d1, dist)
        else:
            d2 = min(d2, dist)

    if d1 <= d2:
        cnt += 1

print(cnt)
