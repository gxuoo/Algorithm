T = int(input())

for test_case in range(1, T + 1):
    field = list(map(str, input()))
    count = 0

    for idx in range(len(field) - 1):
        if field[idx] == '(' and field[idx + 1] == '|':
            field[idx + 1] = ')'
        if field[idx] == '|' and field[idx + 1] == ')':
            field[idx] = '('

    for idx in range(len(field) - 1):
        if field[idx] == '(' and field[idx + 1] == ')':
            count += 1

    print(f"#{test_case} {count}")
