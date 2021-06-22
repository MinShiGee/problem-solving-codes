# https://programmers.co.kr/learn/courses/30/lessons/42747?language=python3

def solution(citations):
    answer = 0
    
    li = [citations.count(d) for d in range(10005)]
    for i in range(1, len(li)):
        li[i] += li[i-1]

    for i in range(0, len(li)):
        if len(citations) - li[i - 1] >= i:
            answer = i 

    return answer

print(solution([3,0,6,1,5]))