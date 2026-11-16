ability = list(map(int, input().split()))

# Please write your code here.
ability.sort()
res = []
for i in range(3):
    res.append(ability[i] + ability[5 - i])


print(max(res) - min(res))
