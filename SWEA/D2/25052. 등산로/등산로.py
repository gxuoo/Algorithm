T = int(input())

def dfs(row, col, path_length):
    global longest_path
    longest_path = max(longest_path, path_length)

    best_row, best_col = -1, -1
    lowest = arr[row][col]

    for dir_row, dir_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        next_row = row + dir_row
        next_col = col + dir_col

        if not (0 <= next_row < N and 0 <= next_col < N):
            continue

        if arr[next_row][next_col] < lowest:
            lowest = arr[next_row][next_col]
            best_row, best_col = next_row, next_col

    if best_row != -1:
        dfs(best_row, best_col, path_length + 1)


for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    longest_path = 0
    for r in range(N):
        for c in range(N):
            dfs(r, c, 1)

    print(f"#{test_case} {longest_path}")
