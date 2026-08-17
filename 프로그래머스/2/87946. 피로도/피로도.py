def solution(k, dungeons):
    visited = [False for _ in range(len(dungeons))]

    def dfs(k):
        best = 0
        for i in range(len(dungeons)):
            if visited[i] or k < dungeons[i][0]:
                continue
            visited[i] = True
            best = max(best, 1 + dfs(k - dungeons[i][1]))
            visited[i] = False
        return best
    return dfs(k)

print(solution(80, [[80,20],[50,40],[30,10]]))
