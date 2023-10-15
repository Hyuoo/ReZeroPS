//작성중
#define INF (long)2e9
typedef struct NODE {
	int n;
	int w;
	struct NODE* l;
}node;
long* directed_dijkstra(node** graph, int graphSize, int startIdx);


long* directed_dijkstra(node** graph, int graphSize, int startIdx){
	long* visit = (long*)malloc(sizeof(long) * graphSize);
	long* shortest = (long*)malloc(sizeof(long) * graphSize);
	node* tmp;
	int next = 0;
	int now = startIdx;

	for (int i = 0; i < graphSize; i++) {
		visit[i] = 0;
		shortest[i] = INF;
	}

	visit[startIdx] = 0;
	shortest[startIdx] = 0;
	tmp = graph[startIdx];

	//방향이 있기 때문에 갈수있는 부분 중에서만 다음 지점(next)를 탐색한다.
	while (next != -1) {
		visit[now] = 1;
		tmp = graph[now];
		next = -1;

		while (tmp != NULL) {
			//갈 수 있으면 더 짧은 거리 갱신하고
			if (visit[tmp->n] == 0 && shortest[tmp->n] > shortest[now] + tmp->w)
				shortest[tmp->n] = shortest[now] + tmp->w;
			tmp = tmp->l;
		}

		//갈수있는 곳 중 가장가까운곳 next로
		for (int i = 0; i < graphSize; i++) {
			if (visit[i] == 0 && shortest[i] != INF) {
				if (next == -1 || shortest[next] > shortest[i]) {
					next = i;
				}
			}
		}
		now = next;
	}

	return shortest;
}
