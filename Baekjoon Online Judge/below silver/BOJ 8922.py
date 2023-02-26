def dseq(n, a):
    tmp = [0 for _ in range(n)]
    for i in range(n):
        tmp[i] = abs(a[i]-a[i+1])
    tmp.append(tmp[0])
    return tmp

for _ in range(int(input())):
    n=int(input())
    mm=[[] for _ in range(15001)]
    a=list(map(int,input().split()))
    a.append(a[0])
    lp = 1
    for _ in range(1000):
        a = dseq(n,a)
        s = sum(a)
        if s==0:
            lp=0
            break
        else:
            aa = "".join(map(str, a))
            for t in mm[s]:
                if aa in t:
                    # lp=1
                    break
            mm[s].append(aa*2)
    print("LOOP" if lp else "ZERO")

'''
두찌 수열
풀이시간 : 29m

'''
