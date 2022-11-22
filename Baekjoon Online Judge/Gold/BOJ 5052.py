'''
트라이구조 문제
root노드에서부터 없으면 만들고 있으면 이동하고 마지막부분엔 1찍어주기
끝

근데 python3로 제출하면 계속 시간초과나서 pypy3로 제출하니까 바로됨 ㅂㄷ
'''
t = int(input())
for test_case in range(t):
    n = int(input())
    ans = "YES"
    root = [None for _ in range(10)]
    for _ in range(n):
        if ans=="NO":
            _ = input()
            continue
        now = root
        flag = 1
        for s in input():
            s = int(s)
            if now[0]==1:
                ans = "NO"
                break
            elif now[s]==None:
                now[s] = [None for _ in range(10)]
                flag = 0
                now = now[s]
            else:
                now = now[s]
        if flag:
            ans="NO"
        now[0] = 1
    print(ans)
