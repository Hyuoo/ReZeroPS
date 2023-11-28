from collections import deque
n,k = map(int,input().split())
s = [-1]*100001
q = deque([[n, 0]])
while q:
    now, t = q.popleft()
    if now < 0 or now > 100000 or s[now]!=-1 :
        continue
    if now == k:
        print(t)
        break
    s[now] = t
    t+=1
    q.append([now-1, t])
    q.append([now+1, t])
    q.append([now*2, t])
'''
숨바꼭질
풀이시간 : 22m

사실상 완전탐색

k<=n면 무조건 k-n시간
아니면 짝수라인 생각해서 가장 근접한 짝수라인으로 이동하는거 비교
생각했는데 구현이 헷갈려서 큐로 싹다 넣음.

------------------------------
풀이 후 숏코딩보고
재귀로 아래 케이스별로 나눔
n>=k:
n<k and k%2
n<k and not k%2
예외처리 n, k = 0, 1 일 때,
(X) 예외처리가 아니라 하한조건 종료문
'''
