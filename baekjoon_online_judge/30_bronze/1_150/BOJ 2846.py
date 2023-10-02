"""
Solving Date    : 2023.10.02
Solving Time    : 13m
Title           : 오르막길
tags            : 구현
url             : https://www.acmicpc.net/problem/2846
runtime         : 44 ms
memory          : 31256 KB
"""

n = int(input())
ar = list(map(int, input().split()))
m = 0
tmp = 0

for i in range(1, n):
    if ar[i] > ar[i-1]:
        if not tmp:
            tmp = ar[i-1]
        m = max(m, ar[i] - tmp)
    else:
        tmp = 0

print(m)

"""
아니 왜 같은높이 오르막길로 안쳐줌 ㅡㅡ
당연히 1223 이런거 오르막길인줄아랏네 
"""