"""
Solving Date    : 2023.12.20
Solving Time    : 약 40m
Title           : 별자리 만들기
tags            : 그래프 이론, 최소 스패닝 트리
url             : https://www.acmicpc.net/problem/4386
runtime         : 52 ms
memory          : 33188 KB
"""

import sys
input = sys.stdin.readline
import heapq

star_dist = lambda a, b: ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

n = int(input())
stars = []

for _ in range(n):
    x, y = map(float, input().split())
    stars.append([x, y])

visited = [False for _ in range(n)]
visited[0] = True

q = [[star_dist(stars[0], stars[i]), i] for i in range(1, n)]
heapq.heapify(q)

star_link = 0
ans = 0.0

while star_link != n - 1:
    dist, dest = heapq.heappop(q)
    if not visited[dest]:
        visited[dest] = True
        ans += dist
        star_link += 1

        for i in range(n):
            if not visited[i]:
                heapq.heappush(q, [star_dist(stars[dest], stars[i]), i])

print(round(ans, 2))

"""
별이 최대 100개까지라서
99번 돌면서 방문안한 100개중 최소인거 찾고
체크하면서 반복해서 풀려고 했는데, 실패
-> 새로운 간선 추가를 전체 간선 풀에 추가해서 했어야 했는데,
-> 항상 현재위치를 기준으로 최소거리로 이동해서 실패함.

그래서 그냥 프림 알고리즘 그대로 구현했다. 
"""