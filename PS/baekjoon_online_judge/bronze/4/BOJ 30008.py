"""
Solving Date    : 2023.11.27
Solving Time    : 4m
Title           : 준영이의 등급
tags            : 수학, 구현, 사칙연산, 많은 조건 분기
url             : https://www.acmicpc.net/problem/30008
runtime         : 48 ms
memory          : 31120 KB
"""

n, k = map(int, input().split())
G = [*map(int, input().split())]
P = [4, 11, 23, 40, 60, 77, 89, 96, 100]

ret = []
for g in G:
    t = g*100//n
    for i, p in enumerate(P):
        if t<=p:
            ret.append(i+1)
            break
print(*ret)

"""
제 1회 선린 프로그래밍 챌린지 Open Contest

시키는 그대로 구현
"""