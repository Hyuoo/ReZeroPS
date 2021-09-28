#코딩테스트 연습 > 2018 KAKAO BLIND RECRUITMENT > [1차] 뉴스 클러스터링
#https://programmers.co.kr/learn/courses/30/lessons/17677

import re
def solution(str1, str2):
    rr = re.compile("[A-Z]{2}")
    str1=str1.upper()
    str2=str2.upper()
    group1=[]
    group2=[]

    #print("input_\nA : ", str1, "\nB : ", str2, sep="")
    for i in range(len(str1)-1):
        tmp = str1[i:i+2]
        if rr.match(tmp) is None:
            continue
        group1+=[tmp]
    for i in range(len(str2)-1):
        tmp = str2[i:i+2]
        if rr.match(tmp) is None:
            continue
        group2+=[tmp]
    #print(group1,"\n",group2, sep="")

    s1 = set(group1)
    s2 = set(group2)
    element = s1|s2
    a= len(s1&s2)
    b= len(element)

    if b==0:
        answer=1
    else:
        for ee in element:
            count1=0
            count2=0
            for e in group1:
                count1 += 1 if ee==e else 0
            for e in group2:
                count2 += 1 if ee==e else 0
            a+=min(max(count1,1),max(count2,1))-1
            b+=max(count1,count2,1)-1
        answer=a/b
    
    return int(answer*65536)
