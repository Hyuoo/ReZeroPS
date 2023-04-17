def ruination(n):
    global party
    if not party[n]:
        return []
    mo_shiteru = []
    for p in party[n]:
        mo_shiteru.append(p)
    party[n] = []
    return mo_shiteru

n,m = map(int,input().split())
shiteru = list(map(lambda x:(int(x)-1),input().split()))[1:]
party = []
people = [[] for _ in range(n)]

for i in range(m):
    some_party = list(map(lambda x:(int(x)-1),input().split()))[1:]
    party.append(some_party)
    for j in some_party:
        people[j].append(i)

while shiteru:
    new_shiteru = []
    factor = shiteru[-1]
    shiteru.pop()
    if people[factor]:
        for attend in people[factor]:
            new_shiteru = ruination(attend)
            shiteru.extend(new_shiteru)
        people[factor] = []

ans = 0
for i in party:
    if i:
        ans+=1
print(ans)

'''
거짓말
(뻥쟁이)
풀이시간 : 52m

이야기가 잘퍼지는 마을에서 뻥쟁이가 얼마나 들키지않는 뻥을칠수있을지 고민하는 문제

i번째 사람이 참석하는 파티 리스트
j번째 파티에 참석하는 사람 리스트
두개 만들어서
왔다리갔다리 하면서 파티 날리기

결국 큰 과정은 정점 n+m개의 단방향 그래프 탐색
다만 m의 결과만 세어야 하기때문에 분리시키는것이 편함
'''
