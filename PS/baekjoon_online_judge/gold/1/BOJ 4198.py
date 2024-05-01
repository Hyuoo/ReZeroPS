"""
Solving Date    : 2024.05.01
Solving Time    : 43m
Title           : 열차정렬
tags            : 다이나믹 프로그래밍, 가장 긴 증가하는 부분 수열: o(n log n)
url             : https://www.acmicpc.net/problem/4198
runtime         : 620 ms
memory          : 33184 KB
"""

import bisect

def foo(start):
    ldp = [ar[start]]
    rdp = [-ar[start]]
    crit = ar[start]

    for e in ar[start+1:]:
        if ldp[-1] < e:
            ldp.append(e)
        elif crit < e:
            idx = bisect.bisect_left(ldp, e)
            ldp[idx] = e

        if rdp[-1] < -e:
            rdp.append(-e)
        elif crit > e:
            idx = bisect.bisect_right(rdp, -e)
            rdp[idx] = -e

    return (len(ldp) + len(rdp) - 1)

n = int(input())
if n == 0:
    print(0)
    exit(0)
ar = [int(input()) for _ in range(n)]
print(max([foo(i) for i in range(n)]))


"""
위로 최장수열, 아래로 최장수열 해서 합치기.

왜 시작 인덱스를 다 비교해야 하는지 이유를 몰라서 한참 걸렸다.


풀이 방법에서
뒷부분은 최장수열을 구하면서 자연스럽게 버리기가 되지만,
앞부분은 무조건 선택이 된다.
다만, 이 앞부분을 버리는게 더 길이가 긴 경우가 있다.
- [10, 1, 2, 3]
    - 10부터 하게되면 위로 길이 1, 아래로 길이 2
    - 1부터 하게되면 위로 길이 3, 아래로 길이 1


그리고 100%에서 틀린다면 입력길이가 0인 경우이다.
max()로 전체경우를 커버하게 해놔서 "틀렸습니다"대신, valueerror가 떠서 쉽게 수정했다.
"""