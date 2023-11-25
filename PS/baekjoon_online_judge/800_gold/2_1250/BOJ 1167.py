"""
Solving Date    : 2023.11.25
Solving Time    : 15m
Title           : 트리의 지름
tags            : 그래프 이론, 그래프 탐색, 트리, 깊이 우선 탐색
url             : https://www.acmicpc.net/problem/1167
runtime         : 924 ms
memory          : 87276 KB
"""

import sys
input = sys.stdin.readline

def foo(now):
    global n
    visit = {now}
    q = [[now, 0]]
    max_val = 0
    max_idx = 0

    while q:
        now, now_dist = q.pop()
        for nxt, nxt_dist in g[now]:
            if nxt not in visit:
                visit.add(nxt)
                tmp = now_dist + nxt_dist
                if max_val < tmp:
                    max_val = tmp
                    max_idx = nxt
                q.append([nxt, tmp])

    return max_idx, max_val

n = int(input())
g = [[] for _ in range(n+1)]
for _ in range(n):
    i, *tmp = [*map(int, input().split())][:-1]
    for n, d in zip(tmp[::2], tmp[1::2]):
        g[i].append([n, d])

print(foo(foo(1)[0])[1])


"""
트리의 지름 문제
1967번 문제와 그래프 입력 방식만 다르다.

1. 임의 노드에서 가장 먼 노드
2. 1의 노드에서 다시 가장 먼 노드까지의 거리 
"""