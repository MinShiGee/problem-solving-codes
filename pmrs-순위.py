# https://programmers.co.kr/learn/courses/30/lessons/49191

from queue import Queue

def solve(adj_list:list, vers_cnt:list, n):
    res = []
    vers_list = [[i] for i in range(n + 1)]
    q = Queue()
    for ver, val in zip(range(1, n+1), vers_cnt[1:]):
        if val > 0:
            continue
        q.put(ver)

    while q.empty() == False:
        ver = q.get()
        for to in adj_list[ver]:
            vers_cnt[to] -= 1
            if vers_cnt[to] == 0:
                q.put(to)
            vers_list[to] = list(set(vers_list[to] + vers_list[ver]))
    res = [len(data)-1 for data in vers_list]

    return res

def solution(n, results):
    answer = 0
    adj_list_towin = [[] for i in range(n + 1)]
    adj_list_tolose = [[] for i in range(n + 1)]
    vers_win = [0 for i in range(n + 1)]
    vers_lose = [0 for i in range(n + 1)]
    
    for w, l in  results:
        adj_list_towin[l].append(w)
        adj_list_tolose[w].append(l)
        vers_win[w] += 1
        vers_lose[l] += 1
    
    res_win = solve(adj_list_towin, vers_win, n)
    res_lose = solve(adj_list_tolose, vers_lose, n)

    for v in range(1, n + 1):
        val = res_lose[v] + res_win[v]
        if val != n - 1:
            continue
        answer += 1
    return answer