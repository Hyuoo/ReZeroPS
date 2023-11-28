#include <stdio.h>
int main() {
	int ch[52], sum = 0, tmp = 0, sign = 1;
	fgets(ch, 52, stdin);
	char *exp = ch;
	while (*exp != '\0' && *exp != '\n') {
		switch (*exp) {
		case '+':
		case '-':
			sum += tmp*sign;
			tmp = 0;
			if(*exp=='-')sign = -1;
			break;
		default:
			tmp = tmp * 10 + *exp - '0';
		}
		exp++;
	}
	printf("%d", sum + tmp*sign);
}
