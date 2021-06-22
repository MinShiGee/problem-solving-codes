# https://programmers.co.kr/learn/courses/30/lessons/42628

import bisect

def solution(operations):
    li = []
    for data in operations:
        print(li)
        op, code = data.split(' ')
        print(op, code)
        if op == 'I':
            bisect.insort(li,int(code))
            continue
        if len(li) <= 0:
            continue
        if code == '1':
            li.pop()
            continue
        li = li[1:]
        
    answer = [0,0]
    if len(li) > 0:
        answer = [li[-1],li[0]]
    return answer