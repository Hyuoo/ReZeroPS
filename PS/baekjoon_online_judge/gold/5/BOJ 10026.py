"""
Solving Date    : 2024.01.30
Solving Time    : 14m
Title           : 적록색약
tags            : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
url             : https://www.acmicpc.net/problem/10026
runtime         : 92 ms
memory          : 31728 KB
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
import copy

r = [[0, 1], [0, -1], [1, 0], [-1, 0]]
def dfs(fig, x, y, foo:callable):
    global n
    tmp = fig[x][y]
    fig[x][y] = None
    for i, j in r:
        nx = x+i
        ny = y+j
        if 0<=nx<n and 0<=ny<n and fig[nx][ny] and foo(tmp, fig[nx][ny]):
            dfs(fig, nx, ny, foo)

n = int(input())
origin = [[*input()] for _ in range(n)]
rg_blindness = copy.deepcopy(origin)
answer = [0, 0]

for i in range(n):
    for j in range(n):
        if origin[i][j]:
            dfs(origin, i, j, (lambda a, b: a==b))
            answer[0] += 1
        
        if rg_blindness[i][j]:
            dfs(rg_blindness, i, j, (lambda a, b: (a!="B")==(b!="B")))
            answer[1] += 1

print(*answer)

"""
R, G를 하나로 다 교체하고 순회하기 싫어서
함수를 생성해 기준으로 탐색하도록 했다.
"""