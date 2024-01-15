"""
Solving Date    : 2024.01.15
Solving Time    : -
Title           : 주사위 굴리기
tags            : 구현, 시뮬레이션
url             : https://www.acmicpc.net/problem/14499
runtime         : 44 ms
memory          : 31120 KB
"""

n, m, x, y, k = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(n)]
dice = [0]*6
rotate_mapping = ["", "310542", "215043", "402351", "152304"]

r = [[], [0, 1], [0, -1], [-1, 0], [1, 0]]
for op in map(int, input().split()):
    i, j = r[op]
    if 0<=(nx:=x+i)<n and 0<=(ny:=y+j)<m:
        x, y = nx, ny
        dice = list(map(lambda x:dice[int(x)], rotate_mapping[op]))
        if board[x][y]:
            dice[-1] = board[x][y]
            board[x][y] = 0
        else:
            board[x][y] = dice[-1]
        print(dice[0])

"""
숏코딩까진 아니고 그냥 주석없애고 적당히 줄인 버전

범위 표현을 n>nx>0<ny<m 이런식으로 한번에 할수도 있더라.
근데 너무 가독성 별로임.
"""