"""
Solving Date    : 2023.10.20
Solving Time    : 18m
Title           : IOIOI
tags            : 문자열
url             : https://www.acmicpc.net/problem/5525
runtime         : 452 ms
memory          : 33076 Kb
"""

n = int(input())
_ = int(input())

tmp = 0
ans = 0
for io in input()+"E":
    if (io=="O") if tmp%2 else (io=="I"):
        tmp += 1
    else:
        ans += max(((tmp+1)//2)-n, 0)
        tmp %= 2

print(ans)

"""
규칙찾아서 의식의 흐름대로 구현.

IOIO..반복적으로 진행될 경우 카운팅해서
초기화 될 경우 포함된 개수만큼 증가.
"""