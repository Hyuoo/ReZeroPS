a, b, n = map(int,input().split())
aq = [-a]
bq = [-b]
present = 1
for _ in range(n):
    t, c, m = input().split()
    t = int(t)
    m = int(m)
    present += m
    if c == "B":
        start = max(aq[-1]+a, t)
        for i in range(m):
            aq.append(start)
            start += a
    else:
        start = max(bq[-1]+b, t)
        for i in range(m):
            bq.append(start)
            start += b
# print(aq,bq)

i = j = 1
A = []
B = []
present = iter(range(1, present))
while i < len(aq) and j < len(bq):
    if aq[i] <= bq[j]:
        A.append(next(present))
        i += 1
    else:
        B.append(next(present))
        j += 1

while i < len(aq):
    A.append(next(present))
    i += 1
while j < len(bq):
    B.append(next(present))
    j += 1

print(len(A))
print(*A)
print(len(B))
print(*B)

'''
세훈이의 선물가게
풀이시간 : 29m
#KDT_코테스터디

2명이 각자 작업속도에 맞춰서
큐에 들어온 작업순서로 처리.
전체 처리 순서 맞추는 문제.

풀이:
- 일단 각자 실제 작업이 일어나는 시간으로 큐를 생성 (aq, bq)
- 각 큐 시간 순서대로 1부터 차례대로 처리한 번호 삽입
'''
