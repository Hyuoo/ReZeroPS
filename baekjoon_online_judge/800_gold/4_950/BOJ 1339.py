"""
Solving Date    : 2023.09.17
Solving Time    : 11m
Title           : 단어 수학
tags            : 그리디 알고리즘
url             : https://www.acmicpc.net/problem/1339
runtime         : 40 ms
memory          : 31256 KB
"""

n = int(input())

weight = {}
for _ in range(n):
    for i, c in enumerate(input()[::-1]):
        weight[c] = weight.get(c, 0)+(10**i)

ans = 0
for i, v in enumerate(sorted(weight.values(), reverse=True)):
    ans += (9-i)*v
print(ans)

"""
각 알파벳 별 가중치를 주고,
가중치 큰 순서대로 9..8..7...

그리고 덧셈이기 때문에 앞뒤 알파벳 상관없이
자기 자릿수 위치만 중요하다.
"""