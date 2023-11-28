"""
Solving Date    : 2023.09.19
Solving Time    : 1h 27m
Title           : 보석 도둑
tags            : 자료 구조,그리디 알고리즘, 정렬, 우선순위 큐
url             : https://www.acmicpc.net/problem/1202
runtime         : 1684 ms
memory          : 87620 KB
"""

import sys
input = sys.stdin.readline
import heapq

n, k = map(int, input().split())

jewels = sorted(tuple(map(int, input().split())) for _ in range(n))
bags = []

for _ in range(k):
    heapq.heappush(bags, int(input()))

ans = 0
selected = []
while bags:
    bag = heapq.heappop(bags)

    while jewels and jewels[0][0]<=bag:
        heapq.heappush(selected, -heapq.heappop(jewels)[1])
    if selected:
        ans -= heapq.heappop(selected)
print(ans)

"""
가방에 무게기반으로 보석 가치 최적화하는 문제

풀이:
1. 작은 가방부터 채운다.
2. 넣을 수 있는 것 중 젤 비싼걸 선택해서 넣는다.

접근:
첨에 암튼 그리디하게 하면 된다고 생각하고 접근했다.

fit하게 들어가는게 베스트. 인데 어떻게?
1. 가치기준 - 고가치 우선으로 선택
    1-1. 무게 무거운거부터
    1-2. 무게 가벼운거부터
    근데 가치 기준으로하면 결국 가방을 채우는거라 순서가 엉망진창 - 기각
    
2. 가방기준 - 작은 가방부터 채우기
    2-1. 제일 비싼거 채우면 된다.
        *그런데 넣을 수 있는 것 중에

근데 시간이 빡빡한 문제라 힙을 써서 시간을 단축해야 한다.


힙을 써서 
1. 처음 모든 보석
2. 챙길 수 있는 모든 보석
3. 챙긴 보석
세가지 범주로 나눠서 생각.

1. 먼저 가방을 작은 것부터 순서대로 채운다.
    1-1. 가방에 챙길 수 있는 보석을 일단 다
        (처음 모든 보석)에서 (챙길 수 있는 모든 보석)으로 옮긴다.
    1-2. (챙길 수 있는 모든 보석)에서 제일 비싼걸 (챙긴 보석)으로 옮긴다.
끝

이렇게하면 처음에 가능한 보석에서 챙긴 보석으로 옮기면
그 보석만을 제거 해줘야 하는데 어떻게 하는지 이해가 안됐다.

근데 작은 가방부터 차례로 챙기기 때문에 작은 가방에서
(챙길 수 있는 모든 보석)으로 이동 한 보석들은
다음 크기 가방에서도 (챙길 수 있는 모든 보석)에 그대로 남는다.

그래서 1개만 빼고 나머지는 이어서 계속 진행하면 된다.
 -- 얘떔에 진짜 한시간동안 고민
"""