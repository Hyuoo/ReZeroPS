n = input()
c = len(n)
l = 10**(c-1)
a = c*int(n)
while l:
    a-=(l-1)
    l//=10
print(a%1234567)
