# https://programmers.co.kr/learn/courses/30/lessons/70128

def solution(a, b):
    answer = sum([v1 * v2 for v1, v2 in zip(a,b)])
    return answer