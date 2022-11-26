'''
DP문제.
t일수만큼 다음 날로 영향을 주기 때문에 역순으로
>> i=n일부터 1일까지 >> 편의를 위해 기존 배열을 통째로 뒤집어서 받음. (range(n))
i일 일때 최선의 값은 i일을 포함할때, i일을 포함안할때 중 큰 값.
>> 설명은 뒤에서부터 한 셈 치고 구현은 뒤집어서.
i일을 포함 : {i+t[i]까지의 최선 + p[i]}
i일을 포함X : {p[i-1]}
포함/비포함 비교해가며 끝까지 하면 마지막 값이 최대 이익
(예외처리 i+t[i]날짜가 n을 넘으면 마지막 최대이익(비포함))
'''
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
