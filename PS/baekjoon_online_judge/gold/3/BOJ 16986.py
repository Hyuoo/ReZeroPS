"""
Solving Date    : 2024.03.06
Solving Time    : 1h 29m
Title           : 인싸들의 가위바위보
tags            : 구현, 브루트포스 알고리즘, 백트래킹
url             : https://www.acmicpc.net/problem/16986
runtime         : 3028 ms
memory          : 31120 KB
"""

import sys
input = sys.stdin.readline
from itertools import permutations

i = lambda:[*map(int, input().split())]

def battle(matching, a, b):
    other = matching[2]
    if cheet_table[a-1][b-1] == 2:
        winner = matching[0]
        loser = matching[1]
    elif cheet_table[a-1][b-1] == 0:
        winner = matching[1]
        loser = matching[0]
    else:
        winner = max(matching[:2])
        loser = min(matching[:2])

    return [winner, other, loser]

def matchhhhhhh(matching, nxt_table, nxt_idx, scores):
    global n, k
    if nxt_idx[0] == n or n-nxt_idx[0] < k-scores[0]:
        return -1
    
    a = nxt_table[matching[0]][nxt_idx[matching[0]]]
    b = nxt_table[matching[1]][nxt_idx[matching[1]]]
    nxt_idx[matching[0]] += 1
    nxt_idx[matching[1]] += 1

    winner, *_ = nxt_matching = battle(matching, a, b)

    scores[winner] += 1
    if scores[winner] >= k:
        return winner

    return matchhhhhhh(nxt_matching, nxt_table, nxt_idx, scores)

n, k = i()
cheet_table = []  # [[int(i==j) for j in range(n)] for i in range(n)]

for _ in range(n):
    cheet_table.append(i())

B = i()
C = i()

for A in permutations(range(1, n+1)):
    if matchhhhhhh([0,1,2], [A, B, C], [0, 0, 0], [0,0,0]) == 0:
        print(1)
        break
else:
    print(0)


"""
가위불바위총번개악마용물공기보스펀지늑대나무사람뱀
..

거의 시뮬레이션너낌으로 푼 듯
- 족보대로 싸우면 누가 이기는지 출력하는거 구현하고
- 모든 경우 그냥 대입.

시간 1000ms이하인 다른 코드들을 봐도 이게뭐지 싶다.
난 바보당 백트래킹 어려웡

일반적으로
느린건 브루트포스,
빠른건 백트래킹인 듯 하다.

===

문제를 제대로 안봐서
"무승부가 발생할 경우 경기 진행 순서상 뒤인 사람이 이긴 것으로 간주"
를 절대적으로 ABC순서가 아니라,
이긴사람이 A자리로 올라가고, 무승부 시에 뒤에오는 사람이 이긴 것으로 치는거라 판단했다.

그래서 예제입력 8에서 다음과 같이 잘못 풀이된다.
>   지우가 낼 동작 순서 : (1, 4, 2, 5, 7, 9, 3, 6, 8)
>   최종승리 : 지우
>   지우(1) vs 경희(4) : 경희 win
>   경희(7) vs 민호(1) : 경희 win
>   경희(4) vs 지우(4) : 지우 win
>   지우(2) vs 민호(3) : 민호 win
>   민호(5) vs 경희(4) : 경희 win
>   경희(1) vs 지우(5) : 지우 win
>   지우(7) vs 민호(5) : 지우 win
>   지우(9) vs 경희(8) : 지우 win
>   지우(3) vs 민호(7) : 지우 win

옳은 풀이는 다음과 같다.
>   지우가 낼 동작 순서 : (1, 4, 2, 5, 7, 9, 3, 6, 8)
>   최종 승리 : 경희
>   지우(1) vs 경희(4) : 경희 win
>   경희(7) vs 민호(1) : 경희 win
>   경희(4) vs 지우(4) : 경희 win
>   경희(4) vs 민호(3) : 경희 win
>   경희(1) vs 지우(2) : 경희 win

.. (아니근데 왜 앞에건 다 정답이 되어가지고 헷갈리게)
"""