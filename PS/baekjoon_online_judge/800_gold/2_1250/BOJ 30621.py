"""
Solving Date    : 2023.11.12
Solving Time    : 약 20m
Title           : 어? 금지
tags            : 다이나믹 프로그래밍, 이분 탐색
url             : https://www.acmicpc.net/problem/30621
runtime         : 720 ms
memory          : 50356 KB
"""

z=lambda:[*map(int, input().split())]

n = int(input())
t, b, c = [[0]+z() for _ in range(3)]
tot = [0 for _ in range(n+1)]

for i in range(n+1):
    past = t[i]-b[i]
    l, r = 1, i
    while l<=r:
        m = (l+r)//2
        if t[m] < past:
            l = m+1
        else:
            r = m-1
    tot[i] = max(tot[i-1], tot[l-1]+c[i])
print(tot[-1])

"""
2023 Sogang Programming Contest Open (Master) · Arena #12
E번 문제

어?

누가봐도 DP하게 푸는 문제.
다만,
- DP를 비교하는 기준이 고정되어있지 않고
- 기준이 존재하지 않을 수도 있기 때문에
이부분에 대해서 처리를 하는게 어려운 문제.

이 때문에 넓은 범위를 항상 스캔해야해서 이분탐색을 사용했다.

--- 1.
대회때 제출한 코드는
(past == 0)일 때와
(t[m] == past)일 때 break를 해주는 식으로
분기를 덜 돌게 한다고 했는데,
시간이 더 오래걸린다.

--- 2.
다른 문제에서도 그렇고
bisect 라이브러리를 쓴 게
성능이 압도적으로 차이난다. 뫄고
"""