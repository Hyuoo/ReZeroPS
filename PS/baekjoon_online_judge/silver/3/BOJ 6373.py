"""
Solving Date    : 2024.09.05
Solving Time    : 8m
Title           : Round and Round We Go
tags            : 수학, 구현, 문자열, 사칙연산, 시뮬레이션, 임의 정밀도 / 큰 수 연산
url             : https://www.acmicpc.net/problem/6373
runtime         : 32 ms
memory          : 31120 KB
"""

for cand in open(0):
    cand = cand.rstrip()
    l = len(cand)
    tot = add = int(cand)
    cand_rep = cand*2
    flag = True

    for _ in range(l-1):
        tot += add
        tmp = f"{tot:0{l}}"
        if cand_rep.find(tmp) == -1:
            flag = False
            break
    
    print(f"{cand} is {['not ', ''][flag]}cyclic")