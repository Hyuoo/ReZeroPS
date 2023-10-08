"""
Solving Date    : 2023.10.08
Solving Time    : -
Title           : 뉴스 전하기
tags            : 다이나믹 프로그래밍, 그리디 알고리즘, 정렬, 트리, 트리에서의 다이나믹 프로그래밍
url             : https://www.acmicpc.net/problem/1135
runtime         : 40 ms
memory          : 31256 KB
"""

f=lambda x:max([i+1-n for i,n in enumerate(sorted([-f(nxt)for nxt in t[x]]))])if t[x]else 0
n=int(input())
b=list(map(int,input().split()))
t=[[]for _ in range(n)]
for i in range(1,n):t[b[i]].append(i)
print(f(0))