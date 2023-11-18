"""
Solving Date    : 2023.10.27
Solving Time    : 16m
Title           : 효구와 호규 (Easy)
tags            : 애드 혹, 비둘기집 원리
url             : https://www.acmicpc.net/problem/26085
runtime         : 224 ms
memory          : 39072 KB
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ar = []
c = 0

for _ in range(n):
    ar.append(tmp := input().split())
    c += tmp.count("1")

if n*m%2 or c%2:
    print(-1)
else:
    for i in range(n-1):
        for j in range(m-1):
            if ar[i][j] == ar[i+1][j] or ar[i][j] == ar[i][j+1]:
                print(1)
                exit(0)
    print(-1)

"""
음
비둘기집 원리 풀어보고 나서
비슷한 느낌의 다른 문제를 풀어보고싶었는데 얘는 아닌듯.
"""