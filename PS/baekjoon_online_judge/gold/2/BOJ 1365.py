"""
Solving Date    : 2024.01.08
Solving Time    : 5m
Title           : 꼬인 전깃줄
tags            : 이분 탐색, 가장 긴 증가하는 부분 수열: o(n log n)
url             : https://www.acmicpc.net/problem/1365
runtime         : 92 ms
memory          : 44104 KB
"""

import bisect

n = int(input())
ar = [*map(int, input().split())]

q = [ar[0]]
for i in ar[1:]:
    if q[-1] < i:
        q.append(i)
    else:
        idx = bisect.bisect(q, i)
        q[idx] = i

print(n-len(q))

"""
lis공부하니 골2문제가 거저먹기..
"""