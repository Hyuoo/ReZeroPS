a[1001]={0,1};i,j,c;main(){for(i=1;++i<=32;)if(!a[i])for(j=i*2;j<=1e3;j+=i)a[j]=1;scanf("%*d");for(;~scanf("%d",&i);c+=!a[i]);printf("%d",c);}
