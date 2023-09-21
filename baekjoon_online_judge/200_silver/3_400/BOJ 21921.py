"""
Solving Date    : 2023.09.20
Solving Time    : -
Title           : 블로그
tags            : 누적 합, 슬라이딩 윈도우
url             : https://www.acmicpc.net/problem/21921
runtime         : 276 ms
memory          : 63924 KB
"""

n, x = map(int, input().split())
ar = [0]+[*map(int, input().split())]

for i in range(n):
    ar[i+1] += ar[i]

max_p = 0
nums = {}
for i in range(n-x+1):
    p = ar[i+x]-ar[i]
    nums[p] = nums.get(p, 0) + 1
    max_p = max(max_p, p)

print(f"{max_p}\n{nums[max_p]}" if max_p else "SAD")

"""
누적 합과 슬라이딩 윈도우 두가지 풀이 방식 중
누적 합 풀이

임의의 구간 합을 계산하기 쉽게하기 위해서 누적합을 사용하지만,

구간 합의 "구간"이 항상 일정하기 때문에
슬라이딩 윈도우 방식이 더 효율적이다.
"""