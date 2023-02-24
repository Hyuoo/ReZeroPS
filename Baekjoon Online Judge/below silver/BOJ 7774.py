n,m = map(int,input().split())
con=[]
con.append(sorted(map(int,input().split()),reverse=True))
con.append(sorted(map(int,input().split()),reverse=True))
f = 0
a = 1
b = 0
i = 0
j = 0
while (j if f else i)<len(con[f]):
    if not f:#a
        tmp = con[f][i:i+a]
        i += a
        b += sum(tmp)
        a -= len(tmp)
    else:#b
        tmp = con[f][j:j+b]
        j += b
        a += sum(tmp)
        b -= len(tmp)
    #print(("B:" if f else "A:"),a,b)
    f^=1
i=min(i,len(con[0]))-1
while b-con[0][i]>=0:
    b-=con[0][i]
    a+=1
    i-=1
print(a)
'''
콘센트
풀이시간 : 45m

아니 왤케 헷갈려
머리가 안돌아가서 풀이에 진전이 없었다

그냥 콘센트 있는대로 다꽂고
최종 a, b 갯수에서 b만큼 꽂았던 a콘센트를 다시 빼는식으로 품

'''
