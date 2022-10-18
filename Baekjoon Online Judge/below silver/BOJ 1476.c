#include <stdio.h>
//제일 작은 수를 그 빼는값만큼 더해서 셋 다 같은값이 되면 그 날짜가 해답
int main(){
	int e,s,m;
	scanf("%d %d %d",&e,&s,&m);
	while(e!=s||s!=m){
		if(e<s){
			if(e<m)e+=15;
			else m+=19;
		}
		else{
			if(s<m)s+=28;
			else m+=19;
		}
	}
	printf("%d",e);
}
