T = int(input())

for test_case in range(1, T + 1):
    bits = input().strip()

    count = 0

    if bits[0] == '1':
        count += 1

    for i in range(len(bits) - 1):
        if bits[i] != bits[i + 1]:
            count += 1

    print(f"#{test_case} {count}")
