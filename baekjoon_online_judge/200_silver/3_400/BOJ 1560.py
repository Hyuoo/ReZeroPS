n=int(input())
print(1 if n==1 else (n-1)*2)
'''
비숍
풀이시간 : 17m

아니 이거 정답 실화냐

비숍은 특성상 흰/검 갈수있는 영역이 서로 격리된다.
각 케이스마다 n이면 어케어케 n-1개를 놓을 수 있다.

그냥 가장자리만 돌면서 안겹치게 놓기만해도 최대로 놓는법이다.
놔보면 보인다.
'''