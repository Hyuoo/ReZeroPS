'''
칵테일
풀이시간 : 1h 20m

n개 재료를 쓰는 칵테일에서
n-1개의 1:1상대 비율을 알려주고
그럼 싹다 넣으면 어떻게 비율맞추면서 최소로 만들 수 있는지.


접근 :
일단 직접 해본다.
1. 약분해서 a:b=p:q비율로 만들어서, 일단 a,b확정.
2. 새로운게 들어오면, 연결된 비율이 있겠지 그럼 걔네도 싹다 바뀌겠네
3. 이 바뀌는걸 무슨 계산으로 바꾸지
4. 이 바뀌는 규칙만 찾고 연결하는거 구현만 하면 되는 간단한 문제같은데


직접해본결과 :

각 값들을 저장하는 배열 m을 만들고, 비율이 연결되는 애들을 저장하는 m_list 배열까지 총 2개를 만든다.

a,b,p,q를 입력받아서
일단 기존에 m[a], m[b]가 입력이 된게 있으면 걔네도 다 비율을 맞춰야하니
m[a], m[b], p, q 이 네가지 최소공배수를 구한다.
  -> 근데 투머치하네 m[a]는 q를 신경쓸필요가 없고 m[b]는 p를 신경쓸필요가없다.
  그림으로 그리면 직빵인데 깃헙은 고게안되네

암튼 기존의 비율을 고려한 p, q값을 계산하고,
  (m[a]에 p를 넣을건데 변하기 전값으로 연결된 재료들을 곱해야해서 p에 임시저장)
m_list에 연결된애들이 있으면 모두 곱해준다.
  ex) m[a] => p로 값이 변하는데 p//m[a]배수가 된다.

a,b,p,q 반복해서 처리해서 m값을 최대공약수로 나누어주면 끝.


아래 주석을 코드에 쓰면서 풀었었다.
# 1. 약분된 수로 입력 받기.
# 2. m[a]와 m[b]에 value가 없으면 1로 두고 (default:1)
# 2.1 p = p*m[a]*m[b]
# 2.2 q = q*m[a]*m[b]
# 3. m[a] = p, m[b] = q 저장 하기 전에,
#   p//m[a], q//m[b]를 각 m_list 연결된 모두 곱하기.
#   * visit 이용할 필요가 있나?
# 다끝나고 m_list에 연결된 비율 추가. (중간에 해도 됨.)

일단 풀어서 이후 코드정리해서 다시 제출해서 맞은 코드는 별도로 올림
    "BOJ 1033_clear.py"
'''
from collections import deque

def get_gcd(a,b):
    if b==0:
        return a
    else:
        return get_gcd(b,a%b)

n = int(input())
# m: value, m_list: 비율이연결된 어쩌고
m = [1 for i in range(n)]
m_list = [[] for i in range(n)]

for i in range(n-1):
    a,b,p,q = map(int,input().split())
    # 1. 약분된 수로 입력 받기.
    gcd = get_gcd(p,q)
    p //= gcd
    q //= gcd
    #print(m, "1:",a,b,p,q)
    # 2. m[a]와 m[b]에 value가 없으면 1로 두고 (default:1)
    # 2.1 p = p*m[a]*m[b]
    # 2.2 q = q*m[a]*m[b]
    p = p*m[a]*m[b]
    q = q*m[a]*m[b]
    #print(m, "2:",a,b,p,q)
    # 3. m[a] = p, m[b] = q 저장 하기 전에,
    #   p//m[a], q//m[b]를 각 m_list 연결된 모두 곱하기.
    #   * visit 이용할 필요가 있나?
    m_list[a].append(b)
    m_list[b].append(a)

    visit = [a,b]
    deq = deque(m_list[a])
    mul = p // m[a]
    m[a] = p
    while deq:
        now = deq.popleft()
        if now in visit:
            continue
        visit.append(now)
        m[now] *= mul
        for j in m_list[now]:
            deq.append(j)

    visit = [a,b]
    deq = deque(m_list[b])
    mul = q // m[b]
    m[b] = q
    while deq:
        now = deq.popleft()
        if now in visit:
            continue
        visit.append(now)
        m[now] *= mul
        for j in m_list[now]:
            deq.append(j)
    #print(m, "3:",a,b,p,q)
    # 다끝나고 m_list에 연결된 비율 추가.
a = m[0]
for i in m[1:]:
    a = get_gcd(a,i)
if a>1:
    for i in range(n):
        m[i]//=a
print(*m)
