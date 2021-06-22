# https://programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    answer = 0
    
    li = []
    for c in s:
        
        if len(li) == 0 or li[-1] != c:
            li.append(c)
            continue

        li.pop()
    
    if len(li) == 0:
        answer = 1
    
    return answer