#https://school.programmers.co.kr/learn/courses/30/lessons/42583

def solution(bridge, w, tr):
    time = [bridge]*len(tr)
    i = j = count = 0
    while j<len(tr):
        skip = time[i] if tr[j]>w else 1
        for mov in range(i,j):
            time[mov] -= skip
        while time[i]<=0:
            w+=tr[i]
            i+=1
        if tr[j]<=w:
            w-=tr[j]
            j+=1
        count+=skip
    return count+bridge

# 구 풀이
# def solution(bridge, w, tr):
#     time = [bridge] * len(tr)
#     i=j=count=0
#     while j<len(tr):
#         skip_time = 1
#         if i<j:
#             if tr[j]>w:
#                 skip_time = time[i]
#             for k in range(i,j):
#                 time[k] -= skip_time
#         if time[i]==0:
#             w+=tr[i]
#             i+=1
#         if tr[j]<=w:
#             w-=tr[j]
#             j+=1
#         count += skip_time
#     return count+bridge

'''
다리를 지나는 트럭
풀이시간 : 30분쯤?

포인터 두개 써서 각각
- 다리에서 다음에 나올 차 : i
- 대기중인 다음에 들어올 차 : j
가리키고
시간은 다리 길이로 초기화해서 0이 되면 지나간것으로 간주
무게는 그대로 써서 +-해서 계산

while j가 남아 있으면:
  1. 다리에 있는 모든 차 시간 감소
    j 가 들어올 수 없으면
    i 시간만큼 시간스킵
  2. i가 나왔으면
    잔여무게 증가, i++
  3. j가 들어갈 수 있으면
    잔여무게 감소, j++
j가 더 없으므로
경과시간 + 다리길이가 정답
** 다리에있는 가장 마지막 차(=마지막에 들어가는 차)가 나가는 시간인데
  어차피 다리 길이만큼 진행하므로 다리길이 더하면 정답
====================================
최신풀이에서
나오는 차를 while로 다 빼니까 무조건 다리에는 차가 있음.
    ==> if i<j가 불필요해짐
    
    ..어 근데 이제보니까 예전 코드에 오류있는데?
        - 이 코드도 무조건 i<j이긴 해서 발생안하는 오류긴한데,,
        - i<j일때만 skip_time이 되는데,
        - skip_time이 없는 경우에도 count는 skip_time만큼 더해줌.
'''
