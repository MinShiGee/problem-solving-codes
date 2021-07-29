# https://programmers.co.kr/learn/courses/30/lessons/81301

def solution(s:str):
    answer = ''
    li = ['0','1','2','3','4','5','6','7','8','9','zero','one','two','three','four','five','six','seven','eight','nine',]
    while(len(s) > 0):
        for i, d in enumerate(li):
            if s.startswith(d) == False:
                continue
            answer += li[i % 10]
            s = s[len(d):len(s)]
            break

    return int(answer)

print(solution("nineninenine9999"))