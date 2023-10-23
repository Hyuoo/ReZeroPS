"""
Solving Date    : 2023.10.23
Solving Time    : 7m
Title           : 패션왕 신해빈
tags            : 수학, 자료 구조, 조합론, 해시를 사용한 집합과 맵
url             : https://www.acmicpc.net/problem/9375
runtime         : 60 ms
memory          : 31120 KB
"""

for _ in range(int(input())):
    n = int(input())
    ans = 1
    c = {}
    for _ in range(n):
        a, b = input().split()
        c[b] = c.get(b, 0)+1
    for k in c:
        ans *= c[k]+1
    print(ans-1)

"""
프로그래머스 '의상' 문제와 동일한 문제.
https://school.programmers.co.kr/learn/courses/30/lessons/42578

옷 종류마다 '안입는'케이스도 포함시켜서 다 곱한 뒤,
1을 빼주면 됨. (모든종류를 안입는 경우)
"""