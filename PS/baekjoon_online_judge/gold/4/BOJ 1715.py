"""
Solving Date    : 2025.04.17
Solving Time    : 12m
Title           : 카드 정렬하기
tags            : 자료 구조, 그리디 알고리즘, 우선순위 큐
url             : https://www.acmicpc.net/problem/1715
runtime         : 148 ms
memory          : 36292 KB
"""

import sys
input = sys.stdin.readline
import heapq

n = int(input())
q = [int(input()) for _ in range(n)]
heapq.heapify(q)

ans = 0
while len(q)>1:
    t = heapq.heappop(q) + heapq.heappop(q)
    heapq.heappush(q, t)
    ans += t

print(ans)