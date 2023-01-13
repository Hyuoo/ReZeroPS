

T = int(input())
S="abcdefghijklmnopqrstuvwxyz"
ans = []
for tc in range(T):
    st = input()
    c=0
    for i in range(len(st)):
        if S[i]==st[i]:
            c+=1
        else:
            break
    ans.append(c)
for i,a in enumerate(ans):
    print("#{} {}".format(i+1, a))
