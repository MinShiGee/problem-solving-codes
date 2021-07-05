# https://programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    table = [[0 for j in range(m + 1)] for _ in range(n + 1)]
    water = {(j,i):True for i,j in puddles}
    table[1][0] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (i,j) in water:
                continue
            table[i][j] = (table[i - 1][j] + table[i][j - 1]) % 1000000007

    answer = table[n][m]
    return answer