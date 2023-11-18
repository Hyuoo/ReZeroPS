"""
Solving Date    : 2023.10.17
Solving Time    : 26m
Title           : 계단 오르기
tags            : 다이나믹 프로그래밍
url             : https://www.acmicpc.net/problem/2579
runtime         : 40 ms
memory          : 31120 KB
"""

import sys
input = sys.stdin.readline

n = int(input())
st = [int(input()) for _ in range(n)]

score = [[0, 0] for _ in range(n+1)]
score[n-1][1] = st[n-1]

for i in range(n-1, 0, -1):
    if score[i][0] and i-2>=0:
        score[i-2][1] = max(score[i-2][1], st[i-2]+score[i][0])
    if score[i][1]:
        if i-1>=0:
            score[i-1][0] = max(score[i-1][0], st[i-1]+score[i][1])
        if i-2>=0:
            score[i-2][1] = max(score[i-2][1], st[i-2]+score[i][1])

print(max(*score[0], *score[1]))

"""
무조건 마지막계단은 밟으래서
마지막 계단부터 시작했다.

연속해서 밟은 경우와 건너서 밟은 경우 두개로 나눠서
위에서부터 최대값 갱신하는 방식으로 풀었다.

정석?은 dp풀이로 아래서부터 max( (-2)+(0), (-3)+(-1)+(0) )
"""