"""
Solving Date    : 2023.12.06
Solving Time    : 21m
Title           : 계보 복원가 호석
tags            : 자료 구조, 그래프 이론, 정렬, 해시를 사용한 집합과 맵, 위상 정렬, 방향 비순환 그래프
url             : https://www.acmicpc.net/problem/21276
runtime         : 820 ms
memory          : 88256 KB
"""

import sys
input = sys.stdin.readline

n = int(input())
names = sorted(input().split())

m = int(input())
g = {name:set() for name in names}
dep = {name:0 for name in names}
result = {name:[] for name in names}
q = set(names)

for _ in range(m):
    a, b = input().split()
    g[b].add(a)
    dep[a] += 1
    q.discard(a)

print(len(q))
print(*sorted(q))

while q:
    now = q.pop()
    for nxt in g[now]:
        dep[nxt] -= 1
        if dep[nxt] == 0:
            result[now].append(nxt)
            q.add(nxt)

for name in names:
    tmp = sorted(result[name])
    print(name,len(tmp),*tmp)

"""
접근방법:
- 조상을 가리키는 입력이 주어지는데, 뒤집어서 자손을 가리키는 그래프를 만든다.
    - 최초 의존성이 0이면 조상
    - 이후 조상부터 탐색하며 의존성이 0이 되는 자손이 있으면 직계자손.
    - 직계자손일 경우 조상의 리스트에 저장
- 중복된 이름이 없기 때문에 set을 사용해서 성능을 높였다.
"""