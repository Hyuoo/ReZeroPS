#include <stdio.h>
int main() {
	int N, P, a,b, c=0;
	int* st[7];
	int sp[7];
	scanf("%d%d", &N, &P);
	for (int i = 1; i < 7; i++) {
		st[i] = malloc(sizeof(int) * P);
		sp[i] = 0;
	}

	while (N--) {
		scanf("%d%d", &a, &b);
		if (sp[a]) {
			while (st[a][sp[a] - 1] > b) {
				sp[a]--;
				c++;
			}
			if (st[a][sp[a] - 1] != b) {
				st[a][sp[a]++] = b;
				c++;
			}
		}
		else {
			st[a][sp[a]++] = b;
			c++;
		}
	}
	printf("%d", c);
}
