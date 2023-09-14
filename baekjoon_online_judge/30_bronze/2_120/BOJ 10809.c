#include <stdio.h>
int main(){
	int a[26], ch, i;
    for(i=0;i<26;i++) a[i]=-1;i=0;
    while((ch=getchar())+1)a[ch-97]==-1?a[ch-97]=i++:i++;
	for(i=0;i<26;i++) printf("%d ",a[i]);
}
