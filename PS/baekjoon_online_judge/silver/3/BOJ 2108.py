"""
Solving Date    : 2024.07.26
Solving Time    : -
Title           : 통계학
tags            : 수학, 구현, 정렬
url             : https://www.acmicpc.net/problem/2108
runtime         : 392 ms
memory          : 55908 KB
"""

from collections import Counter

n, *r = [*map(int, open(0))]
r.sort()

a,*b = Counter(r).most_common(2)
f = b[0][0] if b and a[1] == b[0][1] else a[0]

print(
    round(sum(r)/n),
    r[n//2],
    f,
    r[-1]-r[0],
    sep="\n"
    )