"""
Solving Date    : 2024.03.08
Solving Time    : 6m
Title           : 칸토어 집합
tags            : 분할 정복, 재귀
url             : https://www.acmicpc.net/problem/4779
runtime         : 44 ms
memory          : 32156 KB
"""

import sys
input = sys.stdin.readline
ar = [a:="-"] + [a:=(a+" "*(3**(i-1))+a) for i in range(1, 13)]
for i in open(0):
    print(ar[int(i)])