h,w=map(int,input().split())
a=[*map(int,input().split())]
water = [h for _ in range(w)]
l,r = 0,0

for i in range(w):
    if a[i]>l:
        l = a[i]
    water[i]=min(water[i],l)

for i in reversed(range(w)):
    if a[i]>r:
        r = a[i]
    water[i]=min(water[i],r)

print(sum(water[i]-a[i] for i in range(w)))

'''
빗물
풀이시간 : 18m
#KDT_코테스터디

먼저 물 다 채워놓고
왼쪽이랑 오른쪽에서 각각 블록높이로 물을 깎아내는 식으로 풀이
'''
