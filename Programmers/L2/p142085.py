#https://school.programmers.co.kr/learn/courses/30/lessons/142085
'''
디펜스게임.
풀이시간 : 45m
n의 병사, k의 라운드무적권, enemy 각 라운드 적 수

접근방식은 보자마자 누적합, 상위k개 적 수 합
으로 접근

처음 상위k개 적 수 합을 구할 때
그냥 단순히 list로 인덱스찾아넣고 하니 시간초과나서
힙으로 고침.

고치는 과정에서 k개만큼은 무조건 클리어되니까
k부터 시작하려고 했다가 풀렸던 문제들이 안풀려서 그냥 처음부터 다시 함.(idx 0부터)
'''

import heapq
def solution(n, k, enemy):
    #if k>len(enemy):
    #    k = len(enemy)
    
    kk = [0]*k #enemy[:k]
    k_sum = n #n+sum(kk)
    enemy_sum = 0 #sum(enemy[:k])
    clear = 0 #k
    
    for i in enemy: #enemy[k:]:
        enemy_sum += i
        k_sum += i
        heapq.heappush(kk,i)
        k_sum -= heapq.heappop(kk)
        if k_sum >= enemy_sum:
            clear+=1
        else:
            break
    
    return clear
