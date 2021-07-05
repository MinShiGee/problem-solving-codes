# https://programmers.co.kr/learn/courses/30/lessons/43105
import copy

def solution(triangle):
    table = copy.deepcopy(triangle)
    for i, li in enumerate(triangle[:-1]):
        for j, _ in enumerate(li):
            table[i+1][j] = max([table[i+1][j], triangle[i+1][j] + table[i][j]])
            table[i+1][j+1] = max([table[i+1][j+1], triangle[i+1][j+1] + table[i][j]])
    answer = max(table[len(triangle) - 1])
    return answer