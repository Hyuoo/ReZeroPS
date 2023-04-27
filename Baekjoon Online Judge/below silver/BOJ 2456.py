tot = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for _ in range(int(input())):
    s = list(map(int,input().split()))
    for i in range(3):
        tot[i][0] += s[i]
        tot[i][s[i]] += 1
for i in range(3):
    tot[i][1] = i+1
tot.sort(key=lambda x:(-x[0],-x[3],-x[2]))
a=tot[0]
b=tot[1]
if a[0]==b[0] and a[2]==b[2] and a[3]==b[3]:
    a[1] = 0
print(a[1],a[0])

'''
나는 학급회장이다

t=[[0]*4 for _ in range(3)]
for _ in range(int(input())):
    s=list(map(int,input().split()))
    for i in range(3):
        t[i][0]-=s[i]
        t[i][s[i]]-=1
for i in range(3):t[i][1]=i+1
t.sort(key=lambda x:(x[0],x[3],x[2]))
a,s,d,f=t[0]
z,_,c,v=t[1]
if not(a-z or d-c or f-v):s=0
print(s,-a)

356B -> 300B
숏코딩 생각 없었지만
공백없애고 변수줄이기만하면 첫페이지인걸 어케참음;
'''
