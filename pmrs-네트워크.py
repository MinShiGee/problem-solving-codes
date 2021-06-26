# https://programmers.co.kr/learn/courses/30/lessons/43162

from collections import deque

par = [i for i in range(205)]
adj_list = [[] for i in range(205)]

def find_par(n):
    if par[n] == n:
        return n
    par[n] = find_par(par[n])
    return par[n] 

def merg(a, b):
    par_a = find_par(a)
    par_b = find_par(b)
    if par_a > par_b:
        par[b] = par_a
    else:
        par[a] = par_b
    
def bfs(n):
    res = 0
    visited = [False for i in range(n + 1)]
    dq = deque([])
    
    for i in range(n):
        if visited[i]:
            continue
        res += 1
        
        dq.append(i)
        while dq:
            v = dq.popleft()
            for t in adj_list[v]:
                merg(v,t)
                if visited[t]:
                    continue
                dq.append(t)
                visited[t] = True
    return res
    
def solution(n, computers):
    for cmp, link_tmp in enumerate(computers):
        for i, pt in enumerate(link_tmp):
            if pt == 0 or i == cmp:
                continue
            adj_list[cmp].append(i)
    answer = bfs(n)
    return answer