"""
Solving Date    : 2023.09.27
Solving Time    : 16m
Title           : 버블 소트
tags            : 정렬
url             : https://www.acmicpc.net/problem/1377
runtime         : 1044 ms
memory          : 105652 KB
"""

import sys
input = sys.stdin.readline

n = int(input())
ar = [(int(input()), i) for i in range(n)]
sorted_ar = sorted(ar)

m = 0
for i in range(n):
    m = max(m, sorted_ar[i][1]-i)

print(m+1)

"""
이게 왜 골2?

그냥 버블정렬 특성을 이해하고 있으면, 풀 수 있는 문제.

문제 코드는 오른쪽으로 미는데,
그렇기 때문에 왼쪽으로는 한 사이클 당 최대 한칸만 이동한다.

그래서 기존 위치랑, 정렬 후 위치를 비교해서
왼쪽으로 이동 한 거리 중 가장 긴 거리를 구하면 끝.


``` short
import sys
input = sys.stdin.readline
a = sorted((int(input()), i) for i in range(int(input())))
print(max([a[i][1]-i for i in range(len(a))])+1)
``` >> 952 ms, 120908 KB
"""