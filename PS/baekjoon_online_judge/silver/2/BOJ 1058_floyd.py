"""
Solving Date    : 2024.09.09
Solving Time    : -
Title           : 친구
tags            : 그래프 이론, 브루트포스 알고리즘, 그래프 탐색, 최단 경로, 플로이드–워셜
url             : https://www.acmicpc.net/problem/1058
runtime         : 64 ms
memory          : 31120 KB
"""

import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
ar = [[*map(lambda x:[9,1][x=="Y"], input())] for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if ar[i][j] > (tmp:=ar[i][k]+ar[k][j]):
                ar[i][j] = tmp

ans = 0
for i in range(n):
    ar[i][i] = 9
    cnt = 0
    for l in ar[i]:
        if l < 3:
            cnt += 1
    
    ans = max(ans, cnt)

print(ans)

"""
플로이드워셜 버전 풀이
"""