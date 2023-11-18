int main() {
	char* a[] = {"mixed", "descending","ascending" };
	int upFlag = 2, downFlag = 1,prev, now;
	for (prev = getchar(); ~(now = getchar());) {
		if (now<'0' || now>'9')
			continue;
		if (prev > now)
			upFlag = 0;
		if (prev < now)
			downFlag = 0;
		prev = now;
	}
	puts(a[upFlag + downFlag]);
}
/* 아니 이거 외않됌?
#include <stdio.h>
#include <string.h>
int main() {//에라이
	char* a[] = {"descending", "mixed", "ascending"};
	char c[16];
	char asc[] = "1 2 3 4 5 6 7 8";
	char desc[] = "8 7 6 5 4 3 2 1";
	fgets(c, 16, stdin);
	puts(a[strcmp(asc,c) + strcmp(desc,c) + 1]);
}
*/
