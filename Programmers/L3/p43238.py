#코딩테스트 연습 > 이분탐색 > 입국심사
#https://programmers.co.kr/learn/courses/30/lessons/43238

#줄서는게 아니라 몇분동안 몇명을 처리할수 있는지 바꿔생각 ==> 이분탐색
def solution(n, times):
    m = 0; M = max(times)*n
    answer = M
    while(m<=M):
        time = (m+M)//2
        careIn = 0
        for t in times:
            careIn += time//t
        if(careIn >= n and time<answer):
            answer = time
        if(careIn >= n):
            M=time-1
        else:
            m=time+1
                
    return answer
