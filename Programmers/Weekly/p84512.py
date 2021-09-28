#LEVEL2
#코딩테스트 연습 > 위클리 챌린지 > 5주차 > 모음 사전
#https://programmers.co.kr/learn/courses/30/lessons/84512

def solution(word):
    answer = 0
    alph = {'A':0,'E':1,'I':2,'O':3,'U':4}
    i = 781
    for c in word:
        answer += i*alph[c]+1
        i = (i-1)//5
    return answer
