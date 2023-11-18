'''
트라이구조 문제
root노드에서부터 없으면 만들고 있으면 이동하고 마지막부분엔 1찍어주기
끝

근데 python3로 제출하면 계속 시간초과나서 pypy3로 제출하니까 바로됨 ㅂㄷ

다른 파이썬 풀이를 보니 정렬하고 List.startswith(str) 메소드를 이용해서 한번에 풀더라
혹은 그냥 정렬된 문자열에서, 중복된 숫자는 안나온다고 했으니 같은길이가 아닐때 더 긴거에 앞부분이 똑같은지 문자열 검사만 해줘도 됨.
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
