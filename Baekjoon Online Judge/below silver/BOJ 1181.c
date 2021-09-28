#include <stdio.h>
#include <string.h>

void swap(int* a, int* b);

int main() {
	// 1. 길이순으로 정렬 후
	// 2. 동 길이 사전순으로 정렬
	// [idx][len] : str
	int N, *len, *idx;
	char (*ar)[52];
	char* ch;
	scanf_s("%d ", &N);
	idx = malloc(sizeof(int) * N);
	len = calloc(sizeof(int) , N);
	ar = malloc(sizeof(char[52]) * N);

	//단어 입력받기
	for (int i = 0; i < N; i++) {
		idx[i] = i;
		fgets(ar + i, 52, stdin);
		ch = ar + i;
		while (*ch) {
			ch++;
			len[i]++;
			if (*ch == '\n')
				*ch = '\0';
		}
	}

	//길이순 정렬
	for (int i = 0; i < N-1; i++)
		for (int j = i; j < N; j++)
			if (len[idx[i]] > len[idx[j]])
				swap(idx + i, idx + j);

	/*for (int i = 0; i < N; i++) {
		printf("[%02d](%2d) : ", idx[i], len[idx[i]]);
		puts(ar + idx[i]);
	}*/
	
	//인덱스 제거해가면서, 길이 같으면 사전순 정렬
	for (int i = 0; i < N - 1; i++) {
		if (idx[i] == -1)
			continue;
		for (int j = i + 1; j < N; j++) {
			if (idx[j] == -1)
				continue;
			if (len[idx[i]] == len[idx[j]]) {
				if (strcmp(ar[idx[i]], ar[idx[j]]) > 0)
					swap(idx + i, idx + j);
				if (strcmp(ar[idx[i]], ar[idx[j]]) == 0)
					idx[j] = -1;
			}
			else if (len[idx[i]] < len[idx[j]])
				break;
		}
	}
	
	//결과 출력
	for (int i = 0; i < N; i++) {
		if (idx[i] == -1) {
			continue;
		}
	//	printf("[%02d](%2d) : ", idx[i], len[idx[i]]);
		puts(ar + idx[i]);
	}
}

void swap(int* a, int* b) {
	int tmp;
	tmp = *a;
	*a = *b;
	*b = tmp;
}
