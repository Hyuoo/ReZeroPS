#LEVEL1
#코딩테스트 연습 > 위클리 챌린지 > 1주차 > 부족한 금액 계산하기
#https://programmers.co.kr/learn/courses/30/lessons/82612

def solution(p, m, c):
    a = p*(c*(c+1)/2)-m
    return a if a>=0 else 0
