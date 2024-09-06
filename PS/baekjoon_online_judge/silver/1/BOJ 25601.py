"""
Solving Date    : 2024.09.06
Solving Time    : 11m
Title           : 자바의 형변환
tags            : 자료 구조, 그래프 이론, 그래프 탐색, 트리, 해시를 사용한 집합과 맵
url             : https://www.acmicpc.net/problem/25601
runtime         : 128 ms
memory          : 51256 KB
"""

import sys
input = sys.stdin.readline

def chk_p(t, target):
    while t:
        t = g.get(t, "")
        if t == target:
            return 1
    return 0

n = int(input())
g = {}

for _ in range(n-1):
    child, parent = input().split()
    g[child] = parent

a, b = input().split()

print(chk_p(a, b) or chk_p(b, a))

"""

"""