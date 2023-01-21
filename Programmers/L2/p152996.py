#https://school.programmers.co.kr/learn/courses/30/lessons/152996

'''
def solution(weights):
    bal = [[w*2,w*3,w*4] for w in sorted(weights)]
    a = 0
    for i in range(len(bal)-1):
        for j in range(i+1,len(bal)):
            if bal[i][2]<bal[j][0]:
                break
            if len(set(bal[i]).union(bal[j])) != 6:
                a += 1
    return a
'''
