n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
arr = [0] * n 
for i in range(n):
    for j in range(n):
        arr[i] += abs(j - i) * A[j]

print(min(arr))
