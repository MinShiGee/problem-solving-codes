# https://programmers.co.kr/learn/courses/30/lessons/42861

def find_par(par:list, n):
    if n == par[n]:
        return n
    par[n] = find_par(par, par[n])
    return par[n]

def merg(par:list, a, b):
    if a > b:
        par[b] = a
    else:
        par[a] = b

def solution(n, costs):
    answer = 0
    edge = sorted(costs, key=lambda x: x[2])
    visited = [i for i in range(n)]
    for v1, v2, cost in edge:
        v1 = find_par(visited, v1)
        v2 = find_par(visited, v2)
        if visited[v1] == visited[v2]:
            continue
        merg(visited,v1,v2)
        answer+=cost
    return answer