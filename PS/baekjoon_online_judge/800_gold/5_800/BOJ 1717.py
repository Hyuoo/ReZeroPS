"""
Solving Date    : 2023.09.17
Solving Time    : 18m
Title           : 집합의 표현
tags            : 자료 구조, 분리 집합
url             : https://www.acmicpc.net/problem/1717
runtime         : 308 ms
memory          : 71248 KB
"""

import sys
input = sys.stdin.readline

def find(n):
    # 왜 이거랑 시간차이가 많이나지? 456 ms
    # if papa[n] != n: 붙여줘도 448 ms
    # me = n
    # while papa[me] != me:
    #     me = papa[me]
    # papa[n] = me
    # return me
    if papa[n] == n:
        return n
    papa[n] = find(papa[n])
    return papa[n]

def union(a, b):
    ap = find(a)
    bp = find(b)
    papa[bp] = ap

n, m = map(int, input().split())

papa = [i for i in range(n+1)]

for _ in range(m):
    op, a, b, = map(int, input().split())
    if op == 0:
        # 합집합
        union(a, b)
    else:
        # 같은 집합 체크
        print("NO" if find(a)-find(b) else "YES")

"""
두개 집합 합치고, 두개 같은건지 확인
바로 union find 알고리즘이 생각났다

정해 인듯 
"""