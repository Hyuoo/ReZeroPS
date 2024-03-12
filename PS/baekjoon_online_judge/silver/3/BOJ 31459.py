"""
Solving Date    : 2024.03.06
Solving Time    : 6m
Title           : 초콜릿과 ㄱ나이트 게임 (Sweet)
tags            : 그리디 알고리즘
url             : https://www.acmicpc.net/problem/31459
runtime         : 124 ms
memory          : 31120 KB
"""

for _ in range(int(input())):
    X, Y, x, y = map(int, input().split())
    ans = 0
    while X>x and Y>y:
        ans += (X*Y) - (X-x) * (Y-y)
        X -= x*2
        Y -= y*2
    if X>0 and Y>0:
        ans += X*Y
    print(ans)

"""
젤먼저 푼건 6분이지만, 제대로 푼건 쫌 걸렸다.

처음에 이렇게 그냥 set써서 대충 풀었는데, 940ms 나왔다.
for _ in range(int(input())):
    x, y, a, b = map(int, input().split())
    check = set()
    count = 0
    for i in range(y):
        for j in range(x):
            if (i, j) not in check:
                check.add((i, j))
                check.add((i+b, j+a))
                count += 1
    print(count)

======
풀고나서 문제 분류 보니까 그리디 적혀있길래
어 깡수학 아니고 그리디면 생각좀 해보면 되지않을라나? 해서 제대로 풀이.

(0, 0)부터 채운다고 생각하면 (x, y)부터 수평수직으로 선긋고 남는 영역이 둘 수 있는 공간이다.

ex) x=2, y=1 일 때 아래와 같은 양상.
OOOOOOOO
OOXXXXXX
OOXX????
OOXX????

이렇게 한세트씩 그리디하게 세면 된다.
- (X*y) + (Y*x) - (x*y)
- (X*Y) - (X-x) * (Y-y)
둘 중 아무거나 하고싶은대로 계산하면 될 듯.
하면서 X, Y 는 2x, 2y씩 줄이면서 반복.

이러고 끝나는 구간만 잘 처리하면 된다.
"""