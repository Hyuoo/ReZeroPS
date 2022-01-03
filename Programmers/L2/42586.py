#코딩테스트 연습 > 스택/큐 > 기능개발
#https://programmers.co.kr/learn/courses/30/lessons/42586

def solution(prg, spd):
    answer = []
    idx = 0
    leng = len(prg)
    while(idx<leng):
        for i in range(idx,leng):
            prg[i] += spd[i]
        release = 0
        while(idx<leng and prg[idx]>=100):
            idx += 1
            release += 1
            continue
        if(release):
            answer.append(release)
    return answer
