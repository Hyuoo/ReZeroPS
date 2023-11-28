import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)#아니 왜 내거만 재귀깊이 걸리냐고
def getpa(papa, n):
	if(papa[n]==n): return n
	papa[n] = getpa(papa,papa[n])
	return papa[n]
N,M = map(int,input().split())
papa = list(range(N))
ans = 0
for i in range(M):
	src,dest=input().split()
	src = int(src)
	dest = int(dest)
	if(getpa(papa,src)==getpa(papa,dest)):
		ans=i+1
		break
	papa[getpa(papa,dest)] = papa[src]
print(ans)
