"""
Solving Date    : 2023.09.27
Solving Time    : 2h 17m
Title           : 합이 0인 네 정수
tags            : 정렬, 이분 탐색, 투 포인터, 중간에서 만나기
url             : https://www.acmicpc.net/problem/7453
runtime         : 6868 ms
memory          : 664640 KB
"""

import sys
input = sys.stdin.readline

n = int(input())
arr = [[*map(int,input().split())] for _ in range(n)]

a = []
b = []
for i in range(n):
    for j in range(n):
        a.append(arr[i][0]+arr[j][1])
        b.append(arr[i][2]+arr[j][3])

a.sort()
b.sort()

n = n**2
i, j = 0, n-1
c = 0

while i < n and j >= 0:
    if a[i]+b[j]:
        # not 0
        if a[i]+b[j] < 0:
            i += 1
        else:  # a[i]+b[j] > 0
            j -= 1
    else:
        # 0
        anc_i = i
        anc_j = j
        while i < n and a[anc_i] == a[i]:
            i += 1
        while j >= 0 and b[anc_j] == b[j]:
            j -= 1
        c += (i-anc_i) * (anc_j-j)

print(c)

"""
시간제한 문제는 어려워
마지막 결과도 Python3 -> pypy로 제출해서 맞았다.

1. 마지막거만 이분탐색, 이후에는 바운드 정해서 탐색범위 줄여가면서 반복
아무리 잘쳐줘도 n^n 정도 되는 듯 하다.

처음에 배열 2개 2개 합칠 생각 하긴 했는데,
그냥 조삼모사 느낌이어서 안했는데, 이게 답이었다.
- 반복자체는 똑같이 되긴 하는데,
    2개 초과하는 배열을 또 반복하려면 기하급수로 올라가서
    줄이는게 이득.

2개씩 배열 합쳐서, 뒤에꺼만 정렬해서
다시 이분탐색으로 접근했는데 내 머리론 잘 줄여봐도
안되어서 결국 컨닝

두개 다 정렬해서 투포인터로 접근.
중복이 필연시 발생할 수 있기 때문에 중복개수 세어서 곱하기.
"""