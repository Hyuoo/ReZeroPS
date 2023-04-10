#리스트 내 재정렬
def merge_sort(arr:list, left:int, right:int)->None:
    if right-left<2:
        return
    l = len(arr)
    mid = (left+right)//2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid, right)
    new = []
    i = left
    j = mid
    while i<mid and j<right:
        if arr[i]<arr[j]:
            new.append(arr[i])
            i+=1
        else:
            new.append(arr[j])
            j+=1
    while i<mid:
        new.append(arr[i])
        i+=1
    while j<right:
        new.append(arr[j])
        j+=1
    for i in range(left,right):
        arr[i] = new[i-left]


import random
a = [random.randint(1,30000) for _ in range(10000)]
b = a[:]
a.sort()
merge_sort(b,0,len(b))
print(a==b)
