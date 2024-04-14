"""
Solving Date    : 2024.04.14
Solving Time    : 1h 30m
Title           : 명랑한 아리의 외출
tags            : 다이나믹 프로그래밍
url             : https://www.acmicpc.net/problem/25170
runtime         : 2324 ms
memory          : 76992 KB
"""

import sys
input = sys.stdin.readline

n, m, t = map(int, input().split())

work_count = [[0]*(m+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
work_time = [[0]*(m+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]

dp = [[[-1 for _ in range(t+1)] for _ in range(m+1)] for _ in range(n+1)]
gdp = lambda x,y,t,z:(-1 if t<0 or dp[x][y][t]==-1 else dp[x][y][t]+z)
dp[1][1][0] = 0

for i in range(1, n+1):
    for j in range(1, m+1):
        for k in range(1, t+1):
            pk = k - work_time[i][j] - 1
            w = work_count[i][j]
            dp[i][j][k] = max(
                gdp(i-1, j, k-1, 0),
                gdp(i, j-1, k-1, 0),
                gdp(i-1, j-1, k-1, 0),
                gdp(i-1, j, pk, w),
                gdp(i, j-1, pk, w),
                gdp(i-1, j-1, pk, w)
            )

print(max(dp[-1][-1]))

"""
머리가 안돌아간다
일단 변수가 많은, 공간이 많은 구조는 원래도 헷갈리긴 하는데
암튼 머리가 굳었나 싶다.

-- 기록 패스

대충. 시간 도메인을 어떻게 할 지 생각하다가
칸수가 50*50이고 시간도 500이라 싹다 돌려도 되는문제겠다 싶어서 저렇게 품.
"""