"""
Solving Date    : 2024.07.31
Solving Time    : 8m
Title           : Shirts
tags            : 구현, 문자열, 정렬
url             : https://www.acmicpc.net/problem/5078
runtime         : 40 ms
memory          : 31120 KB
"""
import sys
input = sys.stdin.readline

while 1:
    # SML + BKNOPRW
    size = {e:i for i, e in enumerate("SML")}
    color = {e:i for i, e in enumerate("BKNOPRW")}
    w = int(input())
    if w==0:
        break
    sh = [input().strip() for _ in range(w)]
    sh.extend([input().strip() for _ in range(int(input()))])
    sh.sort(key=lambda x:(size[x[0]], color[x[1]]))

    print(*sh)