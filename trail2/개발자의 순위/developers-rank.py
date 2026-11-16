k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]

# Please write your code here.
below = {}   # below[dev] = 모든 경기에서 dev보다 뒤에 있던 개발자들

for g, row in enumerate(arr):
    for idx, dev in enumerate(row):
        later = set(row[idx + 1:])   # 이번 경기에서 dev보다 후순위
        if g == 0:
            below[dev] = later
        else:
            below[dev] &= later      # 교집합만 남김

print(sum(len(s) for s in below.values()))
