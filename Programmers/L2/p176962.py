#https://school.programmers.co.kr/learn/courses/30/lessons/176962

def get_t(t):
    h,m=map(int,t.split(":"))
    return h*60+m

def solution(plans):
    answer = []
    s = []
    plans=sorted(map(lambda x:[x[0],get_t(x[1]),int(x[2])],plans+[["","2000:00",0]]),key=lambda x:x[1])
    
    prev = plans[0]
    now = ["",0]
    for name, start, playtime in plans[1:]:
        #print(">>>",name,start,playtime)
        prev[2]-=(start-prev[1])
        if prev[2]>0:
            s.append([prev[0],prev[2]])
        else:
            answer.append(prev[0])
            while prev[2]<0 and s:
                #여유시간
                
                if s[-1][1]+prev[2]>0:
                    #잔업안끝남
                    s[-1][1]+=prev[2]
                    break
                    
                elif s[-1][1]+prev[2]<0:
                    #잔업끝나고도 시간남음
                    prev[2] += s[-1][1]
                    answer.append(s.pop()[0])
                    
                else:
                    #잔업끝남
                    answer.append(s.pop()[0])
                    break
                    
        prev = [name,start,playtime]
    
    return answer
'''
과제 진행하기
#KDT_코테스터디

차례대로 과제를 해결하는데
무조건 정해진시간에 정해진 과제 시작
그외엔 무조건 최근에 멈춘 과제부터 해결

1. 과제 하나씩
  1.1. 현재과제 미해결
      스택에 저장
  1.2. 현재과제 해결
      1.2.1. 여유시간이 있고, 스택에 과제있으면 과제수행
          1. 과제 미해결
            남은시간만 깎음
          2. 과제 해결 and 남은시간 0
            answer에 추가하고 과제삭제
          3. 과제 해결 and 남은시간있음
            1.2.1에서 반복

마지막과제를 여유시간 무한급으로 줘서 1.2.1에서 모두 해결되도록 함
'''
