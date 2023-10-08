"""
Solving Date    : 2023.10.08
Solving Time    : 45m
Title           : 뉴스 전하기
tags            : 다이나믹 프로그래밍, 그리디 알고리즘, 정렬, 트리, 트리에서의 다이나믹 프로그래밍
url             : https://www.acmicpc.net/problem/1135
runtime         : 40 ms
memory          : 31256 KB
"""

foo = lambda idx:max([i+n+1 for i, n in enumerate(sorted([foo(nxt) for nxt in tree[idx]], reverse=True))]) if tree[idx] else 0

n = int(input())
boss = list(map(int, input().split()))
tree = [[] for _ in range(n)]

for i in range(1, n):
    tree[boss[i]].append(i)

print(foo(0))

"""
코드 재밌는거보소

아래는 원래 작성한 함수
def foo(idx):
    if tree[idx]:
        tmp = sorted([foo(nxt) for nxt in tree[idx]], reverse=True)
        tt = [i+n+1 for i, n in enumerate(tmp)]
        # print(idx,":",tt, max(tt))
        return max(tt)
    else:
        return 0

일단 처음에 이게 왜 골드2나 되지 했는데
풀고나서도 왜 골드2나 되지 함.
지금 기준으로 정답비율이 46.82%로 높긴 하네

접근:
트리구조로 이루어진 조직에서
루트노드에서
한번에 한 자식 씩 방문
방문한 자식은 곧바로 자식자식 방문시작
모든 자식 방문완료 되는 시간

예제입력 3을 보기 전까지
그냥 부모-모든자식 이렇게 방문하는 줄 알았다
근데 자식이 4면 각각 1, 2, 3, 4로 시간이 듦

풀이:
먼저 상위 노드 인덱스를 가리키고 있던 배열을
하위노드를 리스트를 가리키는 배열배열로 바꿔줌

dfs로 각 노드 접근해서,
모든 하위노드들 걸리는 시간 모아서
내림차순으로 정렬 후
각 인덱스로 더해줘서 제일 큰 값으로 갱신

코드만큼 간단한 풀이법

---
어 근데 숏코딩 10등이네 더 줄여야징 => 5등
"""