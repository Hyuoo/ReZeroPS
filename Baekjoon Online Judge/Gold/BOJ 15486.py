n = int(input())
t = [0 for _ in range(n)]
p = [0 for _ in range(n)]
for i in range(n):
    t[n-i-1], p[n-i-1] = map(int,input().split())
dp = [0 for _ in range(n)]
for i in range(n):
    if i-t[i]+1<0:
        if i>0:
            dp[i]=dp[i-1]
        continue
    dp[i] = dp[i-1] if dp[i-1]>dp[i-t[i]]+p[i] else dp[i-t[i]]+p[i]
print(dp[-1])
