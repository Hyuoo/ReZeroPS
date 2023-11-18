"""
Solving Date    : 2023.10.29
Solving Time    : 3m
Title           : 구간 합 구하기 4
tags            : 누적 합
url             : https://www.acmicpc.net/problem/11659
runtime         : 264 ms
memory          : 41116 KB
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ar = [0]+[*map(int, input().split())]

for i in range(n):
    ar[i+1] += ar[i]

for _ in range(m):
    a, b = map(int, input().split())
    print(ar[b]-ar[a-1])

"""
누적 합 개념의 베이직 문제
"""