"""
Solving Date    : 2024.02.16
Solving Time    : 20m
Title           : 욱제가 풀어야 하는 문제
tags            : 다이나믹 프로그래밍
url             : https://www.acmicpc.net/problem/18249
runtime         : 248 ms
memory          : 43332 KB
"""

import sys
input = sys.stdin.readline

a, b = 1, 0
ans = [0 for _ in range(191230)]
for i in range(191230):
    ans[i] = a
    a, b = (a+b)%1000000007, a

print(*[ans[int(input())] for tc in range(int(input()))], sep="\n")

"""
dp를 사용해서
- dp[1], dp[2] = 1, 2
- dp[n] = dp[n-1] + dp[n-2]
로 풀어도 동일하다. (대충 수학적으로 동일하단 설명)

시간이 왤케 팍팍함
- print를 한번에 안하고 나눠서 하면 시간초과.
- list를 한번에 안만들고 append하면 시간초과.

근데 또 dp로 풀고, append하고 따로출력해도
더 빠른경우도 있고 더 느린경우도 있고. 컨디션 문젠 것 같다.
"""