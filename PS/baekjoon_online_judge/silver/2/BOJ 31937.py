"""
Solving Date    : 2024.07.12
Solving Time    : 24m
Title           : 로그프레소 마에스트로
tags            : 구현, 브루트포스 알고리즘, 정렬, 시뮬레이션
url             : https://www.acmicpc.net/problem/31937
runtime         : 696 ms
memory          : 33164 KB
"""

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
badcom = [*map(int, input().split())]

log = []
for _ in range(m):
    log.append([*map(int, input().split())])
log.sort()

final_situ = set(badcom)

for real_badcom in badcom:
    s = set([real_badcom])
    
    for _, a, b in log:
        if a in s:
            if b not in final_situ:
                break
            s.add(b)
    else:
        if s == final_situ:
            print(real_badcom)
            exit(0)

"""
우선, max(N) => 1000, max(M) => 10000 으로 케이스가 적다.
감염 순서를 추적해야 하기 때문에 로그 개수만큼 반복이 일어나기 때문에 t와 K는 무시해도 될 것

- 감염이 줄어들지는 않는다.
    - 즉, 마지막 감염되어있는 컴퓨터 중에서만 최초 후보가 된다.

접근1. 파일전송방향을 그래프로 나타내면 한번에 파악되지 않을까
- 특정 시점을 기준으로 감염이 진행되기 때문에 순서를 제외하면 감염순서 파악 불가

접근2. 최초 후보를 정해놓고 전송 로그를 모두 시뮬레이션
- 파일 전송 로그를 시간(t)으로 정렬 한 뒤, 최초 후보 수 만큼 시뮬레이션
- 주의할 점은, 모든 전송이 끝난 뒤의 최종상태가 주어진 감염상태와 동일해야 한다.
    - 중간에 이미 만족하더라도 해당 케이스는 다른 결과가 나올 수 있음.

---
- 최종상태에 감염되지 않은 컴퓨터가 감염 될 경우, break하여 시간을 줄이기
- 로그 앞 부분에서 후보가 아닌 컴퓨터로부터의 전송은 스킵하여 시간 더 줄일 수 있을 듯
"""
