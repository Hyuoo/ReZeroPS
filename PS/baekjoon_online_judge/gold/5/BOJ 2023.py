"""
Solving Date    : 2024.10.04
Solving Time    : -
Title           : 신기한 소수
tags            : https://www.acmicpc.net/problem/2023
url             : 수학, 정수론, 백트래킹, 소수 판정
runtime         : 32 ms
memory          : 31120 KB
"""

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def foo(n, lt):
    if n > 10**lt:
        if is_prime(n):
            corr.append(n)
        return
    if is_prime(n):
        for i in range(10):
            foo(n*10 + i, lt)
    else:
        return

n = int(input())-1

corr = []
for i in range(1, 10):
    foo(i, n)

print(*corr, sep="\n")