import sys
input = sys.stdin.readline
for _ in range(int(input())):
    m,M = 0,0
    l,a = map(int,input().split())
    for _ in range(a):
        n = int(input())
        m = max(m,min(n,l-n))
        M = max(M,max(n,l-n))
    print(m,M)
'''
개미
풀이시간 : 14m

아니 이게 대체 뭔소리여 해서

개미가 0,l 위치에서 떨어지는지 한참있다가 알고
만나게 된다면이 이게 101에서 만나는거랑 11에서 만나는거랑같나 어케취급되는거여
했다가

근데 그런거 고려하면 실버1아닐듯 해서

이거 부딪히는거 상관없지않나?
해서 위와같은 풀이 함.

1. 각 개미별로 짧은거리들 중 가장 긴 거리가 최소시간
2. 각 개미별로 먼 거리들 중 가장 긴 거리가 최대시간
'''
