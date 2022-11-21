'''
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
