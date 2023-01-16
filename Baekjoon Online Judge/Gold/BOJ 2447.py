n = int(input())
for i in range(n):
    for j in range(n):
        c = n//3
        while c>0:
            if (i//c%3 == 1 and j//c%3 == 1):
                c=-1
                break
            c//=3
        if c==-1:
            print(" ",end="")
        else:
            print("*",end="")
    print()
