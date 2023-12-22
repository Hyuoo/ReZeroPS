"""
Solving Date    : 2023.12.22
Solving Time    : 6m
Title           : Rating Increase
tags            : implementation
url             : https://codeforces.com/problemset/problem/1913/A
runtime         : 124 ms
memory          : 100 KB
"""

for tc in range(int(input())):
    ab = input()
    for i in range(1, len(ab)//2+1):
        a, b = ab[:i], ab[i:]
        if b[0] != "0" and int(a)<int(b):
            print(a, b)
            break
    else:
        print(-1)