"""
Solving Date    :2023.12.19
Solving Time    : 10m
Title           : 최소 스패닝 트리
tags            : 그래프 이론, 최소 스패닝 트리
url             : https://www.acmicpc.net/problem/1197
runtime         : 336 ms
memory          : 51748 KB
"""

import sys
input = sys.stdin.readline

def union(a, b):
    pa = find(a)
    pb = find(b)
    if pa < pb: parents[pb] = a
    else: parents[pa] = b

def find(a):
    if parents[a] == a: return a
    parents[a] = find(parents[a])
    return parents[a]

v, e = map(int, input().split())
parents = [i for i in range(v+1)]
edges = []
ans = 0

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append([c, a, b])

edges.sort()

v -= 1
for dist, src, dest in edges:
    a = find(src)
    b = find(dest)
    if a != b:
        ans += dist
        union(a, b)
        v -= 1
        if v == 0:
            break

print(ans)

"""
최소스패닝트리 기본 문제

먼저, edges를 heapq로 써서 풀었었는데
유동적으로 삽입 삭제와 정렬이 이루어지는 리스트가 아니라서
한번에 넣고,
sort한번해서 위 코드처럼 푸는게 더 빠르다.

(1922번 문제와 완전히 동일한 문제)

- reverse없애고 while문 -> for문(v탈출조건)
    - 336ms -> 320ms
- 간선정보를 리스트 -> 튜플로 바꿨더니 성능 향상
    - 320ms -> 252ms

(코드는 튜플 아닌거)
"""