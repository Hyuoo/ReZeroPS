int main() {
	char check[26] = { 0, };
	int N, c=0, prev, now, flag;
	scanf("%d ", &N);
	while (N--) {
		memset(check,0,26);
		prev = -1;
		flag = 1;
		while ((now = getchar())!='\n') {
			now -= 'a';
			if (prev != now && check[now])
				flag = 0;
			check[now] = 1;
			prev = now;
		}
		c += flag;
	}
	printf("%d", c);
}
