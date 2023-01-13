#코딩테스트 연습 2018 KAKAO BLIND RECRUITMENT [1차] 다트 게임
'''
아래처럼 정규식으로 풀었다가, 다른 풀이 보고 소괄호로 그룹화가 된다는걸 알아서 아래 코드로 수정.
import re
def solution(dartResult):
    score = [0,0,0]
    m = re.findall("[0-9]*?\D[^0-9]?",dartResult)
    mul={"S":1,"D":2,"T":3}
    for i, s in enumerate(m):
        j=0
        if s[0]+s[1]=="10":
            score[i] = 10
            j+=2
        else:
            score[i] = int(s[0])
            j+=1
        score[i] **= mul[s[j]]
        j+=1
        if len(s)>j:
            if s[j]=="*":
                score[i]*=2
                if i-1>=0:
                    score[i-1]*=2
            elif s[j]=="#":
                score[i]*=-1
    return sum(score)
'''
import re
def solution(dartResult):
    score = [0,0,0]
    mul={"S":1,"D":2,"T":3}
    for i, s in enumerate(re.findall("([0-9]+)(\D)([*#]?)",dartResult)):
        score[i] = int(s[0])**mul[s[1]]
        if s[2]=="*":
            score[i]*=2
            if i-1>=0:
                score[i-1]*=2
        elif s[2]=="#":
            score[i]*=-1
    return sum(score)
