#코딩테스트 연습 > 연습문제 > 하노이의 탑
#https://programmers.co.kr/learn/courses/30/lessons/12946
#이거 왜 3레벨이나 되는거지
def hanoiSolve(n, a, b, c,answer):
    if(n!=0):
        hanoiSolve(n-1,a,c,b,answer)
        answer+=[[a,c]]
        hanoiSolve(n-1,b,a,c,answer)
    
def solution(n):
    answer = []
    hanoiSolve(n,1,2,3,answer)
    return answer
