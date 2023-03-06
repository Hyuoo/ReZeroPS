import sys
input = sys.stdin.readline
a = []
r = 0
ans = 0
n = int(input())
for _ in range(n):
    b,c = map(int,input().split())
    a.append([b,c])
a.sort(key=lambda x:(x[1],x[0]))
for s,e in a:
    if r<=s:
        r=e
        ans+=1
print(ans)

'''
회의실 배정

그냥 평범한 그리디문제.

but,
"한 개의 회의실"
다른 강의실배정문제 풀다와서 문제도 제대로 안보고
한참 예제출력이 왜 4로나오는지 이해못함
'''
