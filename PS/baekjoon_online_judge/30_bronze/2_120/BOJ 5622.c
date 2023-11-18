#include <stdio.h>
#include <string.h>

int main() {
	int alph[26],i,a=0;
	char st[16];
	for(i=0;i<25;i++) {
		alph[i]=3+((i-(i>17?1:0))/3);
	}
	alph[i]=10;
	scanf("%s", st);
	for(i=0;i<strlen(st);i++) {
		a+=alph[st[i]-'A'];
	}
	printf("%d", a);
}
