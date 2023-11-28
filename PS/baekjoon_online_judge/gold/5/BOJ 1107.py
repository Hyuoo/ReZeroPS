"""
Solving Date    : 2023.11.26
Solving Time    : -
Title           : 리모컨
tags            : 브루트포스 알고리즘
url             : https://www.acmicpc.net/problem/1107
runtime         : 636 ms
memory          : 31120 KB
"""

def try_num(num):
    global ans, n
    if len(num)>5:
        return None

    for i in btn:
        tmp = num+i
        ans = min(ans, len(tmp) + abs(n - int(tmp)))
        try_num(tmp)

n = int(input())
btn = {str(i) for i in range(10)}
if int(input()):
    btn = btn - {*input().split()}

ans = abs(100-n)
try_num("")

print(ans)

"""
예전에 못 풀었던 문제.
이번에도 컨닝하고 풀었다.

최선을 찾아서 접근하려고 하지 말고,
모든 버튼을 누를 수 있는 경우를 구한 뒤
브루트포스로 +- 최소값을 찾는다. 
"""