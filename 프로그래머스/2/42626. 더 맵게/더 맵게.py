import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        if not len(scoville):
            return -1
        
        min1 = heapq.heappop(scoville)
        if min1 < K:
            if not len(scoville):
                return -1
            min2 = heapq.heappop(scoville)
            new_value = min1 + min2 * 2
            heapq.heappush(scoville, new_value)
            answer += 1
        else:
            heapq.heappush(scoville, min1)
            break

    return answer
