'''
매번처리보다 일괄처리가 빠름
"".format() 보다 f"" 가 더 빠름
'''

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
    print(f"#{i+1} {a}")
