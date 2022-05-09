int main(){
	int T,R,r;
	char str[21],*s;
	scanf("%d",&T);
	while(T--){
		scanf("%d %s",&R,str);
		r=R;
		s=str;
		while(*s!='\0'){
			putchar(*s);
			if(!--r){
				r=R;
				s++;
			}
		}
		puts("");
	}
}
