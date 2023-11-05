"""
Solving Date    : 2023.11.04
Solving Time    : -
Title           : 뱀과 사다리 게임
tags            : 그래프 이론, 그래프 탐색, 너비 우선 탐색
url             : https://www.acmicpc.net/problem/16928
runtime         : 72 ms
memory          : 34200 KB
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

    for i in range(1, 7):
        nxt = x+i
        if nxt<101:
            if board[nxt] != nxt:
                nxt = board[nxt]
            if dp[nxt] > dp[x]+1:
                dp[nxt] = dp[x]+1
                q.append(nxt)


print(dp[100])

"""
논리 가독성 높인 버전?

bfs 내부만 살짝 바꿈. 
- 뱀과 사다리를 타는 경우와 아닌경우의
  논리 및 코드 일반화
"""