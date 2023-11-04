"""
Solving Date    : 2023.11.03
Solving Time    : 30m
Title           : 장난감 조립
tags            : 다이나믹 프로그래밍, 그래프 이론, 위상 정렬, 방향 비순환 그래프
url             : https://www.acmicpc.net/problem/2637
runtime         : 68 ms
memory          : 34044 KB
"""

from collections import deque

n = int(input())
m = int(input())

g = [[] for _ in range(n+1)]
fork = [0 for _ in range(n)]
need_parts = [0 for _ in range(n)]+[1]

for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append([b, c])
    fork[b] += 1

q = deque([n])
basic_parts = []

while q:
    now = q.popleft()

    is_basic = True
    for nxt, need in g[now]:
        is_basic = False
        need_parts[nxt] += need_parts[now] * need
        fork[nxt] -= 1
        if fork[nxt] == 0:
            q.append(nxt)
    if is_basic:
        basic_parts.append(now)

for i in sorted(basic_parts):
    print(i, need_parts[i])