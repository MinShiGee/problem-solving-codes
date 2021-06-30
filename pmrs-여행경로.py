# https://programmers.co.kr/learn/courses/30/lessons/43164

adj_list = []
hash_table = {}
edge_count = 0

def dfs(cur_list:list, dep:int):
    global edge_count

    if dep == edge_count:
        return cur_list

    cur = cur_list[-1]
    for i, tu in enumerate(adj_list[cur]):
        t, b = tu
        if b == True:
            continue
        adj_list[cur][i] = (t, True)
        cur_list.append(t)
        tmp = dfs(cur_list, dep + 1)
        if not tmp == None:
            return tmp

        cur_list.pop()
        adj_list[cur][i] = (t, False)


def solution(tickets):
    global adj_list
    global hash_table
    global edge_count

    tickets_set = []
    for t in tickets:
        tickets_set += t
    tickets_set = set(tickets_set)
    adj_list = [[] for i in range(len(tickets_set))]
    hash_table = {k:i for i, k in enumerate(tickets_set)}
    rev_hash_table = {v:k for k, v in hash_table.items()}

    for k1, k2 in tickets:
        v1 = hash_table[k1]
        v2 = hash_table[k2]
        edge_count+=1
        adj_list[v1].append((v2,False))
    adj_list = [sorted(li,key=lambda x:rev_hash_table[x[0]]) for li in adj_list]

    answer = [rev_hash_table[data] for data in dfs([hash_table['ICN']], 0)]
    return answer
