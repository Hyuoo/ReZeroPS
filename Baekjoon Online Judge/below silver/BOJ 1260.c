#include <stdlib.h>

void DFS(const char** graph, const int N, const int V) {
	char* visit = (char*)calloc(sizeof(char), N);
	int* stack = (int*)calloc(sizeof(int), ((N+1)/2)*N);
	int now, top = 0;
	stack[0] = V-1;

	while (top != -1) {
		now = stack[top--];
		if (visit[now])
			continue;
		printf("%d ", now+1);
		visit[now] = 1;
		for (int i = N-1; i >= 0; i--) {
			if (i == now)
				continue;
			if (graph[now][i] && !visit[i])
				stack[++top] = i;
		}
	}
	free(visit);
	free(stack);
}

void BFS(const char** graph, const int N, const int V) {
	char* visit = (char*)calloc(sizeof(char), N);
	int* queue = (int*)calloc(sizeof(int), N);
	int now, head = 0, rear = 1;
	visit[queue[0] = V-1] = 1;

	while (head != rear) {
		now = queue[head++];
		printf("%d ", now+1);
		for (int i = 0; i < N; i++) {
			if (i == now)
				continue;
			if (graph[now][i] && !visit[i]) {
				visit[i] = 1;
				queue[rear++] = i;
			}
		}
	}
	free(visit);
	free(queue);
}

int main() {
	int N, M, V, src, dst;
	char **graph;
	scanf("%d %d %d", &N, &M, &V);
	graph = (char**)malloc(sizeof(char*)*N);

	for (int i = 0; i < N; i++)
		graph[i] = (char*)calloc(sizeof(char), N);

	while (M--) {
		scanf("%d %d", &src, &dst);
		graph[src-1][dst-1] = 1;
		graph[dst-1][src-1] = 1;
	}

	DFS(graph, N, V);
	puts("");
	BFS(graph, N, V);
	free(graph);
}
