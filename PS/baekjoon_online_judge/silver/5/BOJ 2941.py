str=input()
alph=["c=","c-","dz=","d-","lj","nj","s=","z="]
for st in alph:
    str=str.replace(st,"1")
print(len(str))
