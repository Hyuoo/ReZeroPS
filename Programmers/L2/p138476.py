#https://school.programmers.co.kr/learn/courses/30/lessons/138476
'''
귤 고르기
풀이시간 : 5m

k개의 귤을 최소종류로 담기.
단 한상자.
카운터 세서 큰것부터 뺐다. 끗
'''
from collections import Counter
def solution(k, tangerine):
    answer = 0
    for i in  sorted([i for i in Counter(tangerine).values()],reverse=True):
        k-=i
        answer+=1
        if k<=0:
            break
    return answer
