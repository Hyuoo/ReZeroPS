"""
Solving Date    : 2024.01.13
Solving Time    : 3m
Title           : 화성 수학
tags            : 수학, 구현, 사칙연산
url             : https://www.acmicpc.net/problem/5355
runtime         : 40 ms
memory          : 31120 KB
"""

d={"@":"*3", "%":"+5", "#":"-7"}
for s in [*open(0)][1:]:
    a, *b = s.split()
    while b:
        a = eval(str(a)+d[b[0]])
        b = b[1:]
    print(f"{a:.2f}")
