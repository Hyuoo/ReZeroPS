"""
Solving Date    : 2023.11.18
Solving Time    : 14m
Title           : 전깃줄
tags            : 다이나믹 프로그래밍
url             : https://www.acmicpc.net/problem/2565
runtime         : 40 ms
memory          : 31120 KB
"""

import sys
input = sys.stdin.readline

n = int(input())
ar = []

for _ in range(n):
    a, b = map(int, input().split())
    ar.append([a, b])

seq = []
for i in sorted(ar):
    seq.append(i[1])

dp = [1 for _ in range(n)]
t = 0
for i in range(n):
    for j in range(i, n):
        if seq[i] < seq[j]:
            dp[j] = max(dp[j], dp[i]+1)
    t = max(t, dp[i])

print(n-t)

"""
최장증가부분수열 (LIS) 문제

겹치지 않는다는 문제가,
- A전봇대 순으로 정렬 한 뒤
  B전봇대를 같은 순으로 증가하는 수열이면 선이 겹치지 않는다.

이걸 이용해서
1. A전봇대 기준으로 오름차순 정렬
2. B전봇대 순서로 LIS 실행
3. 2의 결과 중 가장 긴 길이

전체 길이에서 가능한 가장 긴 길이를 빼면
없애야하는 전깃줄의 최소 개수가 된다. 
"""