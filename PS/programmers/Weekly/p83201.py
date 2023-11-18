#LEVEL1
#코딩테스트 연습 > 위클리 챌린지 > 2주차 > 상호 평가
#https://programmers.co.kr/learn/courses/30/lessons/83201

def solution(scores):
    answer = ''
    size = len(scores)
    self_score = [0]*size
    score = [[] for _ in range(size)]
    
    for i in range(size):
        for j in range(size):
            score[i]+=[scores[j][i]]
        self_score[i] = score[i][i]
    
    for i in range(size):
        i_sum = sum(score[i])
        i_len = len(score[i])
        if self_score[i] == max(score[i]) or self_score[i] == min(score[i]):
            count=0
            for j in range(size):
                if score[i][j]==self_score[i]:
                    count+=1
            if count==1:
                i_sum-=self_score[i]
                i_len-=1
        answer+="FFFFFDDCBAA"[int(i_sum/i_len//10)]
    
    return answer
