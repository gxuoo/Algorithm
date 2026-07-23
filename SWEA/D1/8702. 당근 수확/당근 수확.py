T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    mid = N // 2

    left, right = arr[:mid], arr[mid:]
    diff = abs(sum(left) - sum(right))
    boundary = mid  # left의 마지막 인덱스

    if sum(left) <= sum(right):
        # right -> left 로 이동
        while right:
            new_left = left + [right[0]]
            new_right = right[1:]
            new_diff = abs(sum(new_left) - sum(new_right))
            if new_diff < diff:
                diff = new_diff
                left, right = new_left, new_right
                boundary = len(left)
            else:
                break
    else:
        # left -> right 로 이동
        while left:
            new_right = [left[-1]] + right
            new_left = left[:-1]
            new_diff = abs(sum(new_left) - sum(new_right))
            if new_diff < diff:
                diff = new_diff
                left, right = new_left, new_right
                boundary = len(left)
            else:
                break

    print(f'#{test_case} {boundary} {diff}')