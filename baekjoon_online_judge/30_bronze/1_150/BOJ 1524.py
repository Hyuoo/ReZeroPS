"""
Solving Date    : 2023.09.27
Solving Time    : 8m
Title           : 세준세비
tags            : 구현, 정렬, 시뮬레이션
url             : https://www.acmicpc.net/problem/1524
runtime         : 356 ms
memory          : 51400 KB
"""

f = lambda x: ar.extend([(n, x) for n in map(int, input().split())])

for tc in range(int(input())):
    _ = input()
    _, _= map(int, input().split())
    ar = []
    f(1);f(0)
    print("BS"[sorted(ar)[-1][1]])

"""
정렬 후 마지막 인덱스
"""