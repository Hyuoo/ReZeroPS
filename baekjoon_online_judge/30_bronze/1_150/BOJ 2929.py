"""
Solving Date    : 2023.10.04
Solving Time    : 20m
Title           : 머신 코드
tags            : 구현, 문자열, 파싱, 정규 표현식
url             : https://www.acmicpc.net/problem/2929
runtime         : 40 ms
memory          : 31256 KB
"""

tmp = 0
ans = 0
for c in input():
    if c>="A" and c<="Z":
        ans += tmp
        tmp = 4
    elif not tmp:
        tmp = 4
    tmp -= 1

print(ans)

"""
len(opcode+operand) <= 4
라고 생각해서 왜안되지 하고 한참 풀이
"""