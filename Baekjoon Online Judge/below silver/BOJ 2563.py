'''
전체 면적에서 칠해진 부분 찾는 문제.
일단 다 더하고 겹쳐진 부분을 제외하는 식으로 계산을 해볼까 했다가
종이 수 100개를 일일히 하는것보다
100*100 맵을 만들어서 그냥 칠해지는 면적을
말그대로 칠한 다음에 칠해진 칸 수를 세는 방식으로 풀었다.
'''
n = int(input())
maps = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(n):
    a,b = map(int, input().split())
    for i in range(a,a+10):
        for j in range(b,b+10):
            maps[i][j] = 1
print(sum([m.count(1) for m in maps]))
