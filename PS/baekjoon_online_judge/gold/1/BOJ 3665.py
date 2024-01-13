"""
Solving Date    : 2024.01.14
Solving Time    : 1h 10m
Title           : 최종 순위
tags            : 그래프 이론, 위상 정렬, 방향 비순환 그래프
url             : https://www.acmicpc.net/problem/3665
runtime         : 504 ms
memory          : 40924 KB
"""

import sys
input = sys.stdin.readline

for tc in range(int(input())):
    # print(f"==tc:{tc}==")
    n = int(input())
    t = [*map(int, input().split())]

    dependency = [set() for _ in range(n + 1)]
    ref_count = [0 for _ in range(n + 1)]
    while t:
        p, *t = t
        dependency[p] = set(t)
        for tmp in t:
            ref_count[tmp] += 1

    # print(dependency)
    # print(ref_count)

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        # print(a,b)
        if b in dependency[a]:
            ref_count[b] -= 1
            ref_count[a] += 1
        else:
            ref_count[b] += 1
            ref_count[a] -= 1
        dependency[a]^={b}
        dependency[b]^={a}

    # print(dependency)
    # print(ref_count)

    q = [i for i in range(1, n+1) if ref_count[i]==0]

    result = []
    while len(q)==1:
        now = q.pop()
        result.append(now)

        for nxt in dependency[now]:
            ref_count[nxt] -= 1
            if ref_count[nxt] == 0:
                q.append(nxt)

    if len(result) != n:
        print("IMPOSSIBLE")
    else:
        print(*result)

"""
온갖 뻘짓을 했는데
풀이시간 -45분(25분째)에 제출한 문제에서
"?"로 처리한 부분만 "IMPOSSIBLE"로 바꿔주니 정답이 되었다.

틀린경우를 맞게 했었으나, 맞다는걸 몰라서 못풀었으니 못푼거다.

문제가 너무 애매함.
- 결과 출력에 대해서
    분명 "올해 최종 순위"를 만드는 문젠데
    순위가 작년과 비교해서 "바뀐" 팀만 출력을 하는게 맞나...??
    해서 한참 시간쓰고 (아니었음) 
- 순위가 바뀌는 팀 2개 입력에 대해서
    맨 처음 2개 팀의 상대적인 순위가 "서로" 바뀐다고 해석했는데,
    아니 이게
    "올해 팀 6이 팀 13보다 순위가 높다면, (6, 13)을 발표할 것이다."
    라는게 6 13 순서로 발표한다는건가??? 해서
    이부분 처리하느라 한참 쓰고 (아니었음)
-- 그럼 또 "데이터 일관성"이라는게
    작년 상대적으로 1, 2등이었는데
    1 2로 바뀌었다고 입력이 들어오면
    - 바뀐 팀의 목록만 주어진다.
    - 근데 안바꼈다.
    : 잘못된 데이터.
    이거 예외 아님?? (상대순위부터 아니었음)

그래서 45분 더 풀었다.
"""