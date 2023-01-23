#https://school.programmers.co.kr/learn/courses/30/lessons/152995

'''
def solution(scores):
    wanho = scores[0]
    rm_e = []
    for i in range(len(scores)):
        flag = False
        for j in range(len(scores)):
            if i==j:
                continue
            if scores[i][0]<scores[j][0] and scores[i][1]<scores[j][1]:
                flag = True
                break
        if flag:
            rm_e.append(scores[i])
            
    for a in rm_e:
        scores.remove(a)
        
    if scores[0] != wanho:
        return -1
    
    wans = 1
    for i in range(1,len(scores)):
        if sum(scores[i])>sum(wanho):
            wans+=1
            
    return wans
'''
