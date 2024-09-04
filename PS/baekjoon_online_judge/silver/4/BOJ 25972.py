"""
Solving Date    : 2024.08.08
Solving Time    : 3m
Title           : 도미노 무너트리기
tags            : 그리디 알고리즘, 정렬
url             : https://www.acmicpc.net/problem/25972
runtime         : 1760 ms
memory          : 133352 KB
"""

import sys
input = sys.stdin.readline

p = 0
c = 0
for d, l in sorted([*map(int, input().split())] for n in range(int(input()))):
    if p < d:
        c += 1
    p = d+l
print(c)

"""
이전 도미노가 닿지 않는 거리 일 경우에만 +1

특이점으로 무조건 1개씩만 넘어진다.
예를 들어
1 10000
2 1
10 1
이런 도미노가 있어도 x:2에서 x:10을 넘어뜨리지 못해서 횟수는 2번이다.
"""