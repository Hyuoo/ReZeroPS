"""
Solving Date    : 2024.09.18
Solving Time    : 6m
Title           : 논리학 교수
tags            : 애드 혹
url             : https://www.acmicpc.net/problem/1813
runtime         : 32 ms
memory          : 31120 KB
"""

n = int(input())
ar = [0 for _ in range(51)]

for i in map(int, input().split()):
    ar[i] += 1

for i in range(n, 0, -1):
    if ar[i] == i:
        print(i)
        break
else:
    print(-1 if ar[0] else 0)