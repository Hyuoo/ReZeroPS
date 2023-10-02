"""
Solving Date    : 2023.10.02
Solving Time    : Fail (3h over)
Title           : 팰린드롬 공장
tags            : 다이나믹 프로그래밍, 브루트포스 알고리즘
url             : https://www.acmicpc.net/problem/1053
runtime         : -
memory          : -
"""

isbound = lambda i, j:(i>=0 and i<n and j>=0 and j<n)

st = input()
n = len(st)
s, e = 0, n-1
# print(st)

dp = [[[9999, False, set()] for _ in range(n)] for _ in range(n)]
dp[s][e][0] = 0

# for i in dp:
#     print(*i, sep="\t\t")
# print("="*90)

for l in range(n-1, -1, -1):
    for i in range(n-l):
        # print(f"({i}-{i+l})", end=", ")
        s = i
        e = i+l
        if not isbound(s, e):
            continue

        dp_count = []
        dp_flag = False
        dp_set = set()
        for x, y in [(-1, 1), (-1, 0), (0, 1)]:
            if isbound(s+x, e+y):
                dp_tmp = dp[s+x][e+y]
                dp_count.append(dp_tmp[0])
                dp_flag |= dp_tmp[1]
                dp_set.update(dp_tmp[2])

        if dp_count:
            dp[s][e][0] = min(dp_count)
        dp[s][e][1] = dp_flag
        if not dp[s][e][1]:
            dp[s][e][2] = dp_set

        if st[s] != st[e]:
            dp[s][e][0] += 1
            if not dp[s][e][1] and isbound(s-1, e+1):
                if st[s] in dp[s][e][2] or st[e] in dp[s][e][2]:
                    dp[s][e][0] -= 1
                    dp[s][e][1] = True
                dp[s][e][2].update([st[s], st[e]])

# for i in dp:
#     print(*i, sep="\t\t")
# print("="*90)

print(min(dp[i][i][0] for i in range(n)))

"""
왼쪽 오른쪽 기준 잡고 (left, right)

1. 삽입
    1-1. 왼쪽 삽입 (right-1)
    1-2. 오른쪽 삽입 (left+1)
2. 제거
    2-1. 왼쪽 제거 (left+1)
    2-2. 오른쪽 제거 (right-1)
3. 변환
    3-1. 왼쪽 변환 (l+1, r-1) 
    3-2. 오른쪽 변환 (l+1, r-1)
4. 일단 논외

연산종류마다 결과기준으로 3개 케이스로 나누어서
l, r이 움직이는 방식으로 구분

dp[l][r] = lr을 포함한 바깥부분이 팰린드롬이 될 경우 최소행동
    -> 근데 이걸 포함하지 않는 으로 바꿔야 될 것 같음.

- 아무튼 그래서 l, r 각각 하나씩만 움직일 경우
    무조건 삽입 또는 삭제라서 +1 (min(l-1, r+1))
- l, r이 동시에 움직일 경우
    - string[l]==string[r]: 최소값 유지
    - string[l]!=string[r]: +1 (l-1,r+1)

이런식으로 접근.

그리고 4번 연산의 경우엔
동시에 움직인 경우 양 문자를 set에 넣고,
이후에 같은 문자가 한번이라도 나오면 flag를 둬서 -1 해주는 방식.
"""
