//내스타일 다익스트라
/*
#define SIZE (n)
#define MAX_VALUE (9999)
#define START (0)
그래프 배열 graph[SIZE][SIZE] 가 있을때 

준비물:
int now, next, min;
int *visit = alloc(SIZE)
int *shortest = alloc(SIZE)

- shortest배열 now 기준으로 초기화
- now 는 시작위치 아무데나 

과정:
//이후 now부터 시작
now = START
//next가 없을때 알아서 나가므로 무한루프
while(1):
	visit[now] <- True
	min = MAX_VALUE
	next = now

	//now로부터 모든 배열 탐색. -> idx -> j
	for j in range(SIZE):
		//j가 now와 같거나, 이미 방문했거나, 갈수없는곳이면 j++
		if((now == j) AND (visit[j] == True) OR (graph[now][j] == MAX_VALUE)):
			continue;
		//기존 최단거리보다 now->j로 가는게 더 짧으면 갱신
		if(shortest[j] > shortest[now] + ar[now][j]):
			shortest[j] = shortest[now] + ar[now][j];
		if(min > shortest[j]):
			min = shortest[j]
			next = j

	//next가 한번도 갱신되지 않으면(now) 갈수있는곳이 없음
	if(next == now):
		break
	now = next
*/

#define SIZE (1000)
#define MAX_VALUE (9999)

int* Dijkstra(int* graph, int start){
	int now, next, min;
	int *visit = calloc(sizeof(int), SIZE);
	int *shortest = malloc(sizeof(int) * SIZE);
	
	for (i = 0; i < N; i++) {
		shortest[i] = MAX_VALUE;
	}

	for (now = start; ;now = next) {
		visit[now] = true;
		min = MAX_VALUE;
		next = now;
		for (j = 0; j < SIZE; j++) {
			if (now == j || visit[j] || !ar[now][j]) continue;
			if (shortest[j] > shortest[now] + graph[now][j]) {
				shortest[j] = shortest[now] + graph[now][j];
			}
			if (min > shortest[j]) {
				min = shortest[j];
				next = j;
			}
		}
		if (next == now)
			break;
	}
	
	return shortest;
}
