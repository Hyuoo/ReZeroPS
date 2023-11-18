"""
Solving Date    : 2023.11.12
Solving Time    : 3m
Title           : donstructive
tags            : 해 구성하기
url             : https://www.acmicpc.net/problem/30618
runtime         : 160 ms
memory          : 41344 KB
"""

from collections import deque
n = int(input())
q = deque()
r = 0
for i in range(n, 0, -1):
    if r:
        q.append(i)
    else:
        q.appendleft(i)
    r ^= 1
print(*q)

"""
2023 Sogang Programming Contest Open (Master) · Arena #12
B번 문제

무조건 큰거 가운데, 양쪽 번갈아가면서 낮아지면 되는 문제.
그래서 deque로 번갈아가면서 붙였다.

대회 이후 다른 풀이를 보니
단순히 range(1, n+1, 2) + range(n-n%2, 0, -2)
이렇게 해도 된다.
"""