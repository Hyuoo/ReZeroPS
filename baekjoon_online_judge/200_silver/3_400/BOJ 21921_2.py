"""
Solving Date    : 2023.09.20
Solving Time    : -
Title           : 블로그
tags            : 누적 합, 슬라이딩 윈도우
url             : https://www.acmicpc.net/problem/21921
runtime         : 156 ms
memory          : 60696 KB
"""

n, x = map(int, input().split())
ar = [*map(int, input().split())]

tot = sum(ar[:x])
peak = tot
peak_count = 1

for i in range(x, n):
    tot += ar[i] - ar[i-x]
    if peak < tot:
        peak = tot
        peak_count = 1
    elif peak == tot:
        peak_count += 1

print(f"{peak}\n{peak_count}" if peak else "SAD")

"""
누적 합과 슬라이딩 윈도우 두가지 풀이 방식 중
슬라이딩 윈도우 풀이

구간을 정하는 간격이 일정하기 때문에
슬라이딩 윈도우 방식이 가능하다.
"""