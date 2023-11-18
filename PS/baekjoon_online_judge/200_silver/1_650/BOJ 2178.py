"""
Solving Date    : 2023.10.17
Solving Time    : 15m
Title           : 미로 탐색
tags            : 그래프 이론, 그래프 탐색, 너비 우선 탐색
url             : https://www.acmicpc.net/problem/2178
runtime         : 84 ms
memory          : 34060 KB
"""

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
maze = [[*map(int, list(input().rstrip()))] for _ in range(n)]

q = deque([[0, 0, 1]])
r = [[1, 0], [-1, 0], [0, 1], [0, -1]]

while q:
    x, y, dist = q.popleft()
    if maze[x][y]!=1:
        continue
    if x==n-1 and y==m-1:
        print(dist)
        break
    maze[x][y] = dist
    for i, j in r:
        nx = x+i
        ny = y+j
        if nx>=0 and nx<n and ny>=0 and ny<m and maze[nx][ny]==1:
            q.append([nx, ny, dist+1])

"""
단순히 bfs하면 되는 문제.

길이 1(True) 못가는곳이 0(False)라서
별도로 길 판별을 안해도 되어 편함.

그리고 각 거리로 기존 맵을 갱신해서
중복방문 방지.

[0, 0]의 경우엔 바로 되돌아 오긴 하나(거리3이 됨), 풀이에 영향 없음.

=== 아래와 같은 식으로
=== 다음 칸에 거리를 누적시켜 더해주는 방식으로
=== 큐에 거리값을 계속 사용하지 않아도 됨.
while q:
    x, y = q.popleft()
    if x==n-1 and y==m-1:
        print(maze[x][y])
        break

    for i, j in r:
        nx = x+i
        ny = y+j
        if nx>=0 and nx<n and ny>=0 and ny<m and maze[nx][ny]==1:
            maze[nx][ny] += maze[x][y]
            q.append([nx, ny])
"""