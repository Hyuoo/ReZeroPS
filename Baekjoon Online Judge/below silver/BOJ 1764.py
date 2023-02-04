'''
듣보잡
풀이시간 : 4m
'''
n,m = map(int,input().split())
s = set()
for _ in range(n):
    s.add(input())
a = []
for _ in range(m):
    b = input()
    if b in s:
        a.append(b)
print(len(a))
print(*sorted(a),sep="\n")
