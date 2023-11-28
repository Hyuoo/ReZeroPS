"""
Solving Date    : 2023.11.18
Solving Time    : 2m
Title           : 반도체 설계
tags            : 이분 탐색, 가장 긴 증가하는 부분 수열: o(n log n)
url             : https://www.acmicpc.net/problem/2352
runtime         : 64 ms
memory          : 38240 KB
"""

import bisect
input()
ar = [*map(int, input().split())]

lis = [ar[0]]
for i in ar[1:]:
    if lis[-1] < i:
        lis.append(i)
    else:
        d = bisect.bisect_left(lis, i)
        lis[d] = i

print(len(lis))

"""
LIS알고리즘 공부 후 풀이.
"""