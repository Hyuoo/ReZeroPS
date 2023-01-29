'''
트리순회
풀이시간 : 38m

트리를 그냥 힙으로 27했다가 인덱스문제때문에 다시풀고
링크드로 트리를 구현하려다가 하다보니까 생각해보니까 그럴필요가 없어서
그냥 딕셔너리에 문자 넣어서 트리인 척 했다.

재귀 줄 안나누고 하나로 리턴 묶어서 해봤는데 잘된다.
'''
N = int(input())
tree = {}
for _ in range(N):
    p, l, r = input().split()
    tree[p] = [l,r]

def post(tr, p):
    if p==".":
        return ""
    return p+post(tr,tr[p][0])+post(tr,tr[p][1])

def inf(tr, p):
    if p==".":
        return ""
    return inf(tr,tr[p][0])+p+inf(tr,tr[p][1])

def pre(tr, p):
    if p==".":
        return ""
    return pre(tr,tr[p][0])+pre(tr,tr[p][1])+p

print(post(tree,"A"),inf(tree,"A"),pre(tree,"A"),sep="\n")
