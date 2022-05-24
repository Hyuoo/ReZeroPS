a[250000]={0,1};i,j,c;main(){for(i=1;++i<=500;)if(!a[i])for(j=i*i;j<=25e4;j+=i)a[j]=1;for(;scanf("%d",&i),i;){for(c=0,j=i;j<i*2;c+=!a[++j]);printf("%d\n",c);}}
