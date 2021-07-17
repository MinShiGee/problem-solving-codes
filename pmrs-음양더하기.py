# https://programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    answer = sum([n * (1 if k == True else -1) for n, k in zip(absolutes, signs)])
    return answer