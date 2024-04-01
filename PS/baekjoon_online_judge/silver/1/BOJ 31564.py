"""
Solving Date    : 2024.04.01
Solving Time    : 15m
Title           : 육각타일미로 탈출기
tags            : 그래프 이론, 그래프 탐색, 너비 우선 탐색
url             : https://www.acmicpc.net/problem/31564
runtime         : 2532 ms
memory          : 69872 KB
"""

import sys
input = sys.stdin.readline
from collections import deque

n, m, k = map(int, input().split())
maze = [[-1 for _ in range(m)] for _ in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    maze[x][y] = 0

maze[0][0] = 0
q = deque([[0, 0]])
r = [[-1, 0], [0, -1], [0, 1], [1, 0]]

while q:
    x, y = q.popleft()

    if x == n-1 and y == m-1:
        break
    
    for tx, ty in r + ([[-1, 1], [1, 1]] if x%2 else [[-1, -1], [1, -1]]):
        nx, ny = x+tx, y+ty
        if 0<=nx<n and 0<=ny<m and maze[nx][ny]==-1:
            maze[nx][ny] = maze[x][y] + 1
            q.append([nx, ny])
    
print(maze[-1][-1])

"""
단순 너비우선탐색을 육각형 구조로 방문하게끔만 하면 되는 문제.

대각방향의 칸 번호가
행 번호가 홀수 일 때와 짝수 일 때 달라서 이부분만 처리 했다.
"""