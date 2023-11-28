n = int(input())
for i in range(-n+1,n):
    for j in range(n-abs(i)-1):
        print(" ",end="")
    for j in range(abs(i)*2+1):
        print("*",end="")
    print()
