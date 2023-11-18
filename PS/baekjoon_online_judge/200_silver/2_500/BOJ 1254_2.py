'''
젠장 이걸 2시간동안 못풀었다니
'''
S = input()
count = len(S)
while S:
    if S == S[::-1]:
        break
    S = S[1:]
    count+=1
print(count)
