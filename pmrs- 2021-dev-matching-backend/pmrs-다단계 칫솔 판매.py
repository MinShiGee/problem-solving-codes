# https://programmers.co.kr/learn/courses/30/lessons/77486

def search(adj_list:dict, val_dict:dict, key:str, value:int):
    if key == '-' or value == 0:
        return
    next_value = value//10
    val_dict[key] += value - next_value
    return search(adj_list, val_dict, adj_list[key], next_value)

def solution(enroll, referral, seller, amount):
    val_dict = {k:0 for k in enroll}
    adj_list = {k:v for k,v in zip(enroll, referral)}

    for key, val in zip(seller, amount):
        val *= 100
        search(adj_list, val_dict, key, val)

    answer = [val_dict[key] for key in enroll]
    return answer