def z_search(n,i,j,r,c,seq):
    if n==0 or (i>r or i+n<=r or j>c or j+n<=c):
        return -1
    if i==r and j==c:
        return seq
    n//=2
    for step,(x,y) in enumerate([[0,0],[0,n],[n,0],[n,n]]):
        t = z_search(n, i+x, j+y, r, c,seq+((n**2)*step))
        if t!=-1:
            return t
n,r,c=map(int,input().split())
print(z_search(2**n,0,0,r,c,0))
'''
Z
풀이시간 : 40m

(재귀적인 문제를 푸는데 왜 함수를 안쓰려그래)

Z모양으로 4분할해서 재귀탐색 하는 문제.
현재위치의 기준점 (i,j)과 n으로 현재 사분면에 포함되는지 검사하고,

현재 사분면에 포함되면 다시 4분할에서 또 탐색.

(r,c) 좌표까지 문제없이 접근하고 정상종료 리턴이 되면
코드 수정해서 그 자리에 탐색한 순서를 리턴하게끔 변경.

각 사분면은 (n*n번째) 탐색 순서가 포함되니
Z순으로 n*n씩 건너뛰면 끝 (n**2)*step. step은 0,1,2,3
'''
