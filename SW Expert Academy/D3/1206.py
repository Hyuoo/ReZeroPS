T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    width = int(input())
    ar = list(map(int,input().split()))
    ans=0
    for i in range(2,width-2):
        h = ar[i]-max(ar[i-2:i]+ar[i+1:i+3])
        if h>0:
            ans+=h
    print(f"#{test_case}",ans)
    # ///////////////////////////////////////////////////////////////////////////////////
#아니 T 테스트케이스 수를 인풋으로 받게 해놓고
#밑에가 코드 쓰라고 해놓고 T때문에 런타임에러가 나게 만들어놔?
#어이가없네
