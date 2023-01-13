'''
단순 구현문제. 풀이 시간 : 6m

각 숫자 별 갯수를 세어서 가장 많은 숫자만큼이 답.
6,9는 같이 세고 2단위로 올림.
'''
n = input()
ar=[0 for _ in range(9)]
for s in n:
    if s=="9":
        s="6"
    ar[int(s)]+=1
ar[6] = (ar[6]+1)//2
print(max(ar))
