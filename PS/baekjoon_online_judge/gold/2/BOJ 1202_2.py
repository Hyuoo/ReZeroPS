"""
Solving Date    : 2023.09.20
Solving Time    : -
Title           : 보석 도둑
tags            : 자료 구조,그리디 알고리즘, 정렬, 우선순위 큐
url             : https://www.acmicpc.net/problem/1202
runtime         : 1344 ms
memory          : 98300 KB
"""

import sys
input = sys.stdin.readline
import heapq

n, k = map(int, input().split())

jewels = sorted(tuple(map(int, input().split())) for _ in range(n))
bags = sorted(int(input()) for _ in range(k))

i = 0
ans = 0
selected = []
for bag in bags:
    while i<n and jewels[i][0]<=bag:
        heapq.heappush(selected, -jewels[i][1])
        i+=1
    if selected:
        ans -= heapq.heappop(selected)
print(ans)

"""
보석도 힙으로 하기엔 낭비같아서 인덱스로 이어서 계속 했는데
속도는 훨 빨라졌는데 왜 메모리가 늘엇지

heappop하면서 리스트 크기가 줄어드는게 메모리 사용량에 의미가 있는건가?

jewels = sorted([tuple(map(int, input().split())) for _ in range(n)], reverse=True)
요래 하고 [-1]로, pop 하는 식으로 하면
87504 KB	1148 ms
되긴 하는데, 지금이 더 이해하는데에는 직관적인 것 같아서 놔둠.
"""