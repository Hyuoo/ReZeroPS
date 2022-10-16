int main() {
	int n, m, a;
	scanf("%d %d", &n, &m);
	switch (n) {
	case 1: a = 1; break;
	case 2: a = (m + 1) / 2; a = a < 4 ? a : 4; break;
	default:
		if (m < 7) a = m < 4 ? m : 4;
		else a = m - 2;
	}
	printf("%d", a);
}
