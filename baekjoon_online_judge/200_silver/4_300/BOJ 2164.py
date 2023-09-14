ar = list(range(1, int(input())+1))
f = 1
while len(ar)>1:
    l = len(ar)
    ar = [n for i,n in enumerate(ar) if i%2==f]
    f ^= l%2
print(ar[0])
