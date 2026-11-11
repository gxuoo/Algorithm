n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.
res = 0
for i in range(n):
    for j in range(n):
        if abs(i - j) <= 1:
            continue
        
        res = max(res, numbers[i] + numbers[j])

print(res)
