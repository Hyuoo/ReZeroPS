"""
Solving Date    : 2023.09.22
Solving Time    : 8m
Title           : 공통 부분 문자열
tags            : 다이나믹 프로그래밍, 문자열
url             : https://www.acmicpc.net/problem/5582
runtime         : 7256 ms
memory          : 31256 KB
"""

a = input()
b = input()

cmp = [0 for _ in range(len(a)+1)]
m = 0

for ch in range():
    # reversed쓰면 손해
    # for i in reversed(range(len(a))): -> 7616 ms
    for i in range(len(a), 0, -1):
        cmp[i] = cmp[i-1]+1 if a[i-1] == ch else 0
        # 비교연산 한번씩 더하면 손해
        # if cmp[i]: -> 7748 ms
        m = max(m, cmp[i])

    # 아예 inline if-else 안하고 if로 max까지 넣으면 7260 ms
    # for i in range(len(a), 0, -1):
    #     if a[i - 1] == ch:
    #         cmp[i] = cmp[i - 1] + 1
    #         m = max(m, cmp[i])
    #     else:
    #         cmp[i] = 0

print(m)

"""
어제 LCS 공부함.
같은문자면 이전 매칭+1 끝.

ABRACADABRA
ECADADABRBCRDARA
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
[0, 1, 0, 0, 1, 0, 2, 0, 1, 0, 0, 1]
[0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0]
[0, 1, 0, 0, 1, 0, 1, 0, 4, 0, 0, 1]
[0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0]
[0, 1, 0, 0, 1, 0, 1, 0, 3, 0, 0, 1]
[0, 0, 2, 0, 0, 0, 0, 0, 0, 4, 0, 0]
[0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 5, 0]
[0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0]
[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0]
[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
[0, 1, 0, 0, 1, 0, 1, 0, 2, 0, 0, 1]
[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0]
[0, 1, 0, 0, 2, 0, 1, 0, 1, 0, 0, 2]
"""