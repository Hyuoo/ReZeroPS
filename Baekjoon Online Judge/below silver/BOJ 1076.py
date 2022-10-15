color=["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
di = dict()
for i in range(10):
    di[color[i]]=i
print((di[input()]*10+di[input()])*10**di[input()])
