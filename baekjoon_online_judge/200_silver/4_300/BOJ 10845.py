import sys
input = sys.stdin.readline
def pop():
    t=Q[0]
    del Q[0]
    return t
q = {"push":(lambda x:Q.append(x)), "pop":(lambda:-1 if q["empty"]() else pop()), "size":(lambda:len(Q)),\
     "empty":(lambda:0 if len(Q) else 1), "front":(lambda:-1 if q["empty"]() else Q[0]),"back":(lambda:-1 if q["empty"]() else Q[-1])}
Q = []
for _ in range(int(input())):
    s = input().split()
    if s[0]=="push":
        q[s[0]](s[1])
    else:
        print(q[s[0]]())
'''
엌ㅋㅋ람다딕셔너리
'''
