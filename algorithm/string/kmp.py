
# pi.
# string p의 길이 i인 서브스트링에서 가장 긴 prefix==suffix 길이 리스트로 반환.
def getpi(p:str)->list:
    m = len(p)
    j = 0
    pi = [0 for _ in range(m)]
    for i in range(1,m):
        while j>0 and p[i]!=p[j]:
            j = pi[j-1]
        if p[i] == p[j]:
            j += 1
            pi[i] = j
    return pi

# kmp.
# string s에서 pattern p 등장 위치 인덱스 리스트로 반환.
def kmp(s:str, p:str)->list:
    ans:int = []
    pi = getpi(p)
    n = len(s)
    m = len(p)
    j = 0
    for i in range(0,n):
        while j>0 and s[i]!=p[j]:
            j = pi[j-1]
        if s[i]==p[j]:
            if j==m-1:
                ans.append(i-m+1)
                j = pi[j]
            else:
                j+=1
    return ans

k=kmp(input(),input())
print(len(k))
print(*k)
