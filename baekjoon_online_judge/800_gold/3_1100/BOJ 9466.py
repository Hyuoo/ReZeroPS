t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    ar = [0]+list(map(int,input().split()))
    v = [0 for _ in range(n + 1)]
    sub_ans = n
    for i in range(1,n+1):
        if ar[i]==0:
            continue
        next = i
        while ar[next]!=0:
            if ar[next] == 0:
                break
            v[next] = i
            next = ar[next]
            if v[next]==i:
                while ar[next]!=0:
                    tmp = ar[next]
                    ar[next] = 0
                    next = tmp
                    sub_ans -= 1
                break
        while ar[i] != 0:
            tmp = ar[i]
            ar[i] = 0
            i = tmp
    ans.append(sub_ans)
print(*ans,sep="\n")

'''
텀 프로젝트
풀이시간 : 1h 54m

그래프 탐색 문제
대강 사이클을 찾아내고 처리하는 문제?

각 학생들이 번호를 지목해서 사이클이 완성될경우 한 팀이다.
사이클이 안되면 팀에 속할수없다.
이방인 학생의 수를 구하여라.

일단 순회하면서 사이클이 생기면 생긴애들 분류 하는 식으로 접근.
시간초과가 오지게 뜸.
그래서
1차 -> 제외된 학생도 또 돌아서, 제외학생 예외처리
2차 -> 스택없이 방문으로만 처리하는건 '제외'할때 손해같아서 스택추가
3차 -> sys.stdin.readline이 범인인가 싶어 괜히 설정
4차 -> 계속 '사이클이 완성'된 학생들만 제외했어서 아닌학생들도 어쨋든 다시이뤄질일 없으니 제외
5차 -> 테스트케이스가 여러개라 매번 처리하는게 문젠가싶어 일괄출력
6차 -> v. 방문 체크 배열을 매 for i in range(1,n+1)사이클마다 생성했는데,
        여러번 만들필요없이 i번째는 i로 두니 해결
    계속 방문체크를 T/F로만 생각하느라 방문체크는 무조건 있긴 해야하는데 어케 줄일지 생각을 못했다.

* 24~27 라인 없으면 다시 시간초과
* 일괄처리로 답안 출력하는건 시간 4204ms -> 4160ms 단축됨
* 13, 14 라인도 필요없는데 왜 살아있냐 이제보니까

더 줄이고싶은데 내머리만으론 방법을 몰루겠다
'''
