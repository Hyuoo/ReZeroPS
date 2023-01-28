//py로 푼 코드 그대로 c

#include <stdio.h>
#include <stdlib.h>

int* Counter(char* q, int size);

int main() {
	int tc, N, M;
	char* q;
	int i, j, pri;
	int* priority;
	int tmp;

	scanf("%d", &tc);
	for (int t = 0; t < tc; t++) {
		scanf("%d %d", &N, &M);
		q = (char*)malloc(sizeof(char*) * N);
		for (int j = 0; j < N; j++) {
			scanf("%d", &tmp);
			q[j] = (char)tmp;
		}
		priority = Counter(q, N);
		i = 0;
		j = 1;
		pri = 9;
		while (1) {
			while (priority[pri]==0) {
				pri--;
			}
			if (q[i % N] == pri) {
				if (i % N == M) {
					printf("%d\n", j);
					break;
				}
				j++;
				q[i % N] = 0;
				priority[pri]--;
			}
			i++;
		}
		free(q);
		free(priority);
	}
}

int* Counter(char* q, int size) {
	int* priority;
	priority = (int*)calloc(sizeof(int*), 10);
	for (int i = 0; i < size; i++) {
		priority[q[i]]++;
	}
	return priority;
}
