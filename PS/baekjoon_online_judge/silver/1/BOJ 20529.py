"""
Solving Date    : 2023.10.22
Solving Time    : 40m
Title           : 가장 가까운 세 사람의 심리적 거리
tags            : 브루트포스 알고리즘, 비둘기집 원리
url             : https://www.acmicpc.net/problem/20529
runtime         : 212 ms
memory          : 38536 KB
"""

import sys
input = sys.stdin.readline

def cmp(a, b):
    return sum(a[i]!=b[i] for i in range(4))

def get_dist(i, j, k):
    if not dist[i][j]:
        dist[i][j] = cmp(ar[i], ar[j])
    if not dist[j][k]:
        dist[j][k] = cmp(ar[j], ar[k])
    if not dist[i][k]:
        dist[i][k] = cmp(ar[i], ar[k])

    return dist[i][j] + dist[j][k] + dist[i][k]

for _ in range(int(input())):
    n = int(input())
    ar = input().split()
    if n>32:
        print(0)
        continue
    dist = [[0 for _ in range(n)] for _ in range(n)]

    ans = 999999
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                ans = min(ans, get_dist(i,j,k))
    print(ans)

"""
전혀 처음풀어보는 유형
힌트없이 풀려고만 하다가 당최 방법이 생각이 안나서 치팅함.

문제 분류의 '비둘기집 원리'라는게
n개 배열에 n개보다 많은 데이터가 들어갈 경우
응당 무조건 1칸은 겹친다는 사실을 이용해서
- 많은 비교가 일어날 경우를 아예 0으로 둘 수 있다.
    - MBTI 종류가 16개라서 32개를 초과 한 입력값이면
    무조건 한곳에 3개는 들어가있다는 것이므로
    **거리가 0**

특정 조건으로 이후 탐색을 싹다 쳐내는것밖에 생각을 안해봐서
이런쪽으로 생각을 전혀 못했다. 
"""