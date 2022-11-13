T = int(input())
#1. 전체 요소 중 최고값 sale
#2. sale 인덱스 앞부분 전부 더해서(s), 그 갯수 n*sale 해서 이익 계산
#3. sale 이후 배열 잘라서 요소가 1개이하 남을때까지 1.부터 반복
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
