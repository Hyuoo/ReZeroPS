n, k = map(int,input().split())
dp=[0]*(k+1)
for i in range(n):
    w, v = map(int,input().split())
    for j in range(k,0,-1):
        if(w<=j and dp[j-w]+v>dp[j]):
            dp[j] = dp[j-w]+v
print(dp[-1])
