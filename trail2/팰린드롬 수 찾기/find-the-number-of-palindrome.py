X, Y = map(int, input().split())

# Please write your code here.
total = 0
for i in range(X, Y + 1):
    arr = list(str(i))
    cnt = 0
    for j in range(len(arr)):
        if arr[j] == arr[len(arr) - j - 1]:
            cnt += 1

    if cnt == len(arr):
        total += 1

print(total)
