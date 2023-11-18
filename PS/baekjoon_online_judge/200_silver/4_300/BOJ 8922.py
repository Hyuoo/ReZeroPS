def dseq(n, a):
    tmp = [0 for _ in range(n)]
    for i in range(n):
        tmp[i] = abs(a[i]-a[i+1])
    return tmp+[tmp[0]]

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.append(a[0])
    lp = 1
    for _ in range(1000):
        a = dseq(n,a)
        if sum(a)==0:
            lp=0
            break
    print("LOOP" if lp else "ZERO")

'''
두찌 수열
풀이시간 : 29m

else:
    aa = "".join(map(str, a))
    for t in mm[s]:
        if aa in t:
            # lp=1
            break
    mm[s].append(aa*2)
괜히 이 코드로 조기퇴근 한다고 더 오래걸림

이거 없앤 위 코드로
33300KB -> 31256KB
660ms -> 220ms
'''
