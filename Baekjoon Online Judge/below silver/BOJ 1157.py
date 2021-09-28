str=input().upper()
ar=[0]*26
for c in str:
    ar[ord(c)-ord('A')]+=1
m = max(ar)
idx=-1
for i in range(len(ar)):
    if ar[i]==m:
        if idx!=-1:
            idx=-2
            break
        idx=i
print(chr(ord('A')+idx))
