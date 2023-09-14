#include <string.h>
#include <stdio.h>
#define UNDER (1<<0)
#define UPPER (1<<1)

int main(){
    char varName[101];
	int varIdx[100];
	int flag=0;
	int ch, i,j;
    
	i = j = 0;
	while (~(ch = getchar())) {
		if (ch >= 'a' && ch <= 'z') {
			varName[i++] = ch;
		}
		else if (ch >= 'A' && ch <= 'Z') {
			if (i == 0) {
				flag |= 3;
				break;
			}
			varIdx[j++] = i;
			varName[i++] = ch | 0x20;
			flag |= UPPER;
		}
		else if (ch == '_') {
			if ((i == 0) || (j && varIdx[j - 1] == i)) {
				flag |= 3;
				break;
			}
			varIdx[j++] = i;
			flag |= UNDER;
		}
	}
    if (varIdx[j-1] == i) { flag |= 3; }
	varName[i] = '\0';
	varIdx[j] = 999;

	switch (flag) {
	case 0://None
		printf("%s", varName);
		break;
	case 1://C++
		for (i = 0, j = 0; i < strlen(varName); i++) {
			if (varIdx[j] == i) {
				printf("%c", varName[i] &= ~0x20);
				j++;
			}
			else {
				printf("%c", varName[i]);
			}
		}
		break;
	case 2://Java
		for (i = 0, j = 0; i < strlen(varName); i++) {
			if (varIdx[j] == i) {
				printf("_%c", varName[i]);
				j++;
			}
			else {
				printf("%c", varName[i]);
			}
		}
		break;
	case 3:
		printf("Error!");
		break;
	}
}
