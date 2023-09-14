a[10000]={0,1};i,j;
main(){
	for(i=2;i<=100;i++)if(!a[i])for(j=i*i;j<=10000;j+=i)a[j]=1;
	int n,f;
	for (scanf("%*d"); ~scanf("%d", &n);) {
		f = 1;
		for (i = n / 2; f && i; i--) {
			if (a[i])continue;
			for (j = n / 2; f && i + j <= n ; j++) {
				if (a[j])continue;
				if (i+j==n) printf("%d %d\n", i, j, f = 0);
			}
		}
	}
}
