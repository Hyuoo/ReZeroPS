a=input()
o=0
for b in a:
    b=ord(b)-48
    o*=9
    o+= b-1 if b>4 else b
print(o)
