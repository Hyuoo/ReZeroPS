"""
Solving Date    : 2023.10.30
Solving Time    : 11m
Title           : 문제집
tags            : 자료 구조, 그래프 이론, 우선순위 큐, 위상 정렬, 방향 비순환 그래프
url             : https://www.acmicpc.net/problem/1766
runtime         : 212 ms
memory          : 42696 KB
"""

import sys
input = sys.stdin.readline
import heapq

n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
dep = [0 for i in range(n+1)]
init_set = {i for i in range(1, n+1)}
q = []

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    dep[b] += 1
    init_set.discard(b)

heapq.heapify((q:=list(init_set)))

result = []
while q:
    now = heapq.heappop(q)
    result.append(now)

    for arw in g[now]:
        dep[arw] -= 1
        if dep[arw] == 0:
            heapq.heappush(q, arw)

print(*result)

"""
위상정렬 문제.
개념만 알았지 처음 풀어본 위상정렬

원소를 넣는 큐를 그냥 힙으로만 사용하면 되는 응용문제
"""