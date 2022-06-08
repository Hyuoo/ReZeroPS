int main(){
	int N,M,m,i,j,f;
	scanf("%d%d",&N,&M);
	int** ar=malloc(sizeof(int*)*N);
	for(i=0;i<N;i++)ar[i]=malloc(sizeof(int)*M);
	for(i=0;i<N;i++)
		for(j=0;j<M;j++)
			scanf("%1d", &ar[i][j]);
	m=N<M?N:M;f=1;
	while(f&&m--)
		for(i=0;i+m<N;i++)
			for(j=0;j+m<M;j++)
				if(ar[i][j]==ar[i][j+m] && ar[i][j]==ar[i+m][j] && ar[i][j]==ar[i+m][j+m])
					f = 0;
	printf("%d",++m*m);
}
