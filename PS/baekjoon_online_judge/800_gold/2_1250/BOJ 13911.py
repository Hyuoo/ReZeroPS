"""
Solving Date    : 2023.10.14
Solving Time    : 51m
Title           : 집 구하기
tags            : 그래프 이론, 데이크스트라, 최단 경로
url             : https://www.acmicpc.net/problem/13911
runtime         : 2032 ms
memory          : 119132 KB
"""

import sys
input = sys.stdin.readline
import heapq
INF = 300000*10000

def dijkstra(g, ready, limit):
    n = len(g)
    shortest = [INF for _ in range(n)]
    q = []
    for s in ready:
        shortest[s] = 0
        q.append((0,s))

    while q:
        dist, now = heapq.heappop(q)
        if shortest[now] < dist:
            continue

        for nxt, nxt_dist in g[now]:
            tot = dist + nxt_dist
            if tot<=limit and shortest[nxt] > tot:
                shortest[nxt] = tot
                heapq.heappush(q, (tot, nxt))

    return shortest


s_input = lambda:map(int, input().split())

v, e = s_input()
g = [[] for _ in range(v+1)]

# mk graph
for _ in range(e):
    u, v, w = s_input()
    g[u].append([v, w])
    g[v].append([u, w])

# mc-do
m, x = s_input()
M = list(s_input())

# sta-ba
s, y = s_input()
S = list(s_input())

ans = INF
for mc, su in zip(dijkstra(g, M, x), dijkstra(g, S, y)):
    if mc and su:
        ans = min(mc+su, ans)

print(ans if ans!=INF else -1)

"""
그래프 상에서 (맥날, 스벅) 노드에 대해서
각 노드 별 일정거리 이하를 만족하면서
(맥날, 스벅) 거리 합이 최소인 지점(최소거리값) 찾기.

접근:
맥날 최단거리 리스트를 만들고
스벅 최단거리 리스트를 만들고
두 최단거리를 더해보면서 조건에 맞는 최소거리 찾기.


- 첫 풀이 메모리초과
    - 인접행렬로 했어서 인접리스트로 변경
- 시간초과
    - 그냥 큐를 쓴 걸 우선순위 큐로 변경
이후 성공했지만,
 

"""