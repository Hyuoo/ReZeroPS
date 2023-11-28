n, k = map(int,input().split())
a = [1 for _ in range(n+1)]
for i in range(k-1):
    for j in range(1,n+1):
        a[j]+=a[j-1]
print(a[-1]%1000000000)
'''
합분해
풀이시간 : 35m

이거 어케푸는거임
def s(n,k,a):
    if len(a)>k:
        return 0
    if len(a)==k and sum(a)==n:
        #print(a)
        return 1
    c=0
    for i in range(n+1):
        c+=s(n,k,a+[i])
    return c
def S(n,k):
    c=0
    for i in range(n+1):
        c+=s(n,k,[i])
    return c
이걸로 싹 출력해보고 그냥 보니까 규칙 보여서 규칙대로 끼워맞춰서 풀었음

풀고나서 규칙을 이해

S(n, k-1)은 0이 하나 더 붙는 경우
S(n-1, k)는 +1을 해준 경우인데
각 경우가 겹치고 중복되는걸 어케 해줘야되나 생각했는데
k 자리 일 때 특정 자리에만 각각 0을 넣고 +1을 하면
0인 경우와 0이 아닌 경우로 안겹쳐서
S(n,k) = S(n-1,k) + S(n,k-1) 하면 된다.
'''
