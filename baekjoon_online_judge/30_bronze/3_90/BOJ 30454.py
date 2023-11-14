"""
Solving Date    : 2023.11.14
Solving Time    : -
Title           : 얼룩말을 찾아라!
tags            : 구현, 문자열
url             : https://www.acmicpc.net/problem/30454
runtime         : 120 ms
memory          : 31120 KB
"""

_,*l = open(0)
p = [("0"+i).count("01") for i in l]
print(max(p), p.count(max(p)))

"""
2023 건국대학교 프로그래밍 경진대회 (KUPC) Open Contest · Arena #10
A번 문제

다른 풀이 방법 보다가.

붙어있는 1 개수를 세기 위한 방법이
주어진 문자열 S에서
"0"+S 한 뒤, "01"의 개수를 세면 된다.

이런걸 왜 생각못했나 싶어 저장.

=== 기존 풀이 (대회)
n, l = map(int, input().split())
m = 0
c = 0
for _ in range(n):
    t = len([i for i in input().split("0") if i])
    if t>m:
        m = t
        c = 1
    elif t==m:
        c += 1
print(m, c)
"""