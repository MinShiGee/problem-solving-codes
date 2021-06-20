# https://programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    
    answer = 0
    mx = max(times)
    
    l = 0
    r = (n + 1) * mx
    
    while l <= r:
        mid = (l + r) // 2
        
        t = 0
        for d in times:
            t += mid // d
            if t >= n:
                answer = mid
                r = mid - 1
                break
                
        if t < n:
            l = mid + 1
            
    return answer