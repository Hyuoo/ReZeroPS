k=int(input())
s=""
l=[]
for _ in range(6):
    a,b=input().split()
    s+=a
    l.append(int(b))
s*=2
for i in range(6):
    if len(set(s[i:i+4]))==2:
        print((l[(i+4)%6]*l[(i+5)%6]-l[(i+1)%6]*l[(i+2)%6])*k)
        break
'''
참외밭
풀이시간 : 25m

풀이 자체는 2번나온 숫자, 1번나온 숫자 나누고
반복되는 두번나온 패턴 찾고

1번나온 쌍에서
2번나온 쌍 중에서 사이숫자 곱 빼기

는 바로 떠올렸는데
뭔가 구현하는 방법에서 한참 생각했다.

한참 고민하다 슬라이딩 윈도우로 구현
'''
