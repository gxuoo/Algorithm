def solution(prices):
    n = len(prices)
    answer = []
    for i in range(n):
        total = 0
        for j in range(i + 1, n):
            total += 1
            if prices[j] < prices[i]:
                break
        answer.append(total)
    return answer