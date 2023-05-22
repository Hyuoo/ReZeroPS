#https://school.programmers.co.kr/learn/courses/30/lessons/150368

from itertools import product as c

def solution(users, emoticons):
    answer = []
    l = len(emoticons)
    m = [0,0]
    
    for case in c([10,20,30,40],repeat=l):
        join = 0
        money = 0
        for a,b in users:
            buy = 0
            for i in range(l):
                if a<=case[i]:
                    buy += emoticons[i]*((100-case[i])/100)
            if buy>=b:
                join+=1
            else:
                money += buy

        if m[0]<join:
            m = [join, int(money)]
        elif m[0]==join and m[1]<money:
            m = [join, int(money)]
            
    return m
'''
이모티콘 할인행사
#KDT_코테스터디

시키는대로 구현하는 문제.
모든 할인 케이스가 그렇게 많지않아 브루트포스

풀이접근
1. 할인 케이스 별로 [플러스가입자, 판매액]을 구해서 기준에 맞게 최대값 갱신
2. 각 케이스마다 유저별로 기준 할인율보다 높은 이모티콘 싹 구입.
  2.1 기준 금액보다 크거나 같으면 가입
  2.2 아니면 그대로 다 구입

combi_with_repl 썼었는데 없는 케이스가 있어서
product를 다른분 풀이를 보고 첨알아서 썼다
'''
