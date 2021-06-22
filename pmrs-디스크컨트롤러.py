# https://programmers.co.kr/learn/courses/30/lessons/42627

from queue import PriorityQueue
from collections import deque
import math

def solution(jobs):
    answer = 0
    time = 0
    pq = PriorityQueue()
    deq = deque(sorted(jobs))

    dd = deq.popleft()
    pq.put((dd[1],dd))
    while pq.empty() == False:
        task = pq.get()
        tmp, t_in, t_v = task[0], *task[1]

        if(time < t_in):
            time = t_in
        time += t_v
        answer += time - t_in

        while len(deq) > 0:
            d = deq[0]
            if d[0] > time:
                break
            dd = deq.popleft()
            pq.put((dd[1],dd))
        
        if pq.empty() and len(deq) > 0:
            dd = deq.popleft()
            pq.put((dd[1],dd))
    answer //= len(jobs)
    return answer