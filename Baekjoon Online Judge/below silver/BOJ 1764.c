//C로 푸는데 qsort, bsearch에서 2차원 포인터 이용하는데에 거의 두시간 걸렸다. 그래서 포인터없이 풀었다. 젠장
#include <stdio.h>
#include <string.h>

char list[500001][21];
char tmp[21];
char* answer[500001];
char* p;
int i, j;

int cmp(const void* a, const void* b) {return strcmp(*(char**)a, *(char**)b);}

int main() {
	int n, m;
	scanf("%d%d\n", &n, &m);
	for (i = 0; i < n; i++) gets(list+i);
	qsort(list, n, 21, strcmp);
	for (i = 0; i < m; i++) {
		p = bsearch(gets(tmp), list, n, 21, strcmp);
		if (p != NULL) {
			answer[j++] = p;
		}
	}
	qsort(answer, j, sizeof(char*), cmp);
	printf("%d\n", j);
	for (i = 0; i < j; i++) puts(answer[i]);
}
