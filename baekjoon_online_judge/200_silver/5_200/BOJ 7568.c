int main() {
	int N, tmp;
	int (*arr)[3];
	scanf("%d", &N);
	arr = (int*)malloc(sizeof(int) *N *3);

	for (int i = 0; i < N; i++) {
		scanf("%d%d", &arr[i][0], &arr[i][1]);
	}
	for (int i = 0; i < N; i++) {
		tmp = 1;
		for (int j = 0; j < N; j++) {
			if (i == j) continue;
			if (arr[i][0] < arr[j][0] && arr[i][1] < arr[j][1]) tmp++;
		}
		arr[i][2] = tmp;
	}
	for (int i = 0; i < N; i++) {
		printf("%d ", arr[i][2]);
	}
}
