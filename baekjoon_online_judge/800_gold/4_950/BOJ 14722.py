"""
Solving Date    : 2023.10.12
Solving Time    : 27m
Title           : 우유 도시
tags            : 다이나믹 프로그래밍
url             : https://www.acmicpc.net/problem/14722
runtime         : 1824 ms
memory          : 38112 KB
"""

import sys
input = sys.stdin.readline

n = int(input())
ar = [[2 for _ in range(n+1)]]
ar.extend([[2]+list(map(int, input().split())) for _ in range(n)])
dp = [[0,0,0] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        for m in range(3):
            if m==ar[i][j]:
                p = (m-1)%3
                tmp = max(dp[j-1][p], dp[j][p])
                if tmp==0 and m!=0:
                    continue
                dp[j][m] = tmp+1
            else:
                dp[j][m] = max(dp[j-1][m], dp[j][m])

print(max(dp[-1]))

"""
좌상단에서 우하단으로 순방향으로만 나아가면서
딸기 초코 바나나 순서대로(1-2-3) 반복을
할 수 있는 최대 길이 찾기

각 칸마다 [딸기, 초코, 바나나]를 마신 해를 저장해서
딸기면 바나나+1, 초코면 딸기+1
그리고 나머지는 그대로 최대값

이렇게 했는데 오답나와서
line25: **처음은 무조건 딸기** 라는 조건을 추가했다.
"""