int main(){
 	int a, d[6]={0,}, m=0;
	for(;~scanf("%d ", &a);){m=m>++d[a-1]?m:d[a-1];};
	for(a=6; a; a--){if(d[a-1]==m){printf("%d", 1000*(m-1)*(m^3?1:5)+(a)*(m^3?100:1000));break;}};   
}
