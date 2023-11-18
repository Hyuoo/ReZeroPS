ff,fs,sf,ss = map(int,input().split())
state = (ff>0 or fs>0)
if state and fs==0:
    a = ff
elif not state and sf==0:
    a = ss
else:
    a = ff + ss + min(fs,sf)*2 + (fs>sf if state else sf>fs)
print(a)
