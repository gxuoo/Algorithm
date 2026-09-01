def solution(clothes):
    count = {}
    for name, kind in clothes:
        count[kind] = count.get(kind, 0) + 1
        
    answer = 1
    for n in count.values():
        answer *= (n + 1)
    return answer - 1