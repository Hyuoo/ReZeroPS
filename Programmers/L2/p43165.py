#코딩테스트 연습 > 깊이/너비 우선 탐색(DFS/BFS) > 타겟 넘버
#https://programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    n=len(numbers)
    ar=[0]*(2**(n+1))
    idx=2
    for i in range(n):
        for j in range(2**(i+1)):
            ar[idx]=ar[idx//2]+numbers[i]*(1 if idx%2 else -1)
            idx+=1
    return ar[2**n:].count(target)
