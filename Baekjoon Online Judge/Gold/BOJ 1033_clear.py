from collections import deque

def get_gcd(a,b):
    if b==0:
        return a
    else:
        return get_gcd(b,a%b)

def update_all(m, visit, deq, mul):
    while deq:
        now = deq.popleft()
        if now in visit:
            continue
        visit.append(now)
        m[now] *= mul
        for j in m_list[now]:
            deq.append(j)

n = int(input())
m = [1 for _ in range(n)]
m_list = [[] for _ in range(n)]

for i in range(n-1):
    a,b,p,q = map(int,input().split())
    gcd = get_gcd(p,q)
    p = p*m[a]*m[b]
    q = q*m[a]*m[b]
    m_list[a].append(b)
    m_list[b].append(a)
    update_all(m, [a,b], deque(m_list[a]), p//m[a])
    update_all(m, [a,b], deque(m_list[b]), q//m[b])
    m[a] = p
    m[b] = q

a = m[0]
for i in m[1:]:
    a = get_gcd(a,i)
m = map(lambda x:x//a, m)

print(*m)
