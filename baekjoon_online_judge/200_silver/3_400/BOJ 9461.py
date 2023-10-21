"""
Solving Date    : 2023.10.21
Solving Time    : 9m
Title           : 파도반 수열
tags            : 수학, 다이나믹 프로그래밍
url             : https://www.acmicpc.net/problem/9461
runtime         : 44 ms
memory          : 31120 KB
"""

# 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, 28, 37
#  +0  +0 +1 +0 +1 +1 +1 +2 +2 +3 +4  +5  +7  +9
#                           -5 -5 -5  -5  -5  -5
p = [0, 1, 1, 1, 2]
for _ in range(96):
    p.append(p[-1]+p[-5])

print(*(p[int(input())] for _ in range(int(input()))), sep="\n")

"""
직접 해봐서 규칙성 찾기.
"""