"""
Solving Date    : 2023.10.30
Solving Time    : 6m
Title           : 연결 요소의 개수
tags            : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
url             : https://www.acmicpc.net/problem/11724
runtime         : 604
memory          : 31120
"""

import sys
input = sys.stdin.readline

def f(x):
    if x==p[x]: return x
    p[x] = f(p[x])
    return p[x]

def u(a, b):
    if (ap := f(a)) < (bp := f(b)):
        p[bp] = ap
    else:
        p[ap] = bp

n, m = map(int, input().split())
p = [i for i in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    u(a, b)

print(len({f(i) for i in range(1, n+1)}))

"""
엥 카테고리가 그래프탐색이네

보자마자 유니온파인드 생각나서 유니온파인드로 풀었다.

풀이:
0. union-find 함수 구현
1. 입력되는 정점 2개씩 union 해주고
2. 마지막에 순회 돌면서 모든 find로 루트노드 셋 만들어서 개수 세기
"""