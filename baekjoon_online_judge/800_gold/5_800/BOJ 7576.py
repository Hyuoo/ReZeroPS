"""
Solving Date    : 2023.09.14
Solving Time    : 20m
Title           : 토마토
tags            : 그래프 이론, 그래프 탐색, 너비 우선 탐색
url             : https://www.acmicpc.net/problem/7576
runtime         : 2308 ms
memory          : 98536 KB
"""

from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())

tomato = [[*map(int, input().split())] for _ in range(n)]

q = deque()
notto = 0
maxto = 0

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append((i, j))
        elif tomato[i][j] == 0:
            notto += 1

d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
while q:
    x, y = q.popleft()
    maxto = max(maxto, tomato[x][y])

    for i, j in d:
        nx = x + i
        ny = y + j
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if tomato[nx][ny] == 0:
            tomato[nx][ny] = tomato[x][y] + 1
            q.append((nx, ny))
            notto -= 1

print(-1 if notto else maxto - 1)

"""
BFS를 이용해서 모든 토마토가 익는 날짜 계산

시간이 1500ms 정도로 걸리는 코드들이 많은데
내껀 왜 2300ms가 최선이지?
판박이 코드를 해도 2284ms가 나온다.. 왜?
- 안익은거 있는지 검사, max값 검사 등을 다 끝부분에 분리해서 해도 큰 차이 안나는디

암튼.

큐 사용한 bfs로
최초 토마토 위치마다 시작해서, 인근 안익토(0)는 +1값으로 갱신
"""