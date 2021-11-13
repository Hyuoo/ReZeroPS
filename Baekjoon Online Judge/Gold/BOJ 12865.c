int main() {
	int n, k, w, v, i, t;
	scanf("%d %d", &n, &k);
	int* dp = calloc(sizeof(int), k+1);
	while(n--){
		scanf("%d %d", &w, &v);
		for(i=k;i>=w;i--){
			t = dp[i-w]+v;
			dp[i] = t>dp[i]?t:dp[i];
		}
	}
	printf("%d", dp[k]);
}
