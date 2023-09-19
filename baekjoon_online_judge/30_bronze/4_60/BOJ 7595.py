"""
Solving Date    : 2023.09.18
Solving Time    : -
Title           : Triangles
tags            : 구현
url             : https://www.acmicpc.net/problem/7595
runtime         : 44 ms
memory          : 32276 KB
"""

import sys
input = sys.stdin.readline
ans = []
while 1:
    n = int(input())
    if n==0:
        break
    ans.extend("*"*i for i in range(1, n+1))
print(*ans, sep="\n")

"""
while 1:
    n = int(input())
    if n==0:
        break
    for i in range(n):
        print("*"*(i+1))
이 코드(60ms)로부터

>> ans += "*"*(i+1)+"\n"    (424ms)

>> ans += f"{'*'*(i+1)}\n"  (436ms)

>> ans.extend("*"*(i+1) for i in range(n))
    print("\n".join(ans))   (56ms)

>> ans.extend("*"*(i+1) for i in range(n))
    print(*ans, sep="\n")   (52ms)
    >> add readline -> 48ms

>> ans.extend("*"*i for i in range(1, n+1))
    print(*ans, sep="\n")   (52ms)
    >> add readline -> 본문 코드 (44ms)
"""