def swap(arr, a,b):
    #print("SWAP to ",a,"&",b)
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp

def qsort(arr, s, e):
    if(s>=e):
        return
    key = s
    l = s+1
    r = e
    while(l<r):
        while(l<r and arr[l]<=arr[key]):
            l+=1
        while(l<=r and arr[r]>arr[key]):
            r-=1
        if(l<r):
            swap(arr,l,r)
    #if(key!=r and arr[key]>arr[r]):
    swap(arr,key,r)
    qsort(arr,s, r-1)
    qsort(arr,r+1,e)

if __name__ == "__main__":
    import random
    arr = [int(random.random()*100) for _ in range(10000)]
    qsort(arr,0,len(arr)-1)
