T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    s = input()

    answer = 'NONE'
    for i in range(N - M + 1):
        sub = s[i:i + M]
        if sub == sub[::-1]:
            answer = sub
            break             

    print(f'#{test_case} {answer}')
