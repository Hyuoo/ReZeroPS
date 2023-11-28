"""
Solving Date    : 2023.10.17
Solving Time    : 20m
Title           : 세 용액
tags            : 정렬, 이분 탐색, 두 포인터
url             : https://www.acmicpc.net/problem/2473
runtime         : 4460 ms
memory          : 21120 KB
"""

n = int(input())
ar = sorted(map(int,input().split()))

mini = 3000000000
mini_set = []

for l in range(n-2):
    m = l+1
    r = n-1
    while m<r:
        tmp = ar[l] + ar[m] + ar[r]
        if mini>abs(tmp):
            mini = abs(tmp)
            mini_set = [ar[l], ar[m], ar[r]]
            if tmp==0:
                break
        if tmp<0:
            m += 1
        else:
            r -= 1

print(*mini_set)

"""
두 용액에서 3개로 늘어나기만 한 문제
(*두 용액 문제 2470, 2467 동일)

세개를 어떻게 할 지 하다가
4개 합을 2/2합쳐서 푼 문제가 생각나서
두개 합치고, 하나를 해서 반복을 줄이려고 했으나,
시간은 O(n^3) >> O(n^2) 인데 
list[25,000,000]가 되어 메모리 초과로 실패

정렬 후 하나 반복 잡고,
남은 사이에서 양방향 투포인터탐색으로 풀이.
시간은 동일하게 O(n^2). 추가 메모리는 사용안함.
"""