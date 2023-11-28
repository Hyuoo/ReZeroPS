n, k = map(int,input().split())
ar = [i for i in range(1,n+1)]
ans = []
k-=1
i = 0
while ar:
    i=(i+k)%len(ar)
    ans.append(ar[i])
    del ar[i]
print("<",", ".join(map(str,ans)),">",sep="")
'''
요세푸스 문제
풀이시간 : 10m
'''
