T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_total = 0
    for row in range(N):
        for col in range(N):
            total = 0
            total += sum(arr[row])
            total += sum(arr[r][col] for r in range(N))
            total -= arr[row][col]
            if total > max_total:
                max_total = total

    print(f"#{test_case} {max_total}")
