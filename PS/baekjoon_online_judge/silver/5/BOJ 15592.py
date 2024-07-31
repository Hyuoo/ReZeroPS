"""
Solving Date    : 2024.07.26
Solving Time    : 14m
Title           : Blocked Billboard II
tags            : 구현, 기하학, 많은 조건 분기
url             : https://www.acmicpc.net/problem/15592
runtime         : 40 ms
memory          : 31120 KB
"""

a,s,d,f = map(int, input().split())
z,x,c,v = map(int, input().split())

cov = 2*(z<=a and c>=d) + 1*(x<=s and v>=f)

if cov == 1:
    if d<=c: d = min(d, z)
    if a>=z: a = max(a, c)
if cov == 2:
    if f<=v: f = min(f, x)
    if s>=x: s = max(s, v)
if cov == 3:
    a = s = d = f = 0

print((d-a)*(f-s))


"""
수평, 수직 커버 여부를 2 비트 cov변수로 나타내고
부분이 완전히 가려지는 케이스를 나눠서 계산값을 제한함
"""