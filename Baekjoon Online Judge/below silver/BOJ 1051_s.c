a[50][50];N,M,m,i,j,f,c;main(){scanf("%d%d",&N,&M);for(i=0;i<N;i++)for(j=0;j<M;j++)scanf("%1d",&a[i][j]);m=N<M?N:M;f=1;while(f&&m--)for(i=0;i+m<N;i++)for(j=0;j+m<M;j++){c=a[i][j];if(c==a[i][j+m]&&c==a[i+m][j]&&c==a[i+m][j+m])f=0;}printf("%d",++m*m);}
