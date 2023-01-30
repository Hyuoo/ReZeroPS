// py >> c
#include <stdio.h>
#include <stdlib.h>
#define INF (100000*100)

void pg(int** g, int n) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			printf("%d ", g[i][j] == INF ? 0 : g[i][j]);
        }
		printf("\n");
	}
}

int main() {
	int n,m;
	int** g;
	int a, b, c;
	
	scanf("%d\n%d", &n, &m);
	g = (int**)malloc(sizeof(int*) * n);
	for (int i = 0; i < n; i++) {
		g[i] = (int*)malloc(sizeof(int) * n);
		for (int j = 0; j < n; j++) {
			g[i][j] = i == j ? 0 : INF;
		}
	}

	while (m--) {
		scanf("%d%d%d", &a, &b, &c);
		a--; b--;
		g[a][b] = c < g[a][b] ? c : g[a][b];
	}

	for (int via = 0; via < n; via++) {
		for (int src = 0; src < n; src++) {
			for (int dst = 0; dst < n; dst++) {
				g[src][dst] = g[src][dst] < g[src][via] + g[via][dst] ? g[src][dst] : g[src][via] + g[via][dst];
			}
		}
	}
	pg(g, n);
}
