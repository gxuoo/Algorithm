T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    monster = {"row": 0, "col": 0}
    count = 0

    # enumerate 사용 방법 숙지하기
    for i, row in enumerate(field):
        if 2 in row:
            monster["row"], monster["col"] = i, row.index(2)

    # 상 방향
    row_idx, col_idx = monster["row"], monster["col"]
    while row_idx > 0:
        row_idx -= 1
        if field[row_idx][col_idx]:
            break
        else:
            field[row_idx][col_idx] = 1

    # 하 방향
    row_idx, col_idx = monster["row"], monster["col"]
    while row_idx < N - 1:
        row_idx += 1
        if field[row_idx][col_idx]:
            break
        else:
            field[row_idx][col_idx] = 1

    # 좌 방향
    row_idx, col_idx = monster["row"], monster["col"]
    while col_idx > 0:
        col_idx -= 1
        if field[row_idx][col_idx]:
            break
        else:
            field[row_idx][col_idx] = 1

    # 우 방향
    row_idx, col_idx = monster["row"], monster["col"]
    while col_idx < N - 1:
        col_idx += 1
        if field[row_idx][col_idx]:
            break
        else:
            field[row_idx][col_idx] = 1

    for i, row in enumerate(field):
        for num in row:
            if num == 0:
                count += 1

    print(f'#{test_case} {count}')
