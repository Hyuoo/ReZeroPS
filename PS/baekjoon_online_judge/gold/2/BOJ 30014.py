"""
Solving Date    : 2023.11.28
Solving Time    : 23m
Title           : 준영이의 사랑
tags            : 자료 구조, 그리디 알고리즘, 정렬, 애드 혹, 덱
url             : https://www.acmicpc.net/problem/30014
runtime         : 44 ms
memory          : 31120 KB
"""

n = int(input())
a = sorted(map(int,input().split()))
b = [*a[::2], *a[1::2][::-1]]

ret = 0
for i in range(n):
    ret += b[i-1]*b[i]

print(ret)
print(*b)

"""
제 1회 선린 프로그래밍 챌린지 Open Contest

그냥 순서대로 지그재그로 배치하면 되는거 아냐?
이렇게 쉽다고? 했는데 정답이었다.

비슷한 문제: S4 donstructive (https://www.acmicpc.net/problem/30618)
위 문제는 수열이라서 가운데부분에 큰숫자가 최대한 몰려있으면 되어서
직관적으로 큰 수부터 몰아넣었다.

근데 이 문제의 경우에는
[a, b, c] 이렇게 있을 때, b로 기준을 잡으면
- (a*b + b*c) == (a+c)*b가 되므로
    마땅히 a+c랑 b가 같이 커야하니까
1. 가운데 b를 큰 숫자를 놓는다.
2. (a+c)가 크도록, 순서대로 큰 숫자를 놓는다.
하면 자연스럽게 지그재그로 배치가 된다.

나머지 부분들도 b를 다시 쓰기 때문에
a+c와 b를 밸런스있게 고르기 위해서 고민하지 않아도 된다.
(그리디하게 큰 숫자부터 배치)
"""