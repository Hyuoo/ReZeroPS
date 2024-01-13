"""
Solving Date    : 2024.01.08
Solving Time    : 1m
Title           : 가장 큰 증가하는 부분 수열
tags            : 다이나믹 프로그래밍
url             : https://www.acmicpc.net/problem/11055
runtime         : 168 ms
memory          : 31120 KB
"""

n = int(input())
ar = [*map(int, input().split())]
dp = [i for i in ar]

for i in range(1, n):
    for j in range(i):
        if ar[i] > ar[j]:
            dp[i] = max(dp[i], dp[j]+ar[i])

print(max(dp))

"""
lis 아주 사알짝 응용
"""