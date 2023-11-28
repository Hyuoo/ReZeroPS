"""
Solving Date    : 2023.11.25
Solving Time    : 18m
Title           : 트리의 지름
tags            : 그래프 이론, 그래프 탐색, 트리, 깊이 우선 탐색
url             : https://www.acmicpc.net/problem/1967
runtime         : 64 ms
memory          : 34188 KB
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def far(now):
    dist = [-1 for _ in range(n + 1)]
    dist[now] = 0
    q = [[now, 0]]

    while q:
        now, now_dist = q.pop()
        for nxt, nxt_dist in g[now]:
            if dist[nxt]==-1:
                dist[nxt] = now_dist + nxt_dist
                q.append([nxt, dist[nxt]])

    m = max(dist)
    return dist.index(m), m

n = int(input())
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    g[a].append([b, c])
    g[b].append([a, c])

print(far(far(1)[0])[1])

"""
트리의 지름 구하기.

1. 임의의 노드에서 가장 멀리 있는 노드 구하기
2. 1의 노드에서 가장 멀리 있는 노드 까지의 거리가 지름
"""