# https://programmers.co.kr/learn/courses/30/lessons/12900

tmp = 1000000007

def f(n:int, dic:dict):
    global tmp
    if n in dic:
        return dic[n]
    res = 0
    if n % 2 == 1:
        res = f(n//2 + 1, dic) * f(n//2, dic) % tmp + f(n//2, dic) * f(n//2 -1, dic) % tmp
    else:
        res = f(n//2, dic) * f(n//2, dic) % tmp + f(n//2 - 1, dic) * f(n//2 -1, dic) % tmp
    res %= tmp
    dic[n] = res
    return dic[n]

def solution(n):
    dp_dic = {0:0, 1:1, 2:2, 3:3}
    answer = f(n, dp_dic)
    return answer