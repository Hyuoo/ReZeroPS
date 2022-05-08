#include <stdio.h>
int wordCount(const char* ch) {
	int isWord = 0, prev = 0, count = 0;
	while (*ch != '\0') {
		isWord = ((*ch >= 'a' && *ch <= 'z') || (*ch >= 'A' && *ch <= 'Z'));
		count += (isWord && !prev);
		prev = isWord;
		ch++;
	}
	return count;
}

int main() {
	char str[1000001];
	fgets(str, 1000001, stdin);
	printf("%d", wordCount(str));
}
