def swap(arr, a, b):
    #print("SWAP to ", a, "&", b)
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp

def qsort(arr, start, end):
    if(start >= end):
        return
    key = start
    left = start+1
    right = end
    while(left<right):
        while(left<right and arr[left]<=arr[key]):
            left+=1
        while(left<=right and arr[right]>arr[key]):
            right-=1
        if(left<right):
            swap(arr, left, right)
    #if(key!=right and arr[key]>arr[r]):
    swap(arr, key, r)
    qsort(arr, start, r-1)
    qsort(arr, r+1, end)

if __name__ == "__main__":
    import random
    arr = [int(random.random()*100) for _ in range(10000)]
    qsort(arr, 0, len(arr)-1)
