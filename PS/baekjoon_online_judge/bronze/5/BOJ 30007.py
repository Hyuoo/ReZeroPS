"""
Solving Date    : 2023.11.27
Solving Time    : 2m
Title           : 라면 공식
tags            : 수학, 구현, 사칙연산
url             : https://www.acmicpc.net/problem/30007
runtime         : 40 ms
memory          : 31120 KB
"""

_,*q = open(0)
for i in q:
    a, b, x = map(int, i.split())
    print(a*(x-1)+b)

"""
제 1회 선린 프로그래밍 챌린지 Open Contest

시키는 그대로 구현
"""