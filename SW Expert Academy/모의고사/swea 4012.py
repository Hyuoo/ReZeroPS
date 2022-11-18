'''
4012. [모의 SW 역량테스트] 요리사

getCase함수 -> N개까지 값중 N/2개를 고르는 경우를 모두 배열로 생성
getAnswer함수 -> getCase로 구한 케이스일 경우의 맛차이 return

풀이:
1. 먼저 2차원배열에 모두 입력받는다.
2. [i][j], [j][i]를 겹친 배열로 변환. -> 오른쪽위 대각선측 영역만 사용
>> for i in range(N-1): for j in range(i+1,N): 참조[i][j]
3. getCase함수로 N개 재료를 각각 N/2개씩 가질 수 있는 경우 모두 생성
4. getCase함수 내부에서 N/2개를 가진 경우가 되면, getAnswer함수를 호출
5. getAnswer함수에서 2.대로 모두 돌며 값 가감산하여 절대값(abs)으로 return
6. 4.에서 호출한 5.를 l에 집어넣는다
>> l은 어떤 경우에서의 맛차이가 저장되는 리스트
7. 모든 케이스에서 모인 l 중 가장 최소값을 return
'''
def getCase(now, N, n):
    l=[9999999]
    if len(now)==n:
        l.append(getAnswer(now, N))
    else:
        for i in range(now[-1]+1,N):
            l.append(getCase(now+[i], N, n))
    return min(l)
def getAnswer(case, N):
    tmp=0
    for i in range(N-1):
        for j in range(i+1,N):
            if i in case and j in case:
                tmp+=arr[i][j]
            elif i not in case and j not in case:
                tmp-=arr[i][j]
    return abs(tmp)

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int,input().split())))
    for i in range(N-1):
        for j in range(i+1,N):
            arr[i][j] += arr[j][i]
    
    print(f"#{test_case}", getCase([0], N, N//2))
            
