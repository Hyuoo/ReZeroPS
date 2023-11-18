"""
Solving Date    : 2023.11.15
Solving Time    : -
Title           : 낚시
tags            : 다이나믹 프로그래밍, 누적 합
url             : https://www.acmicpc.net/problem/30461
runtime         : 3192 ms
memory          : 190100 KB
"""

import sys
input = sys.stdin.readline

n, m, q = map(int, input().split())
lake = [[*map(int, input().split())] for _ in range(n)]

for i in range(n-1):
    for j in range(m):
        lake[i+1][j] += lake[i][j]

for i in range(n-1):
    for j in range(m-1):
        lake[i+1][j+1] += lake[i][j]

for _ in range(q):
    a, b = map(lambda x:int(x)-1, input().split())
    print(lake[a][b])

"""
2023 건국대학교 프로그래밍 경진대회 (KUPC) Open Contest · Arena #10
H번 문제

인덱스로 여러번 풀이를 출력하는 걸 보니,
절대로 칸별로 답을 구해야 하는 문제.

왼쪽위 대각선으로 가면서 위쪽에 있는 모든건 낚으니
해당 값들을 누적합으로 만들어준다.

아래방향으로 쭉 누적합하고
아래오른쪽방향으로 쭉 누적합 하고
인덱스 접근으로 바로 값 출력.

--- 다른 풀이 보고
lake[i][j] = lake[i-1][j] + lake[i-1][j-1] - lake[i-2][j-1]
이런식으로 입체적으로 누적합을 구할 수도 있다.
빼기를 안하면 누누적적합합이 되어버륌
"""