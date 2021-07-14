# https://programmers.co.kr/learn/courses/30/lessons/67258

def solution(gems):
    dic = {k:0 for k in gems}
    l = len(dic.items())
    st = 0
    ed = 0
    dic[gems[0]] += 1
    gemset = set([gems[0]])
    res = (0, len(gems) - 1, len(gems))
    if l == len(gemset) and res[2] > ed - st:
        res = (st, ed, ed - st)
            
    for gem in gems[1:]:
        ed += 1
        dic[gems[ed]] += 1
        gemset.add(gems[ed])
        while dic[gems[st]] > 1:
            dic[gems[st]] -= 1
            st += 1
        if l == len(gemset) and res[2] > ed - st:
            res = (st, ed, ed - st)
        
    answer = [res[0] + 1,res[1] + 1]
    return answer