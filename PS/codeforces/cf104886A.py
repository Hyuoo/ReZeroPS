"""
Solving Date    : 2023.12.22
Solving Time    : 2m
Title           : Schedule Problem
tags            :
url             : https://codeforces.com/gym/104886/problem/A
runtime         : 46 ms
memory          : 0 KB
"""

for tc in range(int(input())):
    low, high = 1, 1000
    for n in range(int(input())):
        a, b = map(int, input().split())
        low = max(low, a)
        high = min(high, b)
    print("YES" if low<=high else "NO")