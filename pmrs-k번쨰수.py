# https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = [sorted(array[st-1:ed])[k-1] for st, ed, k in commands]
    return answer