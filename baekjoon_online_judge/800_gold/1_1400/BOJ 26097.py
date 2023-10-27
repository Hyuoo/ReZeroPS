"""
Solving Date    : 2023.10.26
Solving Time    : 약 1h 30m
Title           : 효구와 호규 (Hard)
tags            : 그래프 이론, 그래프 탐색, 애드 혹, 비둘기집 원리
url             : https://www.acmicpc.net/problem/26097
runtime         : 2180 ms
memory          : 183592 KB
"""

import sys
input = sys.stdin.readline

def foo_p(ax, ay, bx, by, d):
    ret = []
    for i in range(n):
        for j in range(m):
            if (i==ax and j==ay) or (i==bx and j==by):
                continue
            if ar[i][j]==d:
                ret.append([i+1, j+1])
    return ret

def foo(ax, ay, bx, by):
    print(1)
    ret = [[ax+1, ay+1], [bx+1, by+1]]
    sep = 0

    for i in range(2):
        ret.extend(foo_p(ax, ay, bx, by, i))

    for p in ret:
        print(*p, end=" \n"[sep])
        sep^=1

n, m = map(int, input().split())
ar = []
c = 0

for _ in range(n):
    ar.append(tmp := [*map(int, input().split())])
    c += sum(tmp)

if n*m%2 or c%2:
    print(-1)
else:
    for i in range(n-1):
        for j in range(m-1):
            if ar[i][j] == ar[i+1][j]:
                foo(i, j, i+1, j)
                exit(0)
            elif ar[i][j] == ar[i][j+1]:
                foo(i, j, i, j+1)
                exit(0)
    print(-1)

"""
# pypy로 제출하니까 (824 ms, 247640 KB)

효구와 호규 (Easy)(https://www.acmicpc.net/problem/26085)
위 문제를 풀고나서 바로 푼 문제.
- 코드 그대로 옮기고, print(1)부분만 시퀀스 출력으로 바꿔줬다.

처음에 인접한 카드에서 시작해서,
bfs로 힙에 저장해서 2개씩 꺼내는 방식으로 풀이 시도했으나 계속 틀림.
- 왜틀리는지 모르게쑴
    1. 최초 두 쌍 소거 후 인접하는 모든 카드 힙에 삽입.
        - 정렬 기준은 카드 값. (오름차순)
    2. 힙에서 2개 꺼내서 소거 후 (1)반복
        2-1. 0카드가 홀수 개(1개) 남고, 1카드 차례일 때
             단순히 2개를 꺼내면 소거 짝이 맞지 않음.
             그래서 +2해서 다시 힙에 넣고, 하나 더 뽑음
                - 이러면 맨 뒤에 다시 넣는 효과
                - 다 처리 후 0, 2 이렇게 남아도
                  다시 2, 2이렇게 되어 상관없다.
    - 우쒸 정답지가 순서때문에 틀리는거아냐?
      해서 풀이 완료 한 코드에서 shuffle해서 해봤는데 잘된다.
      논리 오류가 뭐가 있지 

근데 계속 틀려서 그냥.
빈칸만 나오게 되면, 모든 위치는 소거시킬 수 있어서
그냥 차례로 출력함.
"""