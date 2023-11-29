"""
Solving Date    : 2023.11.29
Solving Time    : 1h 26m
Title           : 공부 계획하기
tags            : 다이나믹 프로그래밍
url             : https://www.acmicpc.net/problem/30016
runtime         : 168 ms
memory          : 31120 KB
"""

import sys
input = sys.stdin.readline

n, t = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]
d = list(map(int, input().split()))
pdp = [[0, []] for _ in range(t+1)]

for i in range(n):
    ndp = [[-1, []] for _ in range(t + 1)]
    for j in range(t+1):
        for k in range(t-j+1):
            if pdp[k][0]+s[i][j] > ndp[k+j][0]:
                ndp[k+j] = [pdp[k][0]+s[i][j], pdp[k][1]+[j]]
    pdp = ndp
    # print(pdp)

v = -10001
a = []
for i in range(t+1):
    if v < pdp[i][0]-d[i]:
        v = pdp[i][0]-d[i]
        a = pdp[i][1]

print(v)
print(*a)

"""
제 1회 선린 프로그래밍 챌린지 Open Contest

ㅋ 풀이 방식은 맞았으나
문제 제대로 이해 못해서 30분을 더 풀었다.

접근 방식:
dp를 이용해서 0~t초 까지의 베스트를 저장함.
- t가 4일 때,
    - 몇번째인진 안중요하고 dp[2]를 갱신한다고 한다면
      dp[2]는 "총" 2시간을 공부했을 때의 베스트.
        - 고로 2+0, 2+1, 2+2 세가지 경우가 가능하다. (<t)
이 규칙을 가지고 (과목, 시간) 순서대로 베스트값 처리를 반복한다.

풀이:
- pdp는 이전까지의 dp, ndp는 현재의 dp값을 갱신했다.
- 과목 당 모든 시간의 베스트가 갱신되어야 하기 때문에 과목단위로 ndp를 초기화.
- dp의 시간 기준이 아니라, 현재 공부하는 과목의 시간이 기준이라서
  가능 한 시간의 모든 dp를 계속해서 최댓값으로 갱신해줬다.
    ex) 현재 2시간 공부, 총 4시간일 때
        => (이전 0시간 + 현재 2시간) 합 2시간,
           (이전 1시간 + 현재 2시간) 합 3시간,
           (이전 2시간 + 현재 2시간) 합 4시간
  이렇게 과목 단위로 dp[2], dp[3], dp[4] 계속해서 갱신
- 과목의 모든 시간이 고려가 끝나면 pdp=ndp로 덮어쓰기 한 뒤, 반복한다.


내 에바사항:
- 처음 t시간 패널티로 점수 감소를 각 과목별로 생각하여
  실제 오르는 점수는 s[i][j]-d[j]라고 생각하고 풀었다.
  이걸 몰라서 30분 헤멨다.
"""