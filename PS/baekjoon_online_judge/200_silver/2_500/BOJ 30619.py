"""
Solving Date    : 2023.11.14
Solving Time    : 11m
Title           : 내 집 마련하기
tags            : 구현, 정렬
url             : https://www.acmicpc.net/problem/30619
runtime         : 72 ms
memory          : 31120 KB
"""

import sys
input = sys.stdin.readline

n = int(input())
a = [*map(int, input().split())]
p = [0 for _ in range(n+1)]

for i in range(n):
    p[a[i]] = i

for _ in range(int(input())):
    l, r = map(int, input().split())
    r+=1
    tmp = a[:]
    for idx, pep in zip(sorted(p[l:r]), range(l, r)):
        tmp[idx] = pep
    print(*tmp)

"""
2023 Sogang Programming Contest Open (Master) · Arena #12
C번 문제

주어진 범위에 대해서
인덱스가 아니라, 값에 대해서 재정렬을 하는 문제

1. 그래서 몇번 값이 어디에 들어가있는지 인덱스를 만들고
2. 재정렬하는 값 범위를 [값:인덱스] 리스트로 재정렬.
    - 재정렬 기준은 무조건 큰 수가 큰 인덱스로 가면 된다.

===
다른 풀이:
그냥 리스트 전체를 읽어나가면서
값 범위에 있는 값이면
해당 값 min부터 시작해서 대체해서 읽으면 된다.

이 방법이 훨씬 이해하기 쉽고, 리소스도 덜 쓴다.
"""