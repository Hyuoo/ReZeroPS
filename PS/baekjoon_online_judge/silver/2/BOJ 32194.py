"""
Solving Date    : 2024.09.20
Solving Time    : 39m
Title           : 질문은 계속돼
tags            : 누적 합
url             : https://www.acmicpc.net/problem/32194
runtime         : 356 ms
memory          : 52752 KB
"""
import sys
input = sys.stdin.readline

ans = [0, 1]
prev = 1
idx = 1

for _ in range(int(input())):
    op, x, y = map(int, input().split())

    tmp = (ans[x] == ans[y] and ans[x]%2+op == 2)
    # print(op, x, y, ">>", tmp, ":", ans)

    if prev != tmp: idx += 1
    ans.append(idx)
    prev = tmp

print(*map(lambda x:"YNeos"[x%2^1::2], ans[2:]), sep="\n")


"""
아래 코드로 all썼다고 '파이써닉'하게 풀고 싶었는데 시간초과.
ans = (op == 1 and all(answer_t[x:y+1])) | (op == 2 and all(answer_f[x:y+1]))
answer_t.append(ans)
answer_f.append(not ans)

배열 여러개 만들었다가 줄였다가
인덱스 여러개 썼다가 하나로 줄였다가
왔다갔다하면서 푼 문제,,
"""