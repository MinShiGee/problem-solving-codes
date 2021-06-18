# https://programmers.co.kr/learn/courses/30/lessons/72410

def return_char_from_new_id(c):
    if ord('a') <= ord(c) and ord(c) <= ord('z'):
        return c
    if ord('0') <= ord(c) and ord(c) <= ord('9'):
        return c
    if c == '-' or c == '_' or c == '.':
        return c
    return ''

def make_dot_one(id):
    res = ''
    prev = ''
    for c in id:
        if c == '.' and prev == '.':
            continue
        res += prev
        prev = c
    
    res += id[-1]
    
    return res    

def check_1st_last(id):
    res = id
    if len(res) > 0 and res[-1] == '.':
        res = res[:len(res) - 1]
    if len(res) > 0 and res[0] == '.':
        res = res[1:]
    return res

def change_none_id_to_aaa(id):
    if id == '':
        return 'aaa'
    return id

def reduce_id_to_maxlengh(id):
    return id[:15]

def add_id_to_limitlengh(id):
    if len(id) >= 3:
        return id
    return id + id[-1] * (3 - len(id))

def solution(new_id):
    new_id = new_id.lower()
    new_id = ''.join([return_char_from_new_id(c) for c in new_id])
    new_id = make_dot_one(new_id)
    new_id = check_1st_last(new_id)
    new_id = change_none_id_to_aaa(new_id)
    new_id = reduce_id_to_maxlengh(new_id)
    new_id = check_1st_last(new_id)
    new_id = add_id_to_limitlengh(new_id)
    
    answer = new_id
    return answer
