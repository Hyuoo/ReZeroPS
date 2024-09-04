"""
Solving Date    : 2024.09.04
Solving Time    : 1h 1m
Title           : 클레어와 물약
tags            : 그래프 이론, 그래프 탐색, 위상 정렬, 방향 비순환 그래프
url             : https://www.acmicpc.net/problem/20119
runtime         : 804 ms
memory          : 103084 KB
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
recipes = [list(map(int, input().split())) for _ in range(m)]
_ = int(input())
potions = [*map(int, input().split())]
targets = [_ for _ in range(m)]

g = [[] for _ in range(n+1)]
ans = []

for recipe_num, recipe in enumerate(recipes):
    needs, *meterials, mk = recipe
    for m in meterials:
        g[m].append(recipe_num)
    targets[recipe_num] = mk
    recipes[recipe_num] = needs

visit = [0 for i in range(n+1)]
for p in potions:
    visit[p] = 1

q = potions

while q:
    now = q.pop()
    ans.append(now)

    for nxt_recipe_num in g[now]:
        recipes[nxt_recipe_num] -= 1
        target = targets[nxt_recipe_num]
        if recipes[nxt_recipe_num] == 0 and not visit[target]:
            visit[target] = 1
            q.append(target)

print(len(ans))
print(" ".join(str(i) for i in range(n+1) if visit[i]))

"""
같은 포션을 만들기 위한 레시피가 둘 이상인걸 몰라서 오래 걸렸다
- [A, B] -> C
- [D, E] -> C
일 때, 그냥 C로 가는 화살표 4개로 처리되어 재료가 있어도 못만듦

그 외엔 위상정렬 방식과 동일하게 실행.

만들 수 있는 포션번호
-> 그래프[포션번호] = 레시피번호
-> 레시피[레시피번호] = 필요 재료 수


코드 개선:
1. 처음 풀이는 레시피를 "필요 재료 수"가 아니라,
set으로 모든 레시피를 저장하고 discard하여 모두 완료되면 제작되는 식으로 했다.
또한, 제작 완료되는 포션을 중복으로 방문하여 ans도 set으로 하다보니 오래 걸림
- 1688ms


2. 어차피 중복방문 해도 의미가 없고, 이미 소지한 포션을 또 만드는것도 의미가 없다.
- 중복방문해도 문제가 없어서 그렇게 진행했으나, 코드는 짧으나 시간이 오래걸림
-> visit 배열을 만들어서 재방문을 하지 않도록 함
-> 중복이 없어져 ans도 set에서 list로 변경
- 1244ms


3. 마지막 출력문만 sorted(ans)에서 str.join((for_in ans))로 변경
- 1064ms


4. (최종) [target, recipe_num]형태로 저장했던 그래프를 레시피번호만 사용하도록 변경
- unpacking하던 for문도 풀어서 씀
- 804 ms
(*근데 해보니까 언패킹 자체는 더 빠른데, 배열을 만드는게 오히려 오래걸리게 만든다.)


정말 생각없이 파이써닉하면 한없이 느려지네
"""
