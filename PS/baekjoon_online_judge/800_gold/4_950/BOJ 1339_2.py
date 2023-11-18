"""
Solving Date    : 2023.09.17
Solving Time    : -
Title           : 단어 수학
tags            : 그리디 알고리즘
url             : https://www.acmicpc.net/problem/1339
runtime         : 40 ms
memory          : 31256 KB
"""

n = int(input())

alpha = [0 for _ in range(26)]
for _ in range(n):
    for i, c in enumerate(input()[::-1]):
        alpha[ord(c)-65] += 10**i

ans = 0
for i, v in enumerate(sorted(alpha, reverse=True)):
    ans += (9-i)*v
print(ans)

"""
딕셔너리 쓸 필요도 없잖아?
-- 무슨 문자 였는지 저장 할 필요도 없잖아?
"""