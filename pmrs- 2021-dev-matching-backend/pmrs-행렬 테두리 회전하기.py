# https://programmers.co.kr/learn/courses/30/lessons/77485

def solution(rows, columns, queries):
    answer = []
    arr = [[j + columns * i for j in range(1,columns + 1)] for i in range(0,rows)]
    for query in queries:
        move_li = []
        st_y, st_x, ed_y, ed_x = query
        move_li += [(y,x) for y,x in zip([st_y for _ in range(st_x, ed_x)], [x for x in range(st_x, ed_x)])]
        move_li += [(y,x) for y,x in zip([y for y in range(st_y, ed_y)], [ed_x for _ in range(st_y, ed_y)])]
        move_li += [(y,x) for y,x in zip([ed_y for _ in range(st_x, ed_x)], [x for x in range(ed_x, st_x,-1)])]
        move_li += [(y,x) for y,x in zip([y for y in range(ed_y, st_y,-1)], [st_x for _ in range(st_y, ed_y)])]
        
        tmp_pos = move_li[-1]
        tmp_data = arr[tmp_pos[0] - 1][tmp_pos[1] - 1]
        mini = tmp_data
        for pos in move_li:
            cur_y,cur_x = (pos[0]-1, pos[1]-1)
            tmp = arr[cur_y][cur_x]
            arr[cur_y][cur_x] = tmp_data
            tmp_data = tmp
            mini = min(mini, tmp_data)
        answer.append(mini)
    return answer