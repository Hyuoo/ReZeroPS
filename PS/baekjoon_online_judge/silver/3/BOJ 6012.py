"""
Solving Date    : 2024.08.05
Solving Time    : 8m
Title           : The Big Dance
tags            : 재귀
url             : https://www.acmicpc.net/problem/6012
runtime         : 32 ms
memory          : 31120 KB
"""

tot = 0

def div(s, e):
    global tot
    if s+1 == e:
        tot += s*e
    if s==e:
        return None
    m = (s+e)//2
    div(s, m)
    div(m+1, e)

div(1, int(input()))
print(tot)
