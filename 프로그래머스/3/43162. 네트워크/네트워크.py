def solution(n, computers):
    visited = [False] * n
    network_count = 0
    
    def dfs(current):
        visited[current] = True
        for next_com in range(n):
            if computers[current][next_com]:
                if not visited[next_com]:
                    dfs(next_com)
    
    for computer in range(n):
        if not visited[computer]:
            dfs(computer)
            network_count += 1
    
    return network_count
