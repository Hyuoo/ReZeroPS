'''
접근 : 아몰랑 무차별대입 벽 3개 세우고나서 각 바이러스 퍼뜨리고, 빈칸 세기 끝.

풀이 : 
1. i,j,k 3중 포문으로 모든 경우의 벽을 3개 세운다.
  >> 3개 세워진 지도를 tmp_arr로 복사. 오리지날은 arr그대로
2. 세워진 상태에서 바이러스(2)들 인덱스를 리스트(tmp_list)에 저장한다.
3. DFS하듯 tmp_list에 요소가 남아있으면 상하좌우 감염시키고 list에 넣는다.
  >> 큐가 아니라 스택으로 되었지만, 순서가 안중요해서 상관없다.
    >> 2기준에서 0인애들을 push하고 +2 했기 때문에 중복방문 우려 X
4. 3.을 끝낸 tmp_list에서 0갯수 세어서 최고기록이면 갱신
5. 제출
'''
N, M = map(int,input().split())
area = 0
arr = []
for _ in range(N):
    arr.extend(list(map(int,input().split())))

for i in range(N*M-2):
    if arr[i] == 2 or arr[i] == 1:
        continue
    for j in range(i+1, N*M-1):
        if arr[j] == 2 or arr[j] == 1:
            continue
        for k in range(j+1, N*M):
            if arr[k] == 2 or arr[k] == 1:
                continue
            tmp_arr = arr[:]
            tmp_arr[i] = 1
            tmp_arr[j] = 1
            tmp_arr[k] = 1
            tmp_list = []
            for ti, tv in enumerate(tmp_arr):
                if tv==2:
                    tmp_list.append(ti)
            while(tmp_list):
                idx = tmp_list.pop()
                tmp_arr[idx] += 2
                for ro in (-1, 1, -M, M):
                    if idx%M==0 and ro==-1:
                        continue
                    if idx%M==M-1 and ro==1:
                        continue
                    if idx+ro<0 or idx+ro>=N*M:
                        continue
                    if tmp_arr[idx+ro]==0:
                        tmp_list.append(idx+ro)
            tmp_area = tmp_arr.count(0)
            if(area<tmp_area):
                area = tmp_area
print(area)
