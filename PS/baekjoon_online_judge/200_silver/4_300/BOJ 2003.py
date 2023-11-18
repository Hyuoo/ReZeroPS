"""
Solving Date    : 2023.10.29
Solving Time    : 11m
Title           : 수들의 합 2
tags            : 브루트포스 알고리즘, 누적 합, 두 포인터
url             : https://www.acmicpc.net/problem/2003
runtime         : 44 ms
memory          : 32140 KB
"""

n, m = map(int, input().split())
ar = [*map(int, input().split())]

i, j = 0, 0
tot = 0
ans = 0
while j<n:
    while j<n and tot<m:
        tot += ar[j]
        j += 1
    while tot>=m:
        if tot == m:
            ans += 1
        tot -= ar[i]
        i += 1
print(ans)

"""
누적합이래서 골랐는데, 속았다.

누적합으로도 시간 내에 풀 수 있겠지만,
누적합을 해도 똑같은 방식으로 진행해야 해서,
굳이 누적합으로 풀 필요가 없는 문제라고 판단했다.

포인터 두개로 m과 값을 비교해가며
범위를 조절하며 진행해서 풀이. 
"""