import sys
input = sys.stdin.readline

def check(sign):
    state = 0
    '''
    state:
    0 : init
    1 : "0"
    2 : "1"
    3 : "10"
    4 : "100+"
    5 : "100+1"
    6 : "100+1+"
    7 : "100+1+0"
    '''
    transition = [[1,2],[-1,0],[3,-1],[4,-1],[4,5],[1,6],[7,6],[4,0]]
    for s in sign:
        state = transition[state][ord(s)-48]
        if state==-1:
            return -1
    if state in (0,5,6):
        return 0
    else:
        return -1

for _ in range(int(input())):
    sign = input().rstrip()
    print("YES" if check(sign)!=-1 else "NO")
'''
Contact
풀이시간 : 39m

이걸 상태머신 배운게 이렇게 쉽게 쓰이네

그냥 모든 문자열 상태도 만들어서 0,1 입력 당 상태천이 끝.
'''
