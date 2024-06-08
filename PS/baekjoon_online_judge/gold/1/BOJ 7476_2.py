"""
Solving Date    : 2024.06.08
Solving Time    : -
Title           : 최대 공통 증가 수열
tags            : 다이나믹 프로그래밍
url             : https://www.acmicpc.net/problem/7476
runtime         : 872 ms
memory          : 34964 KB
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
ar = [*map(int, input().split())]
m = int(input())
br = [*map(int, input().split())]

# 중복을 미리 없애는게 더 빨라지지 않을까: 빨라짐 100ms정도?
ar = [x for x in ar if x in br]
n = len(ar)
br = [x for x in br if x in ar]
m = len(br)

# print(ar)
# print(br)

memoi = [[None for _ in range(500)] for _ in range(500)]
track = [[(None, None) for _ in range(500)] for _ in range(500)]

def lcis(x, y):
    if x == n or y == m:
        return 0
    if memoi[x][y]:
        return memoi[x][y]
    
    memoi[x][y] = 1
    for i in range(x+1, n):
        if ar[x] >= ar[i]:
            # 더 큰값이 아니면 스킵
            continue
        for j in range(y+1, m):
            if ar[i] == br[j]:
                # 더 큰 값 매칭 시 재귀반복
                tmp = lcis(i, j) + 1
                if memoi[x][y] < tmp:
                    memoi[x][y] = tmp
                    track[x][y] = (i, j)
                # print(x, y, ">", i, j, ">>", tmp)

                # # 뒤에서 앞으로 트래킹 시 시작을 모름 ㅇㅅㅇ
                # # track[i][j] = (x, y)
                break

    return memoi[x][y]

ret = 0
start_idx = (None, None)
for i in range(n):
    for j in range(m):
        if ar[i] == br[j]:
            # 매칭되면 뒷부분에서 재귀적으로 (더 큰 + 매칭되는 값)을 찾음
            tmp = lcis(i, j)
            if ret < tmp:
                ret = tmp
                start_idx = (i, j)
            # print(i, j, ">>", tmp)
            # br에서 같은 수 찾으면 뒤는 볼필요 없어 break
            break

def trace(x, y, s):
    # 그냥 순서대로 따라가면서 리스트에 넣는 함수
    if x is None and y is None:
        return s
    s.append(ar[x])
    return trace(*track[x][y], s)

print(ret)
print(*trace(*start_idx, []))


"""
당최 안풀려서 결국 검색찬스 씀.

그래서 LCIS가 뭐시여? 하고
문제를 다시 보고 어.? 완전 잘못풀고있었네 하고

그냥 틀린방식으로 계속 하고있었다.


- 암튼 풀이는 결국 A배열 B배열을 4중으로 순회하여 "최대 공통 증가 수열"을 찾음.
    - 2중으로 먼저 [i:][j:] 순회하고, 같은 값 발견 시 [i+1:][j+1:] 재귀적 순회
- 찾는 과정에서 "수열"을 추적하기 위해 track[][] 리스트에 다음 순서의 수열 위치를 저장
- [i:][j:]를 순회하는 과정에서 가장 긴 길이의 인덱스(i, j)를 저장해서 해당 지점부터 trace함수로 추적


시간 단축을 위해서:
- "공통" 수열을 구하기 때문에 두 수열에 모두 있는 값이 아니면 존재조차 필요없다.
    -- set() & set()을 하여 ar[i][j] not in SET 처럼 하려고 했는데 그게 더 오래걸릴 것 같아 바꿈
    - A, B 배열에서 처음부터 중복으로 존재하는 값만 남기고, 길이 (n, m)변수까지 재구성 함
- 재귀적으로 찾는 과정에서 memoi리스트를 통해서 [i][j]의 LCIS값을 저장함.
    - (변하는 값이 아니라 dp말고 memoi라 사용,,)


크아악
"""