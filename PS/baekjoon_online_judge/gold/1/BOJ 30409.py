"""
Solving Date    : 2023.11.05
Solving Time    : 43m
Title           : 나비와 전봇대 (Easy)
tags            : 수학, 다이나믹 프로그래밍, 자료 구조, 스택
url             : https://www.acmicpc.net/problem/30409
runtime         : 336 ms
memory          : 51792 KB
"""

import sys
input = sys.stdin.readline

def get_dp(ar, n):
    ret = [0 for _ in range(n)]
    s = []
    for i in range(n):
        while s and s[-1][0] < ar[i]:
            s.pop()
        if s:
            ret[i] = abs(s[-1][0]-ar[i])**2 + (i-s[-1][1])**2 + ret[s[-1][1]]
        s.append([ar[i], i])
    return ret

n = int(input())
ar = [*map(int, input().split())]

L = get_dp(ar, n)
R = get_dp(ar[::-1], n)

for _ in range(int(input())):
    x = int(input())-1
    print(L[x] + R[n-x-1])

"""
2023 제1회 춘배컵

대회 춘배컵에서 풀어보려다가 시간없어서 못 푼 문제.
당시 코드 자체도 못냈지만 풀이방식은 생각했던대로 그대로 풀려서
생각한 시간 +20분정도 하면 실제 풀이시간정도 될듯.

풀이 전 생각할 것:
1. 조건 (전선, 전봇대 교차X)와 (p기준으로 좌우 단조증가)
    - 단조증가를 하는데, 건너뛰지말고 그리디하게 단조증가 하라는 소리.
    - 이렇게 단조증가를 하면 교차 자체가 안됨.
2. 단조증가 조건으로 연쇄적으로 전선이 연결된다. 
3. 길이 합 최대 + 연결 비용 최소
    - 2번의 연쇄적으로 연결되는 경우를 살펴보면
      [1 1 3] 이런식으로 전봇대가 있을 경우
      (1---3), (1-1-3) 이렇게 두가지 연결방법이 있는데,
    3-1. 길이 합 최대가 되려면 당연히 최단거리로 이으면 안된다.
         => 가장 가까운 단조증가 전봇대로 바로 연결.
    3-2. 연결 비용 최소가 되려면
         - (1---3): ((2^2) + (2^2)) = 8
         - (1-1-3): (0 + (1^2)) + ((1^2) + (2^2)) = 6
         이런식으로 최대거리가 되는게 비용이 무조건 적다.
         
         ex) (5-5-5-5) vs (5-_-_-5)
             (1+1+1) = 3 vs (3^2) = 9 로 무조건 인접으로 잇는게 최소비용

접근 방법:
단조증가하는 부분을 해결하기 위해서
높이에 가려지면 앞에만 보이는, 그런 풀이가 생각나서
그 방식으로 하면 되겠다고 생각했다.

왼쪽을 바라볼 때, 오른쪽을 바라볼 때 각각 구해서
특정 인덱스로 조회하면 왼쪽+오른쪽 비용을 합쳐서 양쪽 단조증가를 구현.

그리고 연쇄적으로 연결되는 부분을
처음에 스택에 남아있는걸 가지고 연쇄적으로 처리해줘야하나? 했다가
dp처럼 가장 가까운 단조증가 전봇대 값을 그대로 가져오면 됨을 파악.
(풀이전 생각할것 3번에서)

풀이:
스택을 이용해서 단조증가 리스트를 생성했다.
(큰->작은 순으로 읽고 처리하니까 단조감소인가)
1. 원소를 순서대로 읽으면서 처리한다.
    (맨 처음엔 스택이 비어있기때문에 1, 2가 생략되고 3부터 실행된다.)
    1-1. 현재 원소보다 작은 값이 스택에 들어있지 않을 때 까지 pop
    1-2. 스택에 값이 있을 경우 == 단조증가 한 경우.
        - 스택의 값과 인덱스로 비용을 계산하여 저장한다.
        - 연쇄적으로 비용이 필요하기때문에, 최근 단조증가 했던 비용을 더해서 저장.
    1-3. 스택에 넣는다.
        - 원소값과 인덱스를 같이 저장.
        - 단조증가가 아닐 경우 다음 1의 과정에서 pop되므로 조건없이 push
2. 1에서 처리한 반대 순서로, 역방향 단조증가 리스트를 생성한다.
3. 전봇대 p에 해당하는 위치의 (순방향+역방향)값 출력.
"""