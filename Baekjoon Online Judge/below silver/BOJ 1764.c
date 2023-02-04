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
