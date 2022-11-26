dp = [1 for i in range(11)]
dp[0] = 0
dp[10] = 0

n = int(input())
for _ in range(n-1):
    ndp = [0 for i in range(11)]
    for i in range(10):
        ndp[i] = dp[i-1]+dp[i+1]
    dp = ndp
print(sum(dp)%1000000000)
