n = int(input())
char = list(map(int,input().split()))+[0]
strong = list(map(int,input().split()))
dp =  [[char[:],sum(map(lambda x:(x[0]*x[1]),zip(char,strong)))] for i in range(n)]
strong = [strong[i+1]-strong[i] for i in range(n-1)]+[0]

# print(char)
# print(strong)
# print(dp)
for _ in range(int(input())):
    newdp=[]
    for i in range(n):
        maxidx=-1
        maxv=-2000000
        for j in range(n):
            if (i==n-1 or dp[j][0][i]) and maxv<dp[j][1]+strong[i]:
                maxidx = j
                maxv = dp[j][1] + strong[i]
        newarr = dp[maxidx][0][:]
        if i!=n-1 and maxidx!=-1:
            newarr[i]-=1
            newarr[i+1]+=1
            newdp.append([newarr,dp[maxidx][1]+strong[i]])
        else:
            newdp.append([newarr, dp[maxidx][1]])
    dp = newdp
    # print(dp)
print(max([m for _,m in dp]))
'''
원숭이 키우기
풀이시간 : 1h 19m

dp문제
각 레벨별로 캐릭터가 엄청 많을 수 있다.
하루에 한 캐릭터를 렙업해서 힘이 변하는데,
*힘이 줄어들 수도 있고, 안늘어나다가 몇레벨 뒤에 폭풍성장 할 수도 있어서 그리디하게 풀 수 없다.

d일만큼. 즉 렙업을 d번 할 수(도 있고 안할수도) 있는데 다 한 뒤 총 힘 값이 최대가 되는 값을 찾는문제.
(근데 왜 원숭이지)

접근 :
먼저 힘 스탯에 대한 접근을
특정 레벨의 캐릭을 렙업시키면 변동하는 값으로 바꾸고
(ex 2레벨 힘 3, 3레벨 힘 1이면, 렙업(2) = -2)

n개 길이의 dp테이블을 만들고,
각 칸에는 [모든 캐릭터 수, 총합] 저장

- n번째 칸은 이전 케이스에서 n을 렙업(n -> n+1)할 때 가장 최선의 값
- 가능한 경우가 없으면 이전 그대로 유지.
* n레벨(최대레벨)이면 변동x == 아무것도 레벨업시키지 않은 최선

d만큼 반복하고 모든 dp에서 최소값 리턴.

'''
