s=0.0
d=0
for _ in range(20):
    _,b,c=input().split()
    d+=int(b[0]) if c!="P" else 0
    if c not in "FP":
        s+=float(b)*(4-(ord(c[0])-65)+(0.5 if c[1]=="+"else 0.0))
print(s/d)
