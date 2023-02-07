t = int(input())
for _ in range(t):
    h,w,n = map(int,input().split())
    print("{}{:02}".format(h if n%h==0 else n%h,n//h if n%h==0 else n//h+1))
