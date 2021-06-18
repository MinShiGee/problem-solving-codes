# https://programmers.co.kr/learn/courses/30/lessons/62048

import math

def solution(w,h):
    
    total = w * h
    gcd = math.gcd(w,h)
    answer = total - h - w + gcd
    
    return answer