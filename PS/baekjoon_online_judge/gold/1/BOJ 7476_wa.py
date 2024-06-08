"""
Solving Date    : 2024.01.08
Solving Time    : -
Title           : 최대 공통 증가 수열
tags            :
url             : https://www.acmicpc.net/problem/7476
runtime         :  ms
memory          :  KB
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
import bisect

n = int(input())
ar = [*map(int, input().split())]
m = int(input())
br = [*map(int, input().split())]

lcs = [[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(n):
    for j in range(m):
        if ar[i] == br[j]:
            lcs[i+1][j+1] = lcs[i][j] + 1
        else:
            lcs[i+1][j+1] = max(lcs[i+1][j], lcs[i][j+1])

# print(end="   ")
# for i in [0]+br:
#     print(f"{i:>3}", end="")
# print()
# for i in range(n+1):
#     print(f"{([0]+ar)[i]:3} {lcs[i]}")

check = set()
def track(i, j, ret):
    if i==0 or j==0 or (i, j) in check:
        # print(ret)
        return ret
    check.add((i, j))
    if ar[i-1] == br[j-1]:
        if not ret:
            ret = [-ar[i-1]]
        elif ret[-1] < -ar[i-1]:
            ret.append(-ar[i-1])
        else:
            idx = bisect.bisect_left(ret, -ar[i-1])
            ret[idx] = -ar[i-1]
        ret = track(i-1, j-1, ret[:])
        # print(ret, i, j)
        return ret
    else:
        if lcs[i][j] == lcs[i-1][j]:
            tmp = track(i-1, j, ret[:])
            if len(ret) < len(tmp):
                ret = tmp
        if lcs[i][j] == lcs[i][j-1]:
            tmp = track(i, j-1, ret[:])
            if len(ret) < len(tmp):
                ret = tmp
        return ret

ans = track(n, m, [])
# print(ans)
print(len(ans))
print(*map(lambda x:-x, ans[::-1]))

"""
풀이 실패
1시간 반정도 했는데 못 품.

- 방법1:
최대 공통 부분 수열 구한 다음
이 수열에서 최대 증가 찾는 방식으로 하려 했으나,
임의의 LCS가 LIS가 됨이 성립하지 않음.

- 방법2:
LCS로 생성되는 모든 리스트를 만들고 모든 LIS구하기
당연히? 시간초과
"""