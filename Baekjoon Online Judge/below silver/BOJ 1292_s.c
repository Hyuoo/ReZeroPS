a[1001];n;main(i,j){for(i=j=1;i<1001;){a[i++]=a[i-1]+j;if(j==++n)j++,n=0;}scanf("%d%d",&i,&j);printf("%d",a[j]-a[i-1]);}
