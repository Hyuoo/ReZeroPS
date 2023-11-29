"""
Solving Date    : 2023.11.28
Solving Time    : 55m
Title           : 돌베어 법칙
tags            : 수학, 그리디 알고리즘
url             : https://www.acmicpc.net/problem/30012
runtime         : 392 ms
memory          : 31120 KB
"""

_ = input()
a = input().strip(".")
n = len(a)
ans = 2023

for p in range(1, n+1):
    tmp_ans = a[:p].count("#")
    for i in range(p, n):
        if a[i]=="#" and a[i-p]==".":
            tmp_ans += 1
    ans = min(ans, tmp_ans)

print(0 if ans==2023 else ans)

"""
제 1회 선린 프로그래밍 챌린지 Open Contest

계속 시간초과, 틀렸습니다 보고 해설 보고 푼 문제.


처음 풀이를 주기별로, 모든 연속된 '#'을 찾는 방식으로 구현했는데,
(2중 for문) + (각 #길이만큼 while반복)으로 시간초과

한참 고민하다가 해설 보고,
이전 주기에서 안 운 귀뚜라미가 새 귀뚜라미인걸 이용해서 풀이.
"""