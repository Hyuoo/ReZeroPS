"""
Solving Date    : 2024.01.15
Solving Time    : 30m
Title           : 가운데를 말해요
tags            : 자료 구조, 우선순위 큐
url             : https://www.acmicpc.net/problem/1655
runtime         : 188 ms
memory          : 37132 KB
"""

import sys
input = sys.stdin.readline
import heapq

lower = []
upper = []
for i in range(int(input())):
    n = int(input())
    if i%2:
        if -lower[0] > n:
            heapq.heappush(upper, -heapq.heappop(lower))
            heapq.heappush(lower, -n)
        else:
            heapq.heappush(upper, n)
    else:
        if upper and upper[0] < n:
            heapq.heappush(lower, -heapq.heappop(upper))
            heapq.heappush(upper, n)
        else:
            heapq.heappush(lower, -n)
    print(-lower[0])

"""
중간값은 말 그대로 중간에서 움직이고,
바깥쪽 숫자값은 필요가 없으니 힙으로 구현하면 되겠다 싶어 구현했다.

처음엔 lower, mid, upper 세 구간으로 나눠서 할까 생각했는데
mid가 1개였다가 2개였다가 구분해서 구현하는게 복잡하다고 생각해서
lower, upper 두개만 두고,
두 길이가 같거나, lower가 1개 더 많게 만들었다.
- 이렇게 하면 무조건 lower에서 최대값이 중간값이 된다.
    (중간값이 2개면 더 작은 값)

### 풀이 과정 및 구현 최적화 ###
- 처음 풀이: 244ms
1. 일단 lower에 삽입
    - heappush()
2. lower 길이가 1개보다 더 많으면 upper로 옮기기
    - heappop(), heappush()
3. lower최대값이 uppwer최소값보다 크면 교환
    - heappop()*2, heappush()*2 

- 2번째 풀이: 212ms
위의 1, 2과정에서 불필요하게 힙 연산이 반복되어 변경
1. lower, upper 순서대로 번갈아서 삽입
    - heappush()
2. lower최대값이 uppwer최소값보다 크면 교환
    - heappop()*2, heappush()*2

- 3번째 풀이: 188ms
0-1. lower에 삽입 할 차례
    1-1. upper 최소값이 삽입값 n보다 작으면 upper를 lower로 옮기고 upper에 삽입
         (lower에 넣어도 둘이 바꿔줘야할 경우)
        - heappop(), heappush()*2
    1-2. lower에 그냥 삽입
        - heappush()
0-2. upper에 삽입 할 차례
    2-1, 2-2. 위 케이스와 똑같이..
이렇게 해서 한바퀴에 최대 힙연산이 3번만 사용된다.


-- 추가로
결과를 일괄출력하면 시간이 줄긴하는데, 왠지 메모리가 더 아까움.
ms: 188 -> 176
KB: 37132 -> 43340
"""