"""
Solving Date    : 2023.10.18
Solving Time    : 1h 11m
Title           : RGB거리 2
tags            : 다이나믹 프로그래밍
url             : https://www.acmicpc.net/problem/17404
runtime         : 44 ms
memory          : 31252 KB
"""

import sys
input = sys.stdin.readline

INF = 1000*1001
n = int(input())
rgb = [[*map(int, input().split())] for _ in range(n)]
ans = INF

for start_color in range(3):
    dp = [INF for _ in range(3)]
    dp[start_color] = rgb[0][start_color]

    f = lambda a,b,c:(rgb[i][a]+min(dp[b],dp[c]))
    for i in range(1, n):
        dp = [f(0,1,2), f(1,0,2), f(2,0,1)]

    ans = min([ans]+[dp[i] for i in range(3) if i!=start_color])

print(ans)

"""
기존 RGB거리문제의 2버전

맨 앞과 뒤가 연결되어 이부분을 처리해야한다.

처음에 어떻게든 처음 시작에 대한 정보를 가져야된다 생각해서
dp갱신을 하면서, 기원 색을 저장하는 방식으로 했는데
이 방법은 아예 근본적으로 최적해 자체를 못찾는다.
    - 지금까지의 최적해가 앞뒤연결해도 최적해로 이어지지 않음.
그리고 코드도 더럽다.

이 코드 짠다고 뻘짓 한시간 하다가 갈아엎고

그래서 아예 시작을 고정하고 dp풀이를 3번 반복했다.
n=1000이라서 반복해도 3n이어가지고

=== 아래처럼 했던걸 그냥 코드 줄이고싶어서 위로 바꿈
    for i in range(1, n):
        new_dp = [0 for _ in range(3)]
        new_dp[0] = rgb[i][0] + min(dp[1], dp[2])
        new_dp[1] = rgb[i][1] + min(dp[0], dp[2])
        new_dp[2] = rgb[i][2] + min(dp[0], dp[1])
        dp = new_dp
"""