def sim(state,ff,fs,sf,ss,c):
    if ff==0 and ss==0:
        return min(fs,sf)*2+(fs>sf if state else sf>fs)
    if state:
        if fs==0:
            return c+ff
        elif fs!=0 and sf==0:
            return c+ff+1+ss
        else:
            return c+ff+ss+min(fs,sf)*2+(fs>sf)
    else:
        if sf==0:
            return c+ss
        elif fs==0 and sf!=0:
            return c+ss+ff+1
        else:
            return c+ff+ss+min(fs,sf)*2+(fs<sf)

ff,fs,sf,ss = map(int,input().split())

if (ff>0 or fs>0):
    a = sim(1, ff,fs,sf,ss, 0)
else:
    a = sim(0, ff,fs,sf,ss, 0)
print(a)

'''
락스타 락동호
풀이시간 : 1h 4m

경우를 싹다 계산해서 모든 케이스를 커버하는 문제.
'''
