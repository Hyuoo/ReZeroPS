t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    ar = [0]+list(map(int,input().split()))
    v = [0 for _ in range(n + 1)]
    sub_ans = n
    for i in range(1,n+1):
        if v[i]!=0:
            continue
        next = i
        while v[next]==0:
            v[next] = i
            next = ar[next]
            if v[next]==i:
                nnext = ar[next]
                sub_ans -= 1
                while nnext!=next:
                    nnext = ar[nnext]
                    sub_ans -= 1
                break
    ans.append(sub_ans)
print(*ans,sep="\n")

'''
메모리 47732KB -> 50804KB
시간 4160ms -> 3340ms
'''
