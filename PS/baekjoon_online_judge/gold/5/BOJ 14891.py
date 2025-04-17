"""
Solving Date    : 2025.01.02
Solving Time    : 55m
Title           : 톱니바퀴
tags            : 구현, 시뮬레이션
url             : https://www.acmicpc.net/problem/14891
runtime         : 40 ms
memory          : 32412 KB
"""

import sys
input = sys.stdin.readline

RIGHT = 32
LEFT = 2

rot_cw = lambda x: (x>>1) | (x&1 and 128)
rot_ccw = lambda x: (x<<1)&255 | (x&128 and 1)
rot = [rot_cw, rot_ccw]

def spin(no, lr, sn, cw):
    if not(0 <= no < 4) or visit[no]:
        return
    if bool(w[no]&lr)^bool(sn):
        visit[no] = 1
        spin(no-1, RIGHT, w[no]&LEFT, cw^1)
        spin(no+1, LEFT, w[no]&RIGHT, cw^1)
        w[no] = rot[cw](w[no])

w = [int(input(), 2) for _ in range(4)]

for q in range(int(input())):
    no, r = map(lambda x:(int(x)-1), input().split())
    visit = [0,0,0,0]
    spin(no, LEFT, not(w[no]&LEFT), r//-2)

ans = 0
for i in range(4):
    ans = (ans<<1) + bool(w[3-i]&128)

print(ans)