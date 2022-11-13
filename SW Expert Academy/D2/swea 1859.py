T = int(input())
for test_case in range(1, T + 1):
    _ = input()
    ar = list(map(int,input().split()))
    a=0
    while(len(ar)>1):
        s = 0
        sale = max(ar)
        for i in range(ar.index(sale)):
            s += ar[i]
        a += sale*ar.index(sale) - s
        ar = ar[ar.index(max(ar)):]
        del ar[0]
    print(f"#{test_case}",a)
