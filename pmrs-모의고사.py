# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    li = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    ans = [0,0,0]
    for i in range(3):
        for j, v in enumerate(answers):
            if li[i][j % len(li[i])] != v:
                continue
            ans[i] += 1
    answer = [(1,ans[0]),(2,ans[1]),(3,ans[2])]
    answer.sort(key=lambda x: -x[1])
    res = [answer[0][0]]
    
    if answer[0][1] == answer[1][1]:
        res.append(answer[1][0])
        if answer[1][1] == answer[2][1]:
            res.append(answer[2][0])
            
    return res