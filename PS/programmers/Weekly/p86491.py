#LEVEL1
#코딩테스트 연습 > 위클리 챌린지 > 8주차 > 최소직사각형
#https://programmers.co.kr/learn/courses/30/lessons/86491

def solution(s):
    return max(map(max,s))*max(map(min,s))
