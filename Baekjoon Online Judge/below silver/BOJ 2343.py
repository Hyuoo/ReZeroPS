def b_zip(size):
    global ar
    ret = 1
    v = size
    for i in ar:
        if i>size:
            return 1e9
        if v-i>=0:
            v-=i
        else:
            ret+=1
            v=size-i
    return ret

n, m = map(int, input().split())
ar = list(map(int, input().split()))
l = 1
r = sum(ar)
while l<=r:
    size = (l+r)//2
    ret = b_zip(size)
    if ret>m:
        l = size+1
    else:
        r = size-1
print(l)
