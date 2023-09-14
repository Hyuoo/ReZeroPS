import sys
input = sys.stdin.readline
from functools import cmp_to_key
def c(a,b):
    return (b[0]+a[0]*b[1])-(a[0]+b[0]*a[1])
champ = []
for i in range(int(input())):
    a, b = map(int,input().split())
    champ.append([a,b,i+1])
for ch in sorted(champ, key=cmp_to_key(c)):
    print(ch[2])
'''
레슬러
풀이시간 : 13m

뭔가 지문이 굉장히 복잡해보이는 문제지만
까놓고 보면
- 승패 결과를 두고 많이 이긴선수 앞으로 보내기

고로 승패결과에 근거해서 내림차순 정렬하면 끝
'''
