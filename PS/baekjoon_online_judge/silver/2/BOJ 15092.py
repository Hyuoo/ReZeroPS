"""
Solving Date    : 2024.09.05
Solving Time    : 16m
Title           : Sheba’s Amoebas
tags            : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
url             : https://www.acmicpc.net/problem/15092
runtime         : 36 ms
memory          : 31120 KB
"""

import sys
input = lambda:sys.stdin.readline().rstrip()

def chk_adj(x, y):
    for v in range(-1, 2):
        for h in range(-1, 2):
            if v == 0 and h == 0: continue
            nx = x+v
            ny = y+h
            if nx < 0 or nx >= n: continue
            if ny < 0 or ny >= m: continue
            if board[nx][ny] == "#":
                return (nx, ny)
    return None  # (-1, -1)

def bfs(x, y):
    global board
    ret = 1

    while ret:
        board[x][y] = "."
        if ret:=chk_adj(x, y):
            x, y = ret

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == "#":
            bfs(i, j)
            cnt += 1

print(cnt)


"""
루프를 만드는 #이 총 몇개인지 세는 문제.
- 무조건 사이클이 성립됨
- 상하좌우대각선 8방으로 "인접"
- "인접"칸에는 2개만 #이 있음이 보장됨.

안전빵 규칙이 많아서 예외생각 안해도 되는 문제.
방문하는 칸의 #을 지우면서 인접 칸을 재귀로 방문한다.
(처음 bfs로 하려고 이름지었다가 풀이는 dfs인게 유머)

인접칸을 계속 방문하면서 지울 경우,
맨 처음엔 인접칸이 2개이긴 하지만 어차피 사이클이 돌아서 한쪽만 체크해도 된다.

그래서 항상 8칸을 모두 체크하는게 아니라 하나만 만나도 함수가 종료되도록 함.


*--탐색방향이 일정해서 특정모양에서 허리가 끊기는 예외는 고려안해도 됨--
**> 인접칸 2개만 있는게 보장되니 그냥 고려안해도 되네
"""
