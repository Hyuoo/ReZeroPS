'''
팰린드롬 만들기
풀이시간 : 1h 53m

쉽게 접근하는걸 생각 못해서
계속 규칙성 찾는다고, 중간에서 자르고 한다고
거의 2시간동안 못풀었다.
'''
S = input()
R = "".join(reversed(S))
p = S[len(S)-len(S)//2:]
ans = 1
while(p):
    l = len(p)
    if p == R[l+1:l*2+1]:
        ans = l*2+1
        break
    if p == R[l:l*2]:
        ans = l*2
        break
    p = p[1:]
print(len(S)*2-ans)
