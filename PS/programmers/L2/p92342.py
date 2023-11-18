#https://school.programmers.co.kr/learn/courses/30/lessons/92342

from itertools import combinations_with_replacement as c
def solution(n, info):
    apeach = sum([10-i for i in range(10) if info[i]])
    all_case = c([i for i in range(11)],n)
    m_val = 0
    shots = []
    for case in all_case:
        tmp = info[::-1]
        ryan = 0
        for shot in case:
            tmp[shot] -=1
            if tmp[shot]==-1:
                ryan += shot*(2 if info[10-shot] else 1)
        diff = ryan-apeach
        if m_val<diff:
            m_val = diff
            shots = case
    if m_val<=0:
        return [-1]
    return [shots.count(10-i) for i in range(11)]

'''
양궁대회
#KDT_코테스터디

점수뺏는 게임
- 점수있는거 뺏으면 2배 이득
- 어차피 점수 다 따고 화살남으면 0에 다 꽂는게 문제요구사항
처음 풀이는 아래 주석코드.

그리디하게 화살 당 얻는 이득 해서
쏠 위치 계산 했는데,

화살2개에 [0, 1, 1, 0, ..]
이면 0200을 쏘는게 이득인데 
1001을 고른다.
2발로 18점 1발로 10점..

근데 1발로 10점 하고 이후 선택이 7점밖에 안되는데 총 17이득으로,
이 경우만 봐도 화살 수 제약때문에 그리디가 안된다.

다른사람들이 다들 완탐으로 combi써서 풀었는데
그리디가 안되니 결국 나도 그방법으로 풀이.
'''

# def solution(n, info):
#     apeach = sum([10-i for i in range(10) if info[i]])
#     ryan = 0
#     info = list(reversed(info))
#     shot = []
    
#     N=n
#     while n>0:
#         m_val = 0
#         m_idx = 0
#         for i in range(1,11):
#             if info[i]<n:
#                 get = i
#                 if info[i]:
#                     get += i
#                 if m_val < get/(info[i]+1):
#                     m_val = get/(info[i]+1)
#                     m_idx = i

#         ryan += m_idx*(2 if info[m_idx] else 1)
#         shot.append([m_idx,info[m_idx]+1])
#         n -= info[m_idx]+1
#         info[m_idx] = 11
    
#     if apeach >= ryan:
#         return [-1]
    
#     ans = [0 for _ in range(11)]
#     for t, s in shot:
#         if t!=0:
#             ans[10-t] = s
#             N-=s
#     ans[10]=N
    
#     return ans
