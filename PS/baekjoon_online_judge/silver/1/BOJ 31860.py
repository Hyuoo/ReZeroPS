"""
Solving Date    : 2024.05.21
Solving Time    : 12m
Title           : 열심히 일하는 중
tags            : 구현, 자료 구조, 시뮬레이션, 우선순위 큐
url             : https://www.acmicpc.net/problem/31860
runtime         : 1916 ms
memory          : 152040 KB
"""

import sys
import heapq
input = sys.stdin.readline

n, m, k = map(int, input().split())

d = []
for _ in range(n):
    heapq.heappush(d, -int(input()))

y = 0
presure = []

while d:
    task = heapq.heappop(d)
    presure.append(y:=((y//2) - task))
    if -(task:=task+m) <= k:
        continue
    heapq.heappush(d, task)

print(len(presure), *presure, sep="\n")