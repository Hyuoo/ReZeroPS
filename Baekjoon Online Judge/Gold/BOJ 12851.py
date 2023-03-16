from collections import deque
n,k = map(int,input().split())
if n>=k:
    print(n-k,1,sep="\n")
else:
    s = [[-1,0] for _ in range(100001)]
    s[n] = [-1,1]
    q = deque()
    # 경로예외처리 for i in [n-1,n+1] if n==1 else [n-1,n+1,n*2]:
    for i in [n-1,n+1,n*2]:
        q.append([n,i,1])

    ans = 111111
    while q:
        prev, now, t = q.popleft()
        if now<0 or now>100000 or t>ans or (s[now][0]!=-1 and s[now][0]<t):
            continue
        if now==k:
            if ans==111111:
                ans = t
            s[now][1] += s[prev][1]
            continue
        if s[now][0]==-1:
            s[now][0] = t
            s[now][1] += s[prev][1]
        elif s[now][0] == t:
            s[now][1] += s[prev][1]
            continue
        t+=1
        q.append([now, now-1, t])
        q.append([now, now+1, t])
        # 경로예외처리 if now!=1:
        q.append([now, now*2, t])
    print(ans,s[k][1],sep="\n")
'''
숨바꼭질 2
풀이시간 : ?

1->2로 가는
"방법"은 [걷기], [순간이동]
"경로"는 [1->2]
뭔가 이해가 안가서 건의사항 남김

코드 주석친 내용두군데만 빼니 오답 -> 정답처리 되어 이해안됨
숨바꼭질 1,2,3,4 이렇게 4개가 있는데 모두 경로를 기준으로 설명하는 것 같아서 더 이해안되어서
건의남김.

입력:1 3

출력:
2
1
이 오답이고
출력:
2
2
가 정답
'''
