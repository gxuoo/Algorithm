def solution(operations):
    answer = []
    result = []
    
    for op in operations:
        command, num = op.split()
        num = int(num)
        
        if command == 'I':
            answer.append(num)
        else:
            if not len(answer):
                continue
                
            if num == 1:
                answer.remove(max(answer))
            else:
                answer.remove(min(answer))
    
    if len(answer):
        result.append(max(answer))
        result.append(min(answer))
    else:
        result.append(0)
        result.append(0)
        
    return result