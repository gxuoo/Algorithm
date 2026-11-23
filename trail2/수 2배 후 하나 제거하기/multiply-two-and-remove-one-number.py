n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
ans = float('inf')
for i in range(n):
    arr_cp1 = arr[:]
    arr_cp1[i] *= 2
    for j in range(n):
        arr_cp2 = arr_cp1[:]
        arr_cp2.pop(j)
        total = 0
        for k in range(n - 2):
            total += abs(arr_cp2[k] - arr_cp2[k + 1])
        ans = min(ans, total)

print(ans)
