"""
Solving Date    : 2023.11.04
Solving Time    : 29m
Title           : 뱀과 사다리 게임
tags            : 그래프 이론, 그래프 탐색, 너비 우선 탐색
url             : https://www.acmicpc.net/problem/16928
runtime         : 68 ms
memory          : 34072 KB
"""

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
board = [i for i in range(101)]
dp = [999 for _ in range(101)]
dp[1] = 0

for _ in range(n+m):
    a, b = map(int, input().split())
    board[a] = b

q = deque([1])

while q:
    x = q.popleft()
    if x==100:
        break

    if board[x] != x:
        if dp[board[x]] > dp[x]:
            dp[board[x]] = dp[x]
            q.appendleft(board[x])
        continue

    for i in range(1, 7):
        if x+i<101 and dp[x+i] > dp[x]+1:
            dp[x+i] = dp[x]+1
            q.append(x+i)

print(dp[100])

"""
뱀과 사다리 게임.

1. 뱀이든 사다리든 똑같이 a칸을 밟으면 b칸으로 이동한다.
   그래서 구분 없이 입력받아도 된다.
2. 뱀 또는 사다리 칸을 밟으면 강제로 이동한다.
   - 만약 2, 3, 4, 5, 6, 7칸이 전부 50으로 건너뛴다면
     (8 ~ 49) 칸은 아예 못밟는다.
   - 이거 생각안해서 오답을 냈다.

이 두개만 가지고 bfs로 돌리면 풀리는 문제.
"""