"""
Solving Date    : 2023.09.23
Solving Time    : 11m
Title           : LCS 2
tags            : 다이나믹 프로그래밍
url             : https://www.acmicpc.net/problem/9252
runtime         : 596 ms
memory          : 56564 KB
"""

a = input()
b = input()

ar = [[0 for _ in range(len(a)+1)] for _ in range(len(b)+1)]

for i in range(len(b)):
    for j in range(len(a)):
        ar[i + 1][j + 1] = (ar[i][j]+1 if b[i] == a[j] else max(ar[i+1][j], ar[i][j+1]))

ret = ""
x, y = len(b), len(a)
while ar[x][y]!=0:
    # print(f"[{x},{y}]", end="\t")
    if ar[x][y] == ar[x-1][y]:
        x-=1
    elif ar[x][y] == ar[x][y-1]:
        y-=1
    else:
        ret += b[x-1]
        x-=1
        y-=1

print(ar[-1][-1])
print(ret[::-1])

"""
그저께 배운 LCS알고리즘 마지막

5582 -> 9251 -> 9252
순으로 LCS풀어보면 된다.

진짜 그냥 배운 개념 그대로 구현..?
구현이라기도 뭐할만큼 이해한대로 적기만 하면 되는 문제

역추적을 해야하기 때문에 배열을 모두 살려놓는다.
"""