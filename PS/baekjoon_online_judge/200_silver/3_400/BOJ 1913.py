n=int(input())
f=int(input())
a=[[0 for _ in range(n)] for _ in range(n)]
d=[0,0,0,0]
m=1
i=j=n//2
for m in range(1,n**2+1):
    a[i][j]=m
    if m==f:
        f=[i+1,j+1]
    if d[0]:
        d[0]-=1
        j+=1
    elif d[1]:
        d[1]-=1
        i+=1
    elif d[2]:
        d[2]-=1
        j-=1
    elif d[3]:
        d[3]-=1
        i-=1
    else:
        t=int(m**(1/2))
        d=[t,t+1,t+1,t+1]
        i-=1

for i in a:
    print(*i)
print(*f)

'''
달팽이
풀이시간 : 31m
#KDT_코테스터디

우,하,좌,상 순서/홀수제곱칸 으로 한세트로 보고
방향별 남은 횟수 배열 만들어서 반복.

반복횟수 다쓰면: n(홀수)**2 라인에서 반복
'''
