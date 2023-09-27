"""
Solving Date    : 2023.09.27
Solving Time    : 16m
Title           : 팀 이름 정하기
tags            : 구현, 문자열, 정렬
url             : https://www.acmicpc.net/problem/1296
runtime         : 44 ms
memory          : 31256 KB
"""

a = [0 for _ in range(26)]
for c in input():
    a[ord(c)-65] += 1

teams = []
for _ in range(int(input())):
    b = a.copy()
    team_n = input()

    for c in team_n:
        b[ord(c)-65] += 1

    L, O, V, E = b[11], b[14], b[21], b[4]
    s = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
    teams.append([-s, team_n])

print(sorted(teams)[0][1])

"""
아니 문제 뭔소린지 한참읽었네;
"""