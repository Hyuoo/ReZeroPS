"""
Solving Date    :2023.12.19
Solving Time    : 7m
Title           : 네트워크 연결
tags            : 그래프 이론, 최소 스패닝 트리
url             : https://www.acmicpc.net/problem/1922
runtime         : 456 ms
memory          : 68312 KB
"""

import sys
input = sys.stdin.readline
import heapq

n = int(input())
m = int(input())

g = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append([b, c])
    g[b].append([a, c])

q = [[dist, 1, to] for to, dist in g[1]]
visited = [False for _ in range(n+1)]
visited[1] = True
ans = 0

heapq.heapify(q)
n -= 1
while n:
    dist, src, dest = heapq.heappop(q)
    if not visited[dest]:
        visited[dest] = True
        ans += dist
        n -= 1

        for nxt, nxt_dist in g[dest]:
            if not visited[nxt]:
                heapq.heappush(q, [nxt_dist, dest, nxt])

print(ans)

"""
최소스패닝트리 기본 문제

1197번 문제와 완전히 동일한 코드로 풀린다.
prim 알고리즘으로 다시 풀어봤음.
"""