a[1001];main(n,k,i,j){scanf("%d%d",&n,&k);for(i=2;i<=n;i++)if(!a[i])for(j=i;j<=n;j+=i)a[j]=a[j]?1:(--k?0:printf("%d\n",j),1);}
