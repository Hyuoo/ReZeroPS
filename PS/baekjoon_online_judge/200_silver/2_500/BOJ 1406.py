import sys
input = sys.stdin.readline
s = list(input().rstrip())
ss = []
for _ in range(int(input())):
    i = input().split()
    if i[0]=="L":
        if s:
            ss.append(s.pop())
    elif i[0]=="D":
        if ss:
            s.append(ss.pop())
    elif i[0]=="B":
        if s:
            s.pop()
    elif i[0]=="P":
        s.append(i[1])
print(*s,*reversed(ss),sep="")
'''
에디터
풀이시간 : 45m

그냥 파이썬 리스트로 단순구현 -> 시간초과

스택으로 변형하고 시간초과나서
아맞다 입력 핵많지 readline으로 교체

하고 틀렸습니다 떠서
거의 20분동안 아니 대체 뭐가틀린거지 으어어 하다가
다른사람 코드보고 rstrip붙어있는걸 보고

아맞다 readline은 \n도 포함시키지 참 하고 생각남
그래서 for문 안에있는 애는 싹 split으로 처리한건데 바본듯
'''
