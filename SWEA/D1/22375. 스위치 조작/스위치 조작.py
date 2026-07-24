T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    cur = list(map(int, input(). split()))
    res = list(map(int, input().split()))
    count = 0
    i = 0

    while i < N:
        if cur[i] != res[i]:
            count += 1
            idx = i
            while idx < N:
                if cur[idx]:
                    cur[idx] = 0
                else:
                    cur[idx] = 1
                idx += 1
            i = 0
        else:
            i += 1

    print(f'#{test_case} {count}')
