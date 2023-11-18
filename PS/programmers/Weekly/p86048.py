#LEVEL1
#코딩테스트 연습 > 위클리 챌린지 > 7주차 > 입실 퇴실
#https://programmers.co.kr/learn/courses/30/lessons/86048

def meet(answer, stay, a):
    for i,n in enumerate(stay):
        if(n):
            answer[i]+=1
            answer[a]+=1

def solution(enter, leave):
    n = len(enter)
    stay =[0]*n
    answer=[0]*n
    leave+=[-1]
    for en in enter:
        meet(answer, stay, en-1)
        stay[en-1]=en
        while(leave[0] in stay):
            stay[leave[0]-1]=0
            del(leave[0])
    
    return answer
