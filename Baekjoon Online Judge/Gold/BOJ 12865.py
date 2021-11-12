n, k = map(int,input().split())
item = []
for i in range(n):
    w, v = map(int,input().split())
    item += [[w,v]]
dp = [[0]*(k+1)]
for i in range(n):
    dp += [dp[i][:]]
    for j in range(k+1):
        if(item[i][0] <= j and dp[i][j-item[i][0]]+item[i][1] > dp[i+1][j]):
            dp[i+1][j] = dp[i][j-item[i][0]]+item[i][1]
print(dp[n][k])
