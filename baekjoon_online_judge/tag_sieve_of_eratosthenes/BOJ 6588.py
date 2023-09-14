import sys
input = sys.stdin.readline

p = [1 for _ in range(1000001)]
for i in range(2,1002):
    if p[i]:
        for j in range(i*2, len(p), i):
            p[j]=0
idx = -1
pl = []
for i in range(3,1000001):
    if p[i]:
        pl.append(i)
        idx+=1
    p[i] = idx

ans = []
while 1:
    n = int(input())
    if not n:
        break
    i = 0
    j = p[n]
    while i<=j:
        if pl[i]+pl[j]>n:
            j-=1
        elif pl[i]+pl[j]<n:
            i+=1
        else:
            ans.append([n,pl[i],pl[j]])
            break
    else:
        print("Goldbach's conjecture is wrong.")
for a,b,c in ans:
    print("%d = %d + %d" % (a,b,c))

'''
골드바흐의 추측

똑같은 이름 문제 있어서 뭔가했네

시간문제 고친부분
1. readline
2. 매 반복 출력 -> 일괄출력

근데 다른 풀이를 보니
좀 억지로 시간에 맞춘느낌.

일단 위에 for문 2번 반복 할 필요 없고
  -> 소수여부 + 소수배열 바로 만들기
아래 쌍을 찾는 부분도 더 간결한 방법이 있다.
  -> 양방향에서 찾을 필요없이,
      단방향으로 하는데 n-pl[i]와 같은 방법으로 보는게 더 빠륾
'''
