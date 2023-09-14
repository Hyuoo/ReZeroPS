int main() {
	int i, j, n;
	int arr[1001];
	arr[0] = 0;
	for (i = j = n = 1; i < 1001; i++,n++) {
		arr[i] = arr[i-1] + j;
		if (j == n) j++, n = 0;
	}
	scanf("%d%d", &i, &j);
	printf("%d", arr[j] - arr[i-1]);
}
