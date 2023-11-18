#코딩테스트 연습 > 연습문제 > 멀리 뛰기
#https://school.programmers.co.kr/learn/courses/30/lessons/12914

def ans(n,arr):
    if(arr[n]!=-1):
        return arr[n]
    if(n<3):
        return n
    else:
        arr[n] = (ans(n-1,arr)+ans(n-2,arr))%1234567
        return arr[n]
    
def solution(n):
    ar= [-1 for _ in range(2001)]
    if(n>200):
        for i in range(200,n,200):
            ans(i,ar)
    return ans(n,ar)
