"""
Solving Date    : 2023.11.14
Title           : donstructive
tags            : 해 구성하기
url             : https://www.acmicpc.net/problem/30618
rank            : 1
byte            : 55 B
"""

n=int(input())
print(*range(1,n+1,2),*range(n&~1,0,-2))

