# https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    li = sorted(phone_book)
    
    for prev, cur in zip(li[:-1],li[1:]):
        if cur.startswith(prev):
            return False
        
    return True