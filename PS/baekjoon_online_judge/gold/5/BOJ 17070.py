"""
Solving Date    : 2024.02.06
Solving Time    : 41m
Title           : 파이프 옮기기 1
tags            : 다이나믹 프로그래밍, 그래프 이론, 그래프 탐색
url             : https://www.acmicpc.net/problem/17070
runtime         : 44 ms
memory          : 31252 KB
"""

import sys
input = sys.stdin.readline

# (x, y): head position of pipe
# direction: 0 -  1 |  2 \
n = int(input())
ar = [list(map(int, input().split()))+[1] for _ in range(n)]
ar.append([1 for _ in range(n+1)])
dp = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1

for i in range(n):
    for j in range(n):
        hor, ver, diag = map(lambda x:not x, [ar[i][j+1], ar[i+1][j], ar[i+1][j+1]])
        if hor:
            dp[i][j+1][0] += dp[i][j][0] + dp[i][j][2]
        if ver:
            dp[i+1][j][1] += dp[i][j][1] + dp[i][j][2]
        if hor and ver and diag:
            dp[i+1][j+1][2] += sum(dp[i][j])

print(sum(dp[-1][-1]))

"""
재귀방식으로 풀이하려고 했다가 시간초과

dp방식으로 각 파이프 방향별로 가능한 경우를 카운트
무조건 순방향으로만 진행하기 때문에 별다른 조건없이 2중포문을 사용했다.
"""