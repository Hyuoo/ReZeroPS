#https://school.programmers.co.kr/learn/courses/30/lessons/169198

def solution(m, n, startX, startY, balls):
    ans = []
    for x, y in balls:
        case = []
        
        if startY!=y or startX<x:
            case.append([-x,y])
        if startY!=y or startX>x:
            case.append([m+m-x,y])
        if startX!=x or startY<y:
            case.append([x,-y])
        if startX!=x or startY>y:
            case.append([x,n+n-y])
        
        dist = 999999
        for case_x, case_y in case:
            x_len = abs(case_x-startX)
            y_len = abs(case_y-startY)
            tmp = x_len**2+y_len**2
            dist = min(dist,tmp)
        ans.append(dist)
    
    return ans
'''
당구 연습
풀이시간 : 1h 30m 정도,,,????
#KDT_코테스터디

:: 아니 나는 정말 바본가✨⭐😘😁 ::
최솟값 넣는 dist 초기화를 99999로 해놓고 통과 못해서
예외처리를 내가 잘못했나 대체 무슨 예외가 있는거고 어떻게 처리해야하지
하고 한시간 고민했는데
문득 "어 근데 dist가 좀 작지않나?" 해서 9999999999갈겨보니까 바로 통과
ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
아니 대충생각해도 가로천 세로천이라서
백만이면 되겠군! 하고
별로 안크네! 하고
진짜 처음 짤때부터 생각은 했는데 생각만 해놓고 생각없이 최솟값 설정한거
생각없는거 실화

풀이..
- 무적권 1쿠션을 해서 맞춘다
and
- 입사각반사각이 직선 똑띠
=> 벽면에 대칭이동한 직선거리와 같다.

예외사항
공이 수직 수평한 위치에 있는데 벽 사이에 공이 존재하는 경우.

처리하면
끝
와나 이 쉬운걺ㄴㅇ랃거ㅏㅣㅁㄷ구퍼푿미ㅏㅓㅜㅇㄴㄹㅍ가ㅓ
'''
