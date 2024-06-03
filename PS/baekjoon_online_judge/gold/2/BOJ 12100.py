"""
Solving Date    : 2024.06.03
Solving Time    : 1h 53m
Title           : 2048 (Easy)
tags            : 구현, 브루트포스 알고리즘, 시뮬레이션, 백트래킹
url             : https://www.acmicpc.net/problem/12100
runtime         : 408 ms
memory          : 42268 KB
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
import copy
from typing import Iterable
from enum import Enum

class move(Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4

def progress_one_line_hor(board: list, row: int, s_step: range, e_step: Iterable):
    e = next(e_step)
    is_move_flag = False
    for i in s_step:
        if board[row][i]:
            if board[row][e] == 0:
                board[row][e] = board[row][i]
                board[row][i] = 0
                is_move_flag = True
            elif board[row][e] == board[row][i]:
                board[row][e] *= 2
                e = next(e_step)
                board[row][i] = 0
                is_move_flag = True
            else:
                e = next(e_step)
                if board[row][e] == 0:
                    board[row][e] = board[row][i]
                    board[row][i] = 0
                    is_move_flag = True
    return is_move_flag

def progress_one_line_ver(board: list, col: int, s_step:range, e_step:iter):
    e = next(e_step)
    is_move_flag = False
    for i in s_step:
        if board[i][col]:
            if board[e][col] == 0:
                board[e][col] = board[i][col]
                board[i][col] = 0
                is_move_flag = True
            elif board[e][col] == board[i][col]:
                board[e][col] *= 2
                e = next(e_step)
                board[i][col] = 0
                is_move_flag = True
            else:
                e = next(e_step)
                if board[e][col] == 0:
                    board[e][col] = board[i][col]
                    board[i][col] = 0
                    is_move_flag = True
    return is_move_flag

def direction_select(board: list, d: move):
    if d == move.LEFT:
        s_step = range(1, n, 1)
        e_step = range(0, n, 1)
        func = progress_one_line_hor
    elif d == move.RIGHT:
        s_step = range(n-2, -1, -1)
        e_step = range(n-1, -1, -1)
        func = progress_one_line_hor
    elif d == move.UP:
        s_step = range(1, n, 1)
        e_step = range(0, n, 1)
        func = progress_one_line_ver
    elif d == move.DOWN:
        s_step = range(n-2, -1, -1)
        e_step = range(n-1, -1, -1)
        func = progress_one_line_ver
    
    is_changed = False
    for i in range(n):
        if func(board, i, s_step, iter(e_step)):
            is_changed = True
    
    return is_changed

def foo(board, repeat=5):
    if repeat==0:
        results.extend([j for i in board for j in i])
        return None

    for d in move:
        # print("RUN",d)
        tmp = copy.deepcopy(board)
        c = direction_select(tmp, d)
        if c:
            foo(tmp, repeat=repeat-1)
        # print(*tmp, sep="\n")
    return None

n = int(input())
board = [[*map(int, input().split())] for _ in range(n)]

results = [j for i in board for j in i]
foo(board)
# print(results)
print(max(results))

"""
2048게임 구현해서 5번씩 다 돌려보는거.

시퀀셜한 구현 머리가 안돌아간다.
다른 풀이 짧코드, 100ms대 풀이를 보는것도 머뤼가 안돌아가 이해가 안되렁뤙럼ㄴ러
"""