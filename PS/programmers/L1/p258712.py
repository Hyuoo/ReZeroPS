"""
Solving Date    : 2024.01.23
Solving Time    : 16m
Title           : 가장 많이 받은 선물
tags            : string, hash, implement
url             : https://school.programmers.co.kr/learn/courses/30/lessons/258712
runtime         : -
memory          : -
"""

give_id = lambda a,b:hash(a)*10+hash(b)

def solution(friends, gifts):
    n = len(friends)
    gift_score = {name:0 for name in friends}
    gifts = list(map(str.split, gifts))
    atob = {}
    next_gift_count = {name:0 for name in friends}
    
    for a, b in gifts:
        t = give_id(a, b)
        atob[t] = atob.get(t, 0)+1
        gift_score[a] += 1
        gift_score[b] -= 1
    
    for i in range(n-1):
        for j in range(i+1, n):
            a, b = friends[i], friends[j]
            a_give = atob.get(give_id(a, b), 0)
            b_give = atob.get(give_id(b, a), 0)
            if a_give == b_give:
                if gift_score[a] > gift_score[b]:
                    next_gift_count[a] += 1
                elif gift_score[a] < gift_score[b]:
                    next_gift_count[b] += 1
            else:
                if a_give > b_give:
                    next_gift_count[a] += 1
                else:
                    next_gift_count[b] += 1
    
    return max(next_gift_count.values())

"""
2024 KAKAO WINTER INTERNSHIP

역시 카카오문제는 문제읽는데 오래걸린다.

- 모든 프렌즈의 모든 관계에 대해서
- (서로 주고받은 선물 수)와 (선물지수)를 사용해서
- 다음 달 가장 많이 받는 프렌즈의 (선물 수)를 구하는 문제

1. 입력으로 ["누가" "누구한테"] 줬는지 문자열 리스트가 주어진다.
- a -> b 선물 카운트
- "누가"의 선물지수 +1
- "누구한테"의 선물지수 -1

2. 이후 모든 관계에 대해서 (다음달 받을 선물)을 계산한다.
- 서로 (준 선물의 수)의 개수가 같으면(0포함;없는경우)
    - 선물지수를 비교해서 차이가 있을 경우
        - (선물지수) 높은 쪽 +1
- 다르면
    - (준 선물의 수)가 높은 쪽 +1

3. 젤 많이 받는 수 리턴
"""