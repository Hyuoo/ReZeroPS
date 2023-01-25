'''
오등큰수.
풀이시간 : 38m
스택써서 규칙찾는 문제.

오등큰수가 뭔지 지문부터 헷갈린다.
애초에 문제를 풀려고 들어갈때 문제 분류가 스택에 있어 스택으로 접근 할 생각을 했다.
스택이라는 힌트가 없었으면 시간이 두배는 들었을 듯.

처음 접근은 우선 가장 무식한방법으로 앞에서부터 인덱스잡고, 이후 배열에서 차례로 비교해서 찾는것.
당근빠따 시간초과가 날 줄 알았지만 제출은 해 봐야지.

어쨋든 뒤쪽부터 비교를 해야하는데,
지금까지 비교 한 수들 중에서 현재 숫자의 개수보다 큰 값이어야한다.
즉 빈도가 큰 수 위에 작은 수를 쌓고, 현재보다 작은놈은 다 탈락시키면서 스택에 쌓는다.
작은놈은 어차피 현재에 가려져서 안보이는 셈.

문제를 쉽게 이해하려면 숫자가 나타나는 빈도 수를 그대로 배열로 옮기면 이해하기 쉽다.
예제의 [1 1 2 3 4 2 1] 경우에는 [3 3 2 1 1 2 3] 이런식으로.
'''

from collections import Counter
N = int(input())
ar = list(map(int,input().split()))
ac = Counter(ar)
st = []
ans = []
for i in range(len(ar)-1,-1,-1):
    while st:
        if ac[st[-1]]<=ac[ar[i]]:
            del st[-1]
            continue
        else:
            ans.append(st[-1])
            break
    if not st:
        ans.append(-1)
    st.append(ar[i])
ans.reverse()
for i in ans:
    print(i, end=" ")
