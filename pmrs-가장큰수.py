# https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    res = ''.join(sorted([str(data) for data in numbers], key=lambda x: x*5, reverse=True))
    if res[0] == '0':
        res = '0'
    return res
