"""
Solving Date    : 2024.06.04
Solving Time    : 23m
Title           : 연산자 끼워넣기
tags            : 브루트포스, 알고리즘 백트래킹
url             : https://www.acmicpc.net/problem/14888
runtime         : 68 ms
memory          : 31252 KB
"""

import sys
input = sys.stdin.readline

func = [lambda a,b:a+b, lambda a,b:a-b, lambda a,b:a*b, lambda a,b:int(a/b)]

n = int(input())
ar = [*map(int, input().split())]
ops = [*map(int, input().split())]
results = []

def b_solve(tot, i):
    if i == n:
        results.append(tot)
        return None
    
    for op in range(4):
        if ops[op]:
            ops[op] -= 1
            b_solve(func[op](tot, ar[i]), i+1)
            ops[op] += 1
    return None

b_solve(ar[0], 1)
print(max(results), min(results), sep="\n")


"""
음수/양수 일 때, -(-a//b) 했다가 다른 풀이 보고 int(a/b)면 되길래 바꿈.
"""