"""
Solving Date    : 2024.07.30
Solving Time    : 7m
Title           : 배찬우는 배열을 좋아해
tags            : 구현
url             : https://www.acmicpc.net/problem/25966
runtime         : 5616 ms
memory          : 386392 KB
"""

import sys
input = sys.stdin.readline

n, m, q = map(int, input().split())
ar = [[*map(int, input().split())] for _ in range(n)]

for _ in range(q):
    op, i, j, *k = map(int, input().split())

    if op:
        tmp = ar[i]
        ar[i] = ar[j]
        ar[j] = tmp
    else:
        ar[i][j] = k[0]
    
for i in range(n):
    print(*ar[i])

"""
ar를 입력받을 때, 각 요소를 int로 받을 필요는 없긴 함.

int로 안받을 경우
-> 680548 KB / 5200 ms

---

ar를 문자열 그대로 입력받고, 출력코드를 다음과 같이 바꿨을 경우
print(*map(lambda x:" ".join(map(str, x)), ar), sep="\n")
-> 723616 KB / 3708 ms
"""