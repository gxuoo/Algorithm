def solution(arr):
    answer = []
    for value in arr:
        if not len(answer):
            answer.append(value)

        if value != answer[len(answer) - 1]:
            answer.append(value)
    return answer