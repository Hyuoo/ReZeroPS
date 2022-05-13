int getpapa(int *papa, int n) {
	if (papa[n] == n) return n;
	return papa[n] = getpapa(papa, papa[n]);
}
int main() {
	int N, M;
	int i, src, dest, ans=0;
	int* papa;
	scanf("%d%d", &N, &M);
	papa = malloc(sizeof(int*)*N);

	for (i = 0; i < N; i++)
		papa[i] = i;

	for (i = 0; i < M; i++) {
		scanf("%d%d", &src, &dest);
		if (getpapa(papa, src) == getpapa(papa, dest)) {
			ans = i + 1;
			break;
		}
		papa[getpapa(papa,dest)] = papa[src];
	}
	printf("%d", ans);
}
