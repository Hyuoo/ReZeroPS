"""
Solving Date    : 2024.08.02
Solving Time    : 26m
Title           : Swapity Swap
tags            : 수학, 그래프 이론
url             : https://www.acmicpc.net/problem/18788
runtime         : 144 ms
memory          : 31120	 KB
"""

n, k = map(int, input().split())
a = [*map(int, input().split())]
b = [*map(int, input().split())]

cows = [i for i in range(n+1)]
step = lambda low, high: cows[:low] + cows[high:low-1:-1] + cows[high+1:]
c = 0

while k:
    cows = step(*a)
    cows = step(*b)
    c += 1
    k -= 1
    for i in range(n):
        if cows[i] != i:
            break
    else:
        k %= c

print(*cows[1:], sep="\n")


"""
일단 입력범위 안보고 단순무식구현으로 시간초과+1

이후
정해진 범위만 반복해서 뒤집으면 제자리로 돌아오는 사이클이 생기지 않나
생각해서, 겹치는 범위에 따른 규칙성을 찾으려 했으나
머리가 안좋아 규칙파악은 안되고,
- N이 그렇게 크지 않음
- 몇개 케이스를 수작업으로 해보니 생각보다 사이클이 짧음
그래서 매 반복마다 원래대로 돌아왔는지(사이클이 이루어졌는지) 검사를 해서

사이클이 생길 경우, 나머지만큼 더 반복해줬다.
"""