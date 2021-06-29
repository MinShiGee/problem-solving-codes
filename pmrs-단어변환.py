# https://programmers.co.kr/learn/courses/30/lessons/43163

def solution(begin, target, words):

    if not target in words:
        return 0

    words.append(begin)
    st = len(words) - 1
    ed = words.index(target)
    adj_list = [[] for i in range(len(words))]

    for i in range(len(words) - 1):
        v = words[i]
        for j in range(i+1, len(words)):
            t = words[j]
            cnt = 0
            for a, b in zip(v, t):
                if(a == b):
                    continue
                cnt+= 1
            if cnt != 1:
                continue 
            adj_list[i].append(j)
            adj_list[j].append(i)

    visited = [False for i in range(len(words))]
    weight = [0 for i in range(len(words))]
    que = [st]
    visited[st] = True
    while que:
        v = que.pop()
        for t in adj_list[v]:
            if visited[t]:
                continue
            visited[t] = True
            weight[t] = weight[v] + 1
            que.append(t)

    answer = weight[ed]
    return answer