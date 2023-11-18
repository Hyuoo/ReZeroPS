#LEVEL1
#코딩테스트 연습 > 위클리 챌린지 > 6주차 > 복서 정렬하기
#https://programmers.co.kr/learn/courses/30/lessons/85002

def solution(w, h):
    a=[]
    for i,n in enumerate(w):
        a+=[[i+1,0,0,0,n]]
        for j,m in enumerate(h[i]):
            if(m=='W'):
                a[i][1]+=1
                a[i][2]+=1
                if(n<w[j]):
                    a[i][3]+=1
            elif(m=='L'):
                a[i][1]+=1
        if(a[i][1]==0):
            a[i][1]=1
    a=sorted(a,key=lambda x:(-x[2]/x[1], -x[3], -x[4], x[0]))
    return [i[0] for i in a]
