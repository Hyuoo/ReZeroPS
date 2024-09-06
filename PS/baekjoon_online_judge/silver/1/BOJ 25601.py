"""
Solving Date    : 2024.09.06
Solving Time    : 11m
Title           : 자바의 형변환
tags            : 자료 구조, 그래프 이론, 그래프 탐색, 트리, 해시를 사용한 집합과 맵
url             : https://www.acmicpc.net/problem/25601
runtime         : 128 ms
memory          : 51256 KB
"""

import sys
input = sys.stdin.readline

def chk_p(t, target):
    while t:
        t = g.get(t, "")
        if t == target:
            return 1
    return 0

n = int(input())
g = {}

for _ in range(n-1):
    child, parent = input().split()
    g[child] = parent

a, b = input().split()

print(chk_p(a, b) or chk_p(b, a))

"""
상속 개념에서 부모-자식 관계가 성립되는지 체크하는 문제

다중상속이 안되기 때문에 쉬운 문제
- 상속관계가 ( A >> [B, C] )는 되고 ( [A, B] >> C )는 안되기 때문에
  위로(부모방향) 타고 올라가면 갈림길이 없어서,
  윗방향만 저장하고 타고 올라가며 체크하면 된다.

가능)   불가능)
  A      A   B
 / \      \ /
B   C      C

그냥 재귀로 타고 올라가면서 다른하나가 존재하는지 체크하면 끝
"""