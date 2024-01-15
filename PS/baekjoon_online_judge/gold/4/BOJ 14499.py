"""
Solving Date    : 2024.01.15
Solving Time    : 22m
Title           : 주사위 굴리기
tags            : 구현, 시뮬레이션
url             : https://www.acmicpc.net/problem/14499
runtime         : 44 ms
memory          : 31120 KB
"""

import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
board = []  # 0~9
dice = [0]*6  # top:0, bot:5
rotate_mapping = {
    1: [3, 1, 0, 5, 4, 2],
    2: [2, 1, 5, 0, 4, 3],
    3: [4, 0, 2, 3, 5, 1],
    4: [1, 5, 2, 3, 0, 4],
}
ans = []

for _ in range(n):
    tmp = [*map(int, input().split())]
    board.append(tmp)

# print(*board, sep="\n")

# 동서북남: 1234
r = [[], [0, 1], [0, -1], [-1, 0], [1, 0]]
for op in map(int, input().split()):
    i, j = r[op]
    nx, ny = x+i, y+j
    if nx<0 or nx>=n or ny<0 or ny>=m:
        continue
    x, y = nx, ny

    dice = list(map(lambda x:dice[x], rotate_mapping[op]))
    if board[x][y]:
        dice[-1] = board[x][y]
        board[x][y] = 0
    else:
        board[x][y] = dice[-1]
    ans.append(dice[0])  # , dice[-1])

print(*ans, sep="\n")

"""
문제 재밌넹

주사위 굴러가는걸 매핑해서 쉽게 풀었다.
항상 0은 윗면, -1은 바닥면이 된다.
"""