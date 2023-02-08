'''
수열
풀이시간 : 14m

m 값을 0으로 잡아놨다가 3분씀 젠장
'''
_, k = map(int,input().split())
a = [0]+list(map(int,input().split()))
m = -100*100001
for i in range(1,len(a)):
    a[i] += a[i-1]
    if i>=k and m<a[i]-a[i-k]:
        m = a[i]-a[i-k]
print(m)
