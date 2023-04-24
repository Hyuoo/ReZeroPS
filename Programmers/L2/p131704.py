#https://school.programmers.co.kr/learn/courses/30/lessons/131704

def solution(order):
    s = []
    i = 1
    count = 0
    for o in order:
        if i<o:
            s.extend(list(range(i,o)))
            i=o
        if i==o:
            i+=1
        elif i>o and s and s[-1]==o:
            s.pop()
        else:
            break
        count+=1
    return count
'''
택배상자
풀이시간 : 30m

#KDT 코테스터디

order대로 스택 이용해서 만들 수 있느냐 문제.

큐는 사실상 12345.. 순서대로밖에 안되기때문에 큐를 이용하는 문제라 보기 어려움.

i (다음 택배박스)와 order리스트 첫번째 요소인 o를 비교한 경우
3가지 경우로 나눠서 생각

i<o :
  i가 o가 될때까지 스택에 쌓음
    -> 반복요소 줄이고 while문 없애기 위해 while -> if로, append(하나씩) -> extend(한방에)로 바꿈
i==o :
  싣음.
  i++
i>o :
  무조건 스택에 있어야하고, 없으면 더이상 불가능한 경우.
  스택에 있다면 꺼내서 싣음.
  if 없으면?
    break
    --> 이후 조건 합쳐줘서 코드가 간략해짐.
        시간은 짧아진것도 있고 늘어난것도 있고

<<before>>:
elif i>o:
  if s and s[-1]==o:
    s.pop()
  else:
    break

<<after>>:
elif i>o and s and s[-1]==o:
    s.pop()
else:
    break

'''
