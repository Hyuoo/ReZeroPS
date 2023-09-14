main(){
	int *a, n, k, i, j;
	scanf("%d%d", &n,&k);
	a = calloc(sizeof(int), n+1);
	for (i = 2; i <= n; i++)
		if (!a[i])
			for (j = i; j <= n; j += i)
				if (!a[j]) {
					a[j] = 1;
					if(!--k)printf("%d",j);
				}
}
