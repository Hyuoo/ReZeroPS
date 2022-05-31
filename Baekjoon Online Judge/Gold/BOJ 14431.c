#include <stdio.h>
#include <stdlib.h>
#define SIZE 8500
#define INF 99999
#define DIS2(x,y) ((int)sqrt((x)*(x)+(y)*(y)))
#define DISTANCE(Ax, Ay, Bx, By) (DIS2(Bx-Ax, By-Ay))
a[SIZE]={1,1};
#define isPrime(n) (!a[n])

int main() {
	int Px,Py,Ax,Ay,N, i, j, d;
	int **pos;
	int **ar;
	for(i=2;i<=sqrt(SIZE);i++)if(!a[i])for(j=i*i;j<=SIZE;j+=i)a[j]=1;
	
	scanf("%d%d%d%d", &Px, &Py, &Ax, &Ay);
	
	scanf("%d", &N);
	N += 2;
	pos = malloc(sizeof(int*)* N);
	ar = malloc(sizeof(int*)* N);
	for (i = 0; i < N; i++) {
		pos[i] = malloc(sizeof(int) * 2);
		ar[i] = calloc(sizeof(int), N);
	}
	pos[0][0] = Px;
	pos[0][1] = Py;
	pos[1][0] = Ax;
	pos[1][1] = Ay;
	i = 2;
	while (i<N) {
		scanf("%d%d", &pos[i][0], &pos[i][1]);
		i++;
	}
	for (i = 0; i < N; i++) {
		for (j = i+1; j < N; j++) {
			d = DISTANCE(pos[i][0], pos[i][1], pos[j][0], pos[j][1]);
			if (isPrime(d)) {
				ar[i][j] = ar[j][i] = d;
			}
		}
	}

	int now, next, min;
	int *visit = calloc(sizeof(int), N);
	int *shortest = malloc(sizeof(int) * N);
	
	shortest[0] = 0;
	for (i = 1; i < N; i++) {
		shortest[i] = INF;
	}

	for (now = 0; ; now = next) {
		visit[now] = 1;
		min = INF;
		next = now;
		for (j = 0; j < N; j++) {
			if (now == j || visit[j] || !ar[now][j]) continue;
			if (shortest[j] > shortest[now] + ar[now][j]) {
				shortest[j] = shortest[now] + ar[now][j];
			}
			if (min > shortest[j]) {
				min = shortest[j];
				next = j;
			}
		}
		if (next == now)
			break;
	}
	printf("%d", shortest[1]!=INF?shortest[1]:-1);
}
