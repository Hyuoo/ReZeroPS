'''
행렬제곱
풀이시간 : 일단 대충 1시간


'''
import copy

# a행렬, b행렬 받아서 행렬곱 리턴
def matmul(a,b,n):
    new = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                new[i][j] += a[i][k]*b[k][j]
    return new

# a행렬의 n제곱 (matmul을 n-1번 반복호출)
def matnmul(a,n):
    n -= 1
    tmp = copy.deepcopy(a)
    for _ in range(n):
        a = matmul(a,tmp,len(a))
    return a

# 그냥 행렬출력
def pp(a):
    for i in a:
        print(i)
    print("-" * 20)

# 문제용 코드 (입출력)
# n, b = map(int,input().split())
# a = []
# for i in range(n):
#     a.append(list(map(int,input().split())))
#
# a = matnmul(a,b)
#
# for i in a:
#     print(i)

# 각 a1을 n제곱 한 배열이 an
a1 = [[1,2],[3,4]]
a2 = [[7,10],[15,22]]
a3 = [[37,54],[81,118]]
a4 = [[119,290],[435,634]]
a5 = [[1069,1558],[2337,3406]]
# 근데 (3, 2) 이런건 맞는값이 나오고
# (4, 1), (1, 4) 이거는 틀린 값이 나온다.
# 행렬이 순서만 지켜지면 상관없는거 아닌가?
# 근데 n제곱이니까 A x A x A x A x A잖아
# 
ba = matmul(a3,a2,2)
bb = matmul(a4,a1,2)
pp(a5)
pp(ba)
pp(bb)
