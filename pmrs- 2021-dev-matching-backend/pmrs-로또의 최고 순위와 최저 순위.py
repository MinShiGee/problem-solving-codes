# https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    win_nums = set(win_nums)
    lottos = [data for data in lottos if data != 0]
    correct_cnt = len([d for d in lottos if d in win_nums])
    b_res = 7 - (max(correct_cnt + 6 - len(lottos), 1))
    w_res = 7 - (max(correct_cnt, 1))
    answer = [b_res, w_res]
    return answer
