# https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    answer = []
    for r in range(1, yellow + 1):
        if yellow % r != 0:
            continue
        
        c = yellow // r
        br = c * 2 + r * 2 + 4
        if br != brown:
            continue

        answer = [c +2, r + 2]
        break
    
    return answer