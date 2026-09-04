def solution(s):
    arr = []
    for value in s:
        if value == '(':
            arr.append(value)
        else:
            if not len(arr):
                return False
            arr.pop()
            
    if len(arr):
        return False

    return True