'''
Africa _ 특수문제
각 입력이 주어지고 전체 비자발급 비용을 출력하는 문제.

namibia가 nambia인줄 알았다
'''
a = "botswana, ethiopia, kenya, namibia, south-africa, tanzania, zambia, zimbabwe".split(", ")
f = [0, 50, 50, 140, 0, 50, 50, 30]
d = {i:v for i,v in zip(a,f)}
n = int(input())
s = 0
f_sa = 0
f_zz = 0
for _ in range(n):
    t = input()
    s+=d[t]
    if f_zz and (t=="zambia" or t=="zimbabwe"):
        s-=30
    if f_sa and t=="namibia":
        s-=100
    if t=="south-africa":
        f_sa = 1
    if t=="zambia" or t=="zimbabwe":
        f_zz = 1
    else:
        f_zz = 0
print(s)
