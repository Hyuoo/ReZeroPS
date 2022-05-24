#include <math.h>
void primeNum(int m, int n) {
	int *arr = calloc(sizeof(int),(n + 1));
	int i, e = sqrt(n);
    arr[1] = 1;
	for (i = 2; i <= e; i++) {
		if (!arr[i]) {
			for (int j = i * 2; j <= n; j += i) {
				arr[j] = 1;
			}
		}
	}
	for (i = m; i <= n; i++) {
		if(!arr[i])
			printf("%d\n", i);
	}
}
main(){
	int a, b;
	scanf("%d%d", &a, &b);
	primeNum(a, b);
}
