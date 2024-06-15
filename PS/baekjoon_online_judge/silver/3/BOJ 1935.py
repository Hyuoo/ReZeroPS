"""
Solving Date    : 2024.06.12
Solving Time    : 12m
Title           : 후위 표기식2
tags            : 자료 구조, 스택
url             : https://www.acmicpc.net/problem/1935
runtime         : 40 ms
memory          : 31120 KB
"""

import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
postfix_exp = input()
nums = [input() for _ in range(n)]

s = []
for op in postfix_exp:
    if op in "+-*/":
        b = s.pop()
        a = s.pop()
        s.append(str(eval(a+op+b)))
    else:
        s.append(nums[ord(op)-65])
    
print(f"{float(s[0]):.2f}")

"""
eval꼼수.
"""