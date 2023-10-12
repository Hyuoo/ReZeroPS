"""
Solving Date    : 2023.10.12
Solving Time    : -
Title           : 우유 도시
tags            : 다이나믹 프로그래밍
url             : https://www.acmicpc.net/problem/14722
runtime         : 692 ms
memory          : 38880 KB
"""

import sys
input = sys.stdin.readline

n = int(input())
ar = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n+1)]

for i in range(n):
    for j in range(n):
        dp[j+1] = max(dp[j], dp[j+1])
        if dp[j+1]%3 == ar[i][j]:
            dp[j+1] += 1

print(dp[-1])

"""
다른 풀이 보고

어 굳이 딸바초 나눠서 다 할 필요가 없구나 맞네..
(마실 순서가 왔는데 해당 칸이면 무조건 마셔야 이득)

그리고 우유를 마시는(++) 경우를
현재값의 3나머지가 현재 칸이면 마실 수 있음.
"""