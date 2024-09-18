"""
Solving Date    : 2024.09.18
Solving Time    : -
Title           : 터널
tags            : 구현, 그리디 알고리즘
url             : https://www.acmicpc.net/problem/3155
runtime         : 188 ms
memory          : 46060 KB
"""

n = int(input())
top = [1]+[*map(int, input().split())]+[1]
bot = [-1]+[*map(int, input().split())]+[-1]

top = [min(top[i:i+3])-1 for i in range(n)]
bot = [max(bot[i:i+3])+1 for i in range(n)]

appr = lambda a, b, x: sorted([a,b,x])[1]

o = 0
print(*[o:=appr(top[i], bot[i], o) for i in range(n)])


"""
기준점에서 가까운 위치를 찾는 부분을 틀려서 틀린문제.

[기준, 최소, 최대]가 있을 때 정렬해서 2번째를 뽑으면 되는걸 알게되어
해당부분 수정하니 정답.
"""