'''
length*width*height 크기의 박스를 세 변이 2^i크기인 큐브를 이용해 채우는 문제.

나는 분할해서 푸는 방법으로 접근했다.
박스크기를 2의제곱수 큰수부터 체크하여 한 변씩 빼고, 남은크기를 다시 재귀로 반복

cubes[n] : 2^n크기의 큐브 보유 갯수
solve[n] : 2^n크기의 큐브가 필요한 갯수 devide()실행 후 값 들어감.

크기가 5 8 6 이라면 4 8 4와 1 8 6, 4 0 6, 4 8 2로 나누어 재귀호출
4 8 4는 모두4배수 크기이며 4*4*4크기 큐브 2개로 커버되니 solve[2] += 2를 한다.
4 0 6은 0이 들어가서 아무것도 안함.
1 8 6은 1개짜리 큐브 1*8*6개 필요. solve[0] += 1*8*6
4 8 2는 모두 2배수로 2칸큐브가 2*4*1개 필요. solve[1] += 2*4*1
*반복할때 1이 들어가있으면 더이상 재귀없이 1개짜리 큐브로 다 채운다.
5 8 6의 solve는 [48, 8, 2, ..]

이를 가지고 보유한 큐브에서 큰것부터 비교하여 뺄수있는거 빼고,
solve가 남으면 8배수 해서 작은크기로 넘긴다. -> 0인덱스까지 반복
cubes로 뺀 갯수만큼 ans에 더해서 최종 ans.
만약 solve에서 남은칸(max(solve)>0)이 있으면 ans = -1
====================================================================
다른 풀이를 보니 단순하게 그리디하게
2제곱수 역순으로 체크하는데,
바로 전체에 보유한 큐브로 메울 수 있는 크기 계산하고,
그대로 "다음 작은단위로 메울 수 있는 칸" - "이전에 메운 칸"*8
이런식으로 풀었다.
그리고 "메운 칸 수"랑 "전체 칸 수"가 같으면 계산한 큐브 수, 아니면 -1

내가너무 이상하게 풀기도 했다.
'''
import sys
sys.setrecursionlimit(10**9)

def devide(z, x, c):
    if min(z,x,c)<1:
        return
    for i in range(20):
        if z==2**i and z==x and x==c:
            solve[i] += 1
            return
    n=0
    while(min(z,x,c)>=2**(n+1)):
        n+=1
    d = 2**n
    if z>d:
        devide(z%d,x,c)
        z-=z%d
    if x>d:
        devide(z,x%d,c)
        x-=x%d
    if c>d:
        devide(z,x,c%d)
        c-=c%d
    z//=d
    x//=d
    c//=d
    solve[n]+=z*x*c
    return

z,x,c = map(int,input().split())
n = int(input())
cubes = [0 for i in range(20)]
solve = [0 for i in range(20)]
ans = 0
for _ in range(n):
    a,b = map(int,input().split())
    cubes[a] = b

devide(z,x,c)

for i in range(19,-1,-1):
    ans+=solve[i]
    solve[i] -= cubes[i]
    if solve[i]>0:
        ans-=solve[i]
        if i>0:
            solve[i-1]+=8*solve[i]
            solve[i]=0

print(-1 if max(solve)>0 else ans)
