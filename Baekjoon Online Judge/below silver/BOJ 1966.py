'''
풀이시간 : 27m

뭔가 규칙을 찾아서 쉽게 푸는 방법을 하고 싶었는데
뜻대로 안됐다.

Counter써서 하는 방식은 똑같은데,
높은 우선순위 갯수 만큼 순서를 미루고,
찾는 순위만 조회하려 했는데,
그럴 경우 높은 순위에서 차례로 내려 올 때 시작하는 인덱스 위치가 계속 달라져서 복잡해짐.

그냥 큐 계속해서 돌면서 처리하는 방식으로 클리어. Counter 써서 매번 모두 검사 할 필요는 없도록.
'''

from collections import Counter
tc = int(input())

for _ in range(tc):
    N, M = map(int,input().split())
    q = list(map(int,input().split()))
    priority = Counter(q)
    i = 0
    j = 1
    pri = 9
    while(True):
        while priority[pri]==0:
            pri -= 1
        if q[i%N] == pri:
            if i%N == M:
                print(j)
                break
            j += 1
            q[i%N] = 0
            priority[pri] -= 1
        i+=1
