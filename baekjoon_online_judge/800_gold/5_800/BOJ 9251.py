"""
Solving Date    : 2023.09.22
Solving Time    : 27m
Title           : LCS
tags            : 다이나믹 프로그래밍, 문자열
url             : https://www.acmicpc.net/problem/9251
runtime         : 592 ms
memory          : 56408 KB
"""

a = input()
b = input()

dp = [[0 for _ in range(len(a)+1)] for _ in range(len(b)+1)]
# print("    ",*a,sep="  ")
for j in range(len(b)):
    for i in range(len(a)):
        if b[j] == a[i]:
            dp[j+1][i+1] = dp[j][i] + 1
        else:
            dp[j+1][i+1] = max(dp[j+1][i], dp[j][i+1])
    # print([*b, " "][j-1], dp[j])
# print(b[-1], dp[len(b)])
print(dp[-1][-1])

"""
역시 어제 배운 LCS 알고리즘
그대로 구현.

최대길이 유지 한 채로, 일치 문자일 경우 +1

      A  C  A  Y  K  P
  [0, 0, 0, 0, 0, 0, 0]
C [0, 0, 1, 1, 1, 1, 1]
A [0, 1, 1, 2, 2, 2, 2]
P [0, 1, 1, 2, 2, 2, 3]
C [0, 1, 2, 2, 2, 2, 3]
A [0, 1, 2, 3, 3, 3, 3]
K [0, 1, 2, 3, 3, 4, 4]

..타 풀이에 212ms에 이거 머냐
다른 실행 짧은것도 동일코드네.
S1 = input()
S2 = input()
L = [0]*len(S2)
for i in range(len(S1)):
    c = 0
    for f in range(len(S2)):
        if(c < L[f]):
            c = L[f]
        elif(S1[i] == S2[f]):
            L[f] = c + 1
print(max(L))
"""