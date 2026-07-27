T = int(input())
for test_case in range(1, T + 1):
    s = str(test_case)
    count = 0

    for char in s:
        if char in '3' or char in '6' or char in '9':
            count += 1
    if count == 0:
        print(s, end='')
    else:
        print('-' * count, end='')
    print(end=' ')
