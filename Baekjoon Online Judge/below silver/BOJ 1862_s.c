c;main(a,b){scanf("%d",&a);for(b=1;c+=(a%10-(a%10>4?1:0))*b,a/=10;b*=9);printf("%d",c);}
//아니근데 파이썬이 더 짧넹 더 줄일수있나
//o;main(a){for(;~(a=getchar());o+=a-48-(a>52))o*=9;printf("%d",o);} < 이거 왜ㅣ않ㄷ되
