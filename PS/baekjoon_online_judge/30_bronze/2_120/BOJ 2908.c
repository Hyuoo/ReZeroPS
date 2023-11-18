#include <stdio.h>
int main(){
    int a, b, aa=0, bb=0;
	scanf("%d %d", &a, &b);
	for (; a; a/=10, b/=10) {
		aa=aa*10+a%10;
		bb=bb*10+b%10;
	}
	printf("%d\n", aa>bb?aa:bb);
}
