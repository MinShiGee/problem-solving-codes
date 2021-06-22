# https://programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    
    dic = { k:[]  for k in set([v for d, v in clothes])}
    for v,k in clothes:
        dic[k].append(v)
    
    answer = 1
    for k in dic.keys():
        answer *= (len(dic[k]) + 1)
        
    answer -= 1
    return answer