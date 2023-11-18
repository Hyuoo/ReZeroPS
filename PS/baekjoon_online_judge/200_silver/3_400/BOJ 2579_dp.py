"""
Solving Date    : 2023.10.17
Solving Time    : -
Title           : 계단 오르기
tags            : 다이나믹 프로그래밍
url             : https://www.acmicpc.net/problem/2579
runtime         : 40 ms
memory          : 31120 KB
"""

import sys
input = sys.stdin.readline

n = int(input())
st = [int(input()) for _ in range(n)]+[0]
dp = [0 for _ in range(n+2)]

for i in range(n):
    dp[i] = max(st[i]+st[i-1]+dp[i-3], st[i]+dp[i-2])

print(dp[-3])

"""
정석?은 dp풀이로 아래서부터 max( (-2)+(0), (-3)+(-1)+(0) )
를 그대로 구현.
"""