"""
Solving Date    : 2024.03.25
Solving Time    : 10m
Title           : 포도주 시음
tags            : 그리디 알고리즘, 정렬, 두 포인터
url             : https://www.acmicpc.net/problem/31589
runtime         : 260 ms
memory          : 66124 KB
"""

n, k = map(int, input().split())
ar = sorted(map(int, input().split()))

i = -1
ret = 0
prev = 0
flag = 1
for _ in range(k):
    if flag:
        ret += ar.pop()-prev
    else:
        prev = ar[i:=i+1]
    flag ^= 1

print(ret)

"""
큰거 작은거 지그 재그

- 예제가 어케 20이 나오나 문제 이해하는데 5분걸림
"""