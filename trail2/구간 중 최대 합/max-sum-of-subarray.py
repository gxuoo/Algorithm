n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
res = 0
for i in range(n - k + 1):
    arr2 = arr[i:i+k]
    res = max(res, sum(arr2))

print(res)
