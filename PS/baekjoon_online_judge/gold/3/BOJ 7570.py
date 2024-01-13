"""
Solving Date    : 2024.01.08
Solving Time    : 28m
Title           : 줄 세우기
tags            : 다이나믹 프로그래밍, 그리디 알고리즘
url             : https://www.acmicpc.net/problem/7570
runtime         : 524 ms
memory          : 144340 KB
"""

n = int(input())
ar = [*map(int, input().split())]
dp = [0 for _ in range(n+1)]

for i in ar:
    dp[i] += dp[i-1]+1

print(n-max(dp))

"""
치팅했다.

특정 어린이를 지정위치가 아닌, 맨 앞이나 뒤로 보내야 하기 때문에
단순히 최장 증가면 안되고, *연속된* 최장 증가여야 한다.

lis 풀이 방법 중
전체 원소값 사이즈의 배열을 만들어놓고
앞선 원소 중 작은 모든 값의 최댓값에서 +1 하는 방식이 있는데,
그걸 변형해서
앞선 원소 중 1 작은 값에서만 최대길이 +1 하는 방식으로 풀이하면 된다.
"""