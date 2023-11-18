"""
Solving Date    : 2023.10.02
Solving Time    : 5h over
Title           : 팰린드롬 공장
tags            : 다이나믹 프로그래밍, 브루트포스 알고리즘
url             : https://www.acmicpc.net/problem/1053
runtime         : 1012 ms
memory          : 31256 KB
"""

def get_dp(st, s, e):
    if dp[s][e] != 99:
        return dp[s][e]
    if s>=e:
        return 0
    dp[s][e] = min(get_dp(st, s, e-1) + 1, get_dp(st, s+1, e) + 1, get_dp(st, s+1, e-1) + int(st[s] != st[e]))
    return dp[s][e]

st = input()
n = len(st)
dp = [[99 for _ in range(n)] for _ in range(n)]

ret = get_dp(st, 0, n-1)

for i in range(n-1):
    for j in range(i+1, n):
        dp = [[99 for _ in range(n)] for _ in range(n)]
        new_st = list(st)
        new_st[i], new_st[j] = new_st[j], new_st[i]
        ret = min(ret, get_dp(new_st, 0, n-1)+1)

print(ret)

""" 풀이 실패 코드
def foo(st):
    # print(st)
    n = len(st)
    get_dp = lambda s, e: (999 if s < 0 or s >= n or e < 0 or e >= n else dp[s][e])
    dp = [[999 for _ in range(n)] for _ in range(n)]
    dp[0][n - 1] = 0

    for l in range(n - 2, -1, -1):
        for i in range(n - l):
            # print(f"[{i}][{i+l}]", end=", ")
            s, e = i, i + l
            dp[s][e] = min(get_dp(s - 1, e + 1) + int(st[s] != st[e]), get_dp(s - 1, e) + 1, get_dp(s, e + 1) + 1)

    # for i in dp:
    #     print(*i, sep="\t\t")
    # print("=" * 50)

    return min(dp[i][i] for i in range(n))
=========================================
무조건 최종적으로 같은인덱스인 케이스까지 가기 때문에
abba
3		2		1		0
999		1		0		1
999		999		1		2
999		999		999		3
이런식으로 팰린드롬임에도 짝수인 케이스 안맞음.
마지막에 [i][i]만 검사해서.
-> 대각으로만 내려오는 케이스 못합침.
-> bottom-up 방식으로 다시 해야할 듯.

==== bottomup 풀이
dp[i][j] 는 i, j까지를 팰린드롬으로 만들 때 연산횟수

아예 없는 0부터 시작해서,
- 추가/제거는 직각이동 + 1
- 변환은 조건부+1 (st[i]!=st[j])

그리고 문자 스왑은 완전탐색.
"""