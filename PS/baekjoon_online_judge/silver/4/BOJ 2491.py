"""
Solving Date    : 2024.01.08
Solving Time    : -
Title           : 수열
tags            : 구현, 다이나믹 프로그래밍
url             : https://www.acmicpc.net/problem/2491
runtime         : 108 ms
memory          : 32684 KB
"""

n = int(input())
ar = [*map(int, input().split())]

ans = 1
count_up = 1
count_down = 1
for i in range(1, n):
    count_up += 1
    count_down += 1
    if ar[i-1] < ar[i]: count_down = 1
    if ar[i-1] > ar[i]: count_up = 1
    ans = max(ans, count_up, count_down)

print(ans)
