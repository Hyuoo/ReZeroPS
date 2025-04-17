"""
Solving Date    : 2024.09.09
Title           : 친구
tags            : 그래프 이론, 브루트포스 알고리즘, 그래프 탐색, 최단 경로, 플로이드–워셜
url             : https://www.acmicpc.net/problem/1058
rank            : 5
byte            : 192 B
"""

n=int(input())
a=[input()for _ in range(n)]
print(max([len(set([i for x in q for i in range(n) if a[x][i]=="Y"]+q)-{i})for i,q in((i,[j for j in range(n) if a[i][j]=="Y"])for i in range(n))]))

"""
숏코딩 할 생각이 없었는데
줄이다보니 이래됨
"""