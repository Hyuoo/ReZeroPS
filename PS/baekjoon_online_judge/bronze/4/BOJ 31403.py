"""
Solving Date    : 2024.07.26
Solving Time    : 1m
Title           : A + B - C
tags            : 수학, 문자열, 사칙연산
url             : https://www.acmicpc.net/problem/31403
runtime         : 40 ms
memory          : 31120 KB
"""

a, b, c = map(str.strip, open(0))
print(*map(eval, (f"{a}+{b}-{c}", f"{a}{b}-{c}")), sep="\n")


"""
str.strip 할 필요 없이 int를 하면 공백문자가 무시된다.
"""