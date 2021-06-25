# https://programmers.co.kr/learn/courses/30/lessons/49189

from collections import deque

def bfs(n, edge):
    adj_list = [[] for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    weight = [0 for _ in range(n + 1)]
    mx = -2000000000
    
    for a, b in edge:
        adj_list[a].append(b)
        adj_list[b].append(a)
        
    adj_list = [sorted(li) for li in adj_list]
    dq = deque([1])
    while dq:
        v = dq.popleft()
        visited[v] = True
        
        for t in adj_list[v]:
            if visited[t] or weight[t] != 0:
                continue
            weight[t] = weight[v] + 1
            dq.append(t)
    mx = max(weight)
    res = weight.count(mx)
    
    return res
    

def solution(n, edge):
    
    answer = bfs(n, edge)
    return answer