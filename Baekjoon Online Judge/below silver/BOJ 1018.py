m,n = map(int,input().split())
a = [list(map(lambda x:(1 if x=="W" else 0), input())) for _ in range(m)]
w = []
f = 1
#행 교체 수 누적합
for i in range(m):
    t = [0]
    ff = f
    for j in range(n):
        if a[i][j]==ff:
            t.append(t[-1])
        else:
            t.append(t[-1]+1)
        ff^=1
    f^=1
    w.append(t)

#범위 행 교체 수
ww = [[0 for i in range(n-7)]]
for i in w:
    t = []
    for j in range(n-7):
        t.append(i[j+8]-i[j])
    ww.append(t)
#열 교체수 누적합
for i in range(m):
    for j in range(n-7):
        ww[i+1][j]+=ww[i][j]
#범위 열 교체 수
mini = 66
for i in range(m-7):
    for j in range(n-7):
        t = ww[i+8][j]-ww[i][j]
        mini = min(mini,t,abs(64-t))
print(mini)
'''
체스판 다시 칠하기
풀이시간 : 1h 13m

옛날에 보기만하고 도망간적이있는 문젠디
풀이시간도 꽤오래걸렸네
풀고나서 분류를 보니 브루트포스란다.

뭐여 괜히 헷갈리게 푼건가

암튼일단 풀이는
번갈아 나타나는 색깔 체크해서,
교체해야 할 갯수를 누적합으로 구해서 8칸 단위로 총 교체갯수를 구한다.
가로 세로 반복. 끝
'''
