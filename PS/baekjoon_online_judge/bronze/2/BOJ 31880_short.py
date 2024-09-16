"""
Solving Date    : 2024.09.04
Title           : K512컵 개최!
tags            : 수학, 그리디 알고리즘, 사칙연산
url             : https://www.acmicpc.net/problem/31880
rank            : 4
byte            : 85 B
"""

i=lambda:map(int,input().split())
_,a=i(),sum(i())
[a:=a*d for d in i()if d]
print(a)