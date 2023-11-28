"""
Solving Date    : 2023.10.02
Solving Time    : Fail (6h over)
Title           : 팰린드롬 공장
tags            : 다이나믹 프로그래밍, 브루트포스 알고리즘
url             : https://www.acmicpc.net/problem/1053
runtime         : -
memory          : -
"""

def foo(st):
    # print(st)
    n = len(st)
    dp = [[999 for _ in range(n)] for _ in range(n)]
    ret = 999

    for s in range(n):
        for e in range(n - 1, -1, -1):
            # print(f"[{i}][{i+l}]", end=", ")
            if s==0 and e==n-1:
                dp[s][e] = 0
                continue
            if s==0:
                dp[s][e] = dp[s][e+1] + 1
            elif e==n-1:
                dp[s][e] = dp[s-1][e] + 1
            else :
                dp[s][e] = min(dp[s-1][e+1] + int(st[s-1] != st[e+1]), dp[s-1][e] + 1, dp[s][e+1] + 1)
            if s>=e:
                ret = min(ret, dp[s][e])
            if s>e:
                break

    # for i in dp:
    #     print(*i, sep="\t")
    # print("-"*50)

    return ret

st = input()
ret = foo(st)

for i in range(len(st)):
    for j in range(i+1, len(st)):
        new_st = list(st)
        new_st[i], new_st[j] = new_st[j], new_st[i]
        ret = min(ret, foo(new_st) + 1)

print(ret)

"""
기존에 문자열이 짝수 쌍일 때 안되던걸
다른 풀이 보다가, 더 깊이 하면 되겠다 해서 재시도.

근데 왜 안되냐

계속 안되길래 완전 코드 카피하듯 했는데도 틀린다.
뭐가문제지
"""