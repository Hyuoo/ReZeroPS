n = int(input())
ar = list(map(int, input().split()))
s = int(input())
for i in range(n-1):
    j = i
    m = i
    while j<n and j-i<=s:
        if ar[m]<ar[j]:
            m = j
        j+=1
    val = ar[m]
    for j in range(m,i,-1):
        ar[j] = ar[j-1]
    ar[i] = val
    s -= m-i
    # print(ar, i, m, s)
    if s==0:
        break
print(*ar)

'''
소트
풀이시간 : 1h 50m

생각이 복잡해서 한참 못품.


[1차 접근]
뭐야 그냥 버블정렬 하면 되는거아님?
-> swap에 코스트 달아서 버블정렬
-> 실패
: 1 2 8 9 같은 경우가 있으면 9를 먼저 가져와야하는데 8을 먼저 가져옴.
==========================
def swap(i,j):
    global ar, s
    if s:
        ar[i], ar[j] = ar[j], ar[i]
        s-=1
        return 0
    return 1
n = int(input())
ar = list(map(int, input().split()))
s = int(input())
for i in range(n-1):
    for j in range(0,n-i-1):
        if ar[j]<ar[j+1]:
            swap(j,j+1)
        if s==0:
            break
    if s==0:
        break
print(*ar)
==========================


[2차 접근]
최댓값을 찾긴 해야하는데 어디부터 찾아야되냐
대충 다시 보니 정렬이 안 된 부분부터 최대 s까지 중 최댓값을 찾아서 가져오면 되나?
이러하면 [5 4 3 10] 같은 경우,
1> 3이 마지막 정렬된 위치.
2> 3 이후부터 최댓값을 찾는
3> 3 위치까지 가져온다.
4> 가져온 길이만큼 s빼기 (최대 s만큼 범위 중 최댓값을 찾았으니 다 빼도 된다)

>> 위 로직대로 하면 [5 4 10 3] 이 되지만,
>> s는 1개만 쓰고 남았으니, 4 위치에서 위 절차 반복하면 결국 [10 5 4 3]처럼 정렬가능.

-> 실패
: 반례 6 5 8 9 / 2
맞는 답은 [8 6 5 9].
2차접근으로 풀면 [5 8 9] 중 최댓값 찾아서 가져오려함.
==========================
n = int(input())
ar = list(map(int, input().split()))
s = int(input())
while s:
    i = 0
    while i<n-1 and ar[i+1]<ar[i]:
        i += 1
        # i+1은 정렬되지 않은. [i]부터 최대 [i+s]까지 중 최댓값.
        # 최댓값을 s번만큼 옮길 수 있다.
    if i==n-1:
        break
    j = 0
    m = i
    while i+j<n-1 and j<s:
        j += 1
        if ar[i+j]>ar[m]:
            m = i+j
    # print(ar, i, m, s)
    if i!=m:
        ar = ar[:i]+[ar[m]]+ar[i:m]+ar[m+1:] # <ㅋㅋ
        s -= m-i
    else:
        break
print(*ar)
==========================

어 근데 다시보니까
<!> 결국 s값이 허용되는 범위 내에서 최댓값을 맨 앞으로 가져오는게 최선이 맞네?
그래서 다시 버블정렬같은 느낌의 알고리즘으로 본문 코드 작성.

그래서 풀이 :

정렬될 위치 0~(n-1) 순회하면서,
해당 위치에서 s범위 내의 최댓값 찾아서,
최댓값을 위 정렬될 위치까지 땡김. 끝.
땡긴 만큼 s--

중간에 s==0되면 조금이라도 빨리 끝내게.

주의사항 :
더 빨리 끝내고 싶어서 i==m 일 때(바꿀 최댓값 없음)에도 break를 넣었다가,
i~s범위가 이동해서 앞에서 없었는데 뒤에서 있는 경우 있음.
'''
