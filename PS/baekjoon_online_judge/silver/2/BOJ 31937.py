"""
Solving Date    : 2024.07.12
Solving Time    : 24m
Title           : 로그프레소 마에스트로
tags            : 구현, 브루트포스 알고리즘, 정렬, 시뮬레이션
url             : https://www.acmicpc.net/problem/31937
runtime         : 696 ms
memory          : 33164 KB
"""

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
badcom = [*map(int, input().split())]

log = []
for _ in range(m):
    log.append([*map(int, input().split())])
log.sort()

final_situ = set(badcom)

for real_badcom in badcom:
    s = set([real_badcom])
    
    for _, a, b in log:
        if a in s:
            if b not in final_situ:
                break
            s.add(b)
    else:
        if s == final_situ:
            print(real_badcom)
            exit(0)
