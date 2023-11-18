#https://school.programmers.co.kr/learn/courses/30/lessons/120956
'''
문자열단위로 소거시키면 되겠다 싶어서 replace()사용해서 반복처리
입력값에 숫자가 안들어있어서 "1"로 하고나서 다 없애고, 0이 된 갯수를 세었는데
다른 풀이를 보니 그냥 처음부터 " " 공백문자로 준 다음에 strip()해버리면.. 어 똑같나? 아니 오히려 문자열 없애는것보다 바꾸는게 더 빠르지않을까 싶은데
그리고 if문도 어차피 빈문자열이 되니가 not ba 이런식으로 했어도 됐겠다.
if not ba.reaplce("1",""):
  answer+=1
'''
def solution(babbling):
    st = ["aya","ye","woo","ma"]
    answer=0
    for ba in babbling:
        for s in st:
            ba=ba.replace(s,"1")
        ba=ba.replace("1","")
        if(len(ba)==0):
            answer+=1
    return answer
