#include <stdio.h>
#include <math.h>

int main() {
	int N, n;
	int arr[8001] = { 0, };
	double sum = 0;
	int mid, min=4001, max = -4001, mmax = 8000, mmmax;

	scanf("%d", &N);
	for (int i = 0;i<N;i++) {
		scanf("%d", &n);
		sum += n;
		arr[n + 4000] += 1;
		min	= n < min ? n : min;
		max = n > max ? n : max;
	}
	sum /= N;
	N /= 2;
	for (int i = 0; ; i++) {
		if (arr[i]) {
			N -= arr[i];
		}
		if (N < 0 && arr[i] != 0) {
			mid = i - 4000;
			break;
		}
	}
	for (int i = 8000; i >= 0; i--) {
		if (arr[mmax] <= arr[i]) {
			if (arr[mmax] == arr[i]) {
				mmmax = mmax;
			}
			mmax = i;
		}
	}
	printf("%d\n%d\n%d\n%d", (int)(round(sum)), mid, (arr[mmax]==arr[mmmax]?mmmax:mmax)-4000, max-min);
}
