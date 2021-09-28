#코딩테스트 연습 > 해시 > 완주하지 못한 선수
#https://programmers.co.kr/learn/courses/30/lessons/42576

#Clear_Code
def solution(part, comp):
    ans = ''
    dd={}
    idx=0
    for a in part:
        tmp = hash(a)
        dd[tmp] = a
        idx+=tmp
    for b in comp:
        idx-=hash(b)
    ans = dd[idx]
    return ans

'''
#이거 맞으면 해시충돌이 원인이었다
#SIZE줄이면 통과못함
HT_SIZE = 900000
#def hf(str):
#    idx = 1
#    for a in str:
#        idx+=ord(a)
#    return idx
def solution(part, comp):
    ans = ''
    ht=[0 for _ in range(HT_SIZE)]
    for i in comp:
        ht[hash(i)%HT_SIZE]-=1
    for i in part:
        idx=hash(i)%HT_SIZE
        ht[idx]+=1
        if ht[idx]>0:
            ans=i
    return ans
'''
