"""
Solving Date    : 2023.11.27
Solving Time    : 5m
Title           : 포지션 제로
tags            : 수학, 구현, 기하학
url             : https://www.acmicpc.net/problem/30009
runtime         : 48 ms
memory          : 31120 KB
"""

n = int(input())
X, Y, R = map(int, input().split())
l, r = X-R, X+R
ret = [0, 0]

for _ in range(n):
    t = int(input())
    if t == l or t == r:
        ret[1] += 1
    elif t > l and t < r:
        ret[0] += 1

print(*ret)

"""
제 1회 선린 프로그래밍 챌린지 Open Contest

y좌표는 풀이와 상관이 없고,
x좌표 기준으로 반지름만큼 구해서 접선과 내부 계산.
"""