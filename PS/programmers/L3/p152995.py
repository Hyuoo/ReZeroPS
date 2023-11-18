#https://school.programmers.co.kr/learn/courses/30/lessons/152995
'''인사고과
풀이시간 : 1h 40m
사원마다 (근무태도점수,동료평가점수) 가 있는데,
다른 임의의 사원보다 두 점수 모두 낮으면 -1(인센티브없음)
아닌 사원들은 점수합 순으로 순위매겨 인센티브 차등 지급.
0인덱스의 사원이 몇번째 석차인가?

1차시. 다 비교해서 뺄놈빼고 순위세기 -> 시간초과 실패
2차시. 약간의 로직수정 -> 더실패
3차시. 비교해야하는 사원 리스트를 따로 만들어 매 비교횟수 단축. -> 22번만 실패 ㄲㅂ
4차시. 코드 전체적으로 리팩토링, 반복되는 연산 한번에 처리, -1케이스와 아닌케이스 일반화, 인센티브 탈락자 거르는 로직 개선 -> 성공 굿

통과 한 코드를 기준으로 각 부분 역할을 구분하자면.
1. 비교할 점수를 따로 정한다.
    (
        예를들어, [7,7] 이 있으면 각 6,6 이하면 모두 비교할필요가 없으니.
        [7,7]이 있는 상태에서 [1,9] 같은경우도 비교대상으로 남겨놔야함.
        마찬가지로 [9,1] 같은 경우도 비교대상.
        [9,1]이 있을 때 [9,5] 이런경우 [9,1]을 제거하고 갱신
    ) 결과적으로 [a, b] a가 큰거랑, b가 큰거, 둘 다 큰거 세개가 나온다.
2. 0번사원(완호)이 요건이 되는지 검사.
3. 전체 scores중 1.에서의 comp_scores와 비교하여 고과탈락자 걸러내기
4. 남은 인원중 총합 순위 계산.

근데 풀고나서 다른 풀이를 보니
scores.sort(key=lambda x: (-x[0], x[1]))
이 방법을 많이 썼더라.

특히 Devyan0이라는 닉네임분이 이런 코드로 짜셨는데
    def solution(scores):
        s1, s2 = scores[0]
        scores.sort(key=lambda x: (-x[0], x[1]))
        rank, bar = 1, 0
        for x, y in scores:
            if s1+s2 < x+y and bar <= y:
                rank += 1
            if s1 == x and s2 == y and bar > y:
                return -1
            bar = max(bar, y)
        return rank
이렇게 할 경우
x = [0], y = [1] 이라고 할 때
x는 계속 작아지고, y는 계속 증가한다.
x가 같을때 y값은 다 세면 되고,
x가 작아지면 최댓값y보다 작은 값들만 세면 된다.

쭉 내려오면서 완호값을 만났는데 y값이 완호값보다 크면
    => x,y 둘 다 큰 값을 만났던것이므로 -1

쩐당
'''

''' 1차시도 : 21, 24, 25 시간초과
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

'''2차시도 : 21, 22, 24, 25 시간초과
def solution(scores):
    wanho = scores[0]
    rm = []
    for i in range(len(scores)):
        flag = False
        for j in range(len(scores)):
            if i==j:
                continue
            if scores[i][0]<scores[j][0] and scores[i][1]<scores[j][1]:
                flag = True
                break
        if flag:
            rm.append(i)

    if 0 in rm:
        return -1
    
    wans = 1
    for i in range(1,len(scores)):
        if i in rm:
            continue
        if sum(scores[i])>sum(wanho):
            wans+=1
            
    return wans
'''

''' 3차시도 : 22번 테케 하나만 시간초과
def solution(scores):
    rm = []
    comp_scores = [scores[0]]
    for i in range(len(scores)):
        f_append = False
        for c_score in comp_scores:
            if scores[i][0]>=c_score[0] and scores[i][1]>=c_score[1]:
                comp_scores.remove(c_score)
                f_append = True
            elif scores[i][0]>c_score[0] or scores[i][1]>c_score[1]:
                f_append = True
        if f_append:
            comp_scores.append(scores[i])
            
    for i in range(len(scores)):
        flag = False
        for c_s in comp_scores:
            if scores[i][0]<c_s[0] and scores[i][1]<c_s[1]:
                flag = True
                break
        if flag:
            rm.append(i)

    if 0 in rm:
        return -1
    
    wans = 1
    wanho = sum(scores[0])
    for i in range(1,len(scores)):
        if i in rm:
            continue
        if wanho<sum(scores[i]):
            wans+=1
            
    return wans
'''

def solution(scores):
    comp_scores = [scores[0]]
    for s in scores:
        f_append = False
        rm = []
        for c_score in comp_scores:
            if s[0]>=c_score[0] and s[1]>=c_score[1]:
                rm.append(c_score)
                f_append = True
            elif s[0]>c_score[0] or s[1]>c_score[1]:
                f_append = True
        for r in rm:
            comp_scores.remove(r)
        if f_append:
            comp_scores.append(s)

    for c_s in comp_scores:
        if scores[0][0]<c_s[0] and scores[0][1]<c_s[1]:
            return -1
    
    rm = []
    for s in scores:
        for c_s in comp_scores:
            if s[0]<c_s[0] and s[1]<c_s[1]:
                rm.append(s)
                break
    for r in rm:
        scores.remove(r)
        
    scores = list(map(sum,scores))
    wans = 1
    for s in scores:
        if scores[0]<s:
            wans+=1
            
    return wans
