INF = 999999
n = int(input())
cost = []
for i in range(n):
    cost.append(list(map(int,input().split())))
work = list(map(lambda x:(1 if x=="Y" else 0), list(input())))
repair = int(input())-sum(work)

if repair<1:
    print(0)
elif sum(work)==0:
    print(-1)
else:
    state = [([] if work[i] else [[(work[j]) for j in range(n)],0]) for i in range(n)]
    # print(state)
    for _ in range(repair):
        tmp_state = []
        for j in range(n):
            if not state[j]:
                tmp_state.append([])
                continue
            minv = INF
            mins = []
            for k in range(n):
                if not state[k] or state[k][0][j]==1:
                    continue
                for i in range(n):
                    if state[k][0][i]==1 and state[k][1]+cost[i][j]<minv:
                        minv = state[k][1]+cost[i][j]
                        mins = state[k][0][:]
                        mins[j] = 1
            if minv == INF:
                tmp_state.append([])
            else:
                tmp_state.append([mins,minv])
        state = tmp_state
        # print(state)
    print(min([(i[1] if i else INF) for i in state]))
'''
발전소
풀이시간 : 일단 4h정도?

예외처리 앞에서 해주고
repair 갯수만큼 고치는거 반복.
각 시퀀스마다 n개째, j번 발전소를 고치는 [고친발전소, 최소비용] 갱신

state 찍어보면 이해가능..

일단 몇가지 문제들은 다 고쳤으나
계속해서 1%에서 틀렸습니다 등장


7
1 3 0 9 3 2 8
13 28 2 3 8 9 30
9 2 14 19 15 10 23
9 2 8 15 19 23 28
15 19 28 0 13 19 15
9 15 32 19 32 0 14
2 3 19 15 23 15 28
YYYYYYN
7
ANS: 8

16
0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
2 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
1 2 0 1 1 1 1 1 1 1 1 1 1 1 1 1 
1 2 1 0 1 1 1 1 1 1 1 1 1 1 1 1  
1 2 1 1 0 1 1 1 1 1 1 1 1 1 1 1 
1 2 1 1 2 0 1 1 1 1 1 1 1 1 1 1 
1 2 1 1 2 2 0 1 1 1 1 1 1 1 1 1 
1 2 1 1 2 2 1 0 1 1 1 1 1 1 1 1 
1 2 1 1 2 2 1 3 0 1 1 1 1 1 1 1 
1 2 1 1 2 2 1 3 1 0 1 1 1 1 1 1 
1 2 1 1 2 2 1 3 1 1 0 1 1 1 1 1 
1 2 1 1 2 2 1 3 1 1 4 0 1 1 1 1 
1 2 1 1 2 2 1 3 1 1 4 1 0 1 1 1 
1 2 1 1 2 2 1 3 1 1 4 1 1 0 1 1 
1 2 1 1 2 2 1 3 1 1 4 1 1 5 0 1 
1 2 1 1 2 2 1 3 1 1 4 1 1 5 3 0 
YNNNNNNNNNNNNNNN
16
ANS: 15

2
0 1
1 0
NN
2
ANS: -1
'''
