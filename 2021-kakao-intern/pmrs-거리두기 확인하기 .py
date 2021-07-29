# https://programmers.co.kr/learn/courses/30/lessons/81302

from collections import deque

def search(arr:list, y:int, x:int, w:int) -> int:
    deq = deque()
    deq.append((y,x,w))
    dir = [[1,0],[0,1],[-1,0],[0,-1]]
    visit = {(y,x):True}
    while deq:
        cur = deq.popleft()
        cur_y,cur_x,cur_w = cur

        for p_y, p_x in dir:
            next_y = cur_y + p_y
            next_x = cur_x + p_x
            if cur_w >= 2:
                break
            if next_y >= len(arr) or next_y < 0 or next_x >= len(arr[next_y]) or next_x < 0:
                continue
            data = arr[next_y][next_x]
            if data == 'X' or (next_y,next_x) in visit.keys():
                continue
            if data == 'P':
                return 0
            visit[(next_y,next_x)] = True
            deq.append((next_y,next_x,cur_w+1))

    return 1

def solution(places):
    answer = []
    for place in places:
        place = [list(col) for col in place]
        people = [search(place,r,c,0) for r, col_data in enumerate(place) for c, p in enumerate(col_data) if p == 'P'] + [1]
        answer.append(min(people + [1]))
    return answer