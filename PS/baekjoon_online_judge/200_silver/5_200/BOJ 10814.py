from collections import defaultdict
d = defaultdict(list)
for _ in range(int(input())):
    a,b = input().split()
    a = int(a)
    d[a].append(b)
for age in sorted(d.keys()):
    for name in d[age]:
        print(age, name)
