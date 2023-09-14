int find(int* p, int a){
	if (p[a] == a) { return a; }
	return p[a]=find(p, p[a]);
}
main(){
	int p[101];
	int n, m, i, j;
	scanf("%d\n%d", &n, &m);
	for (i = 0; i <= n; i++) {
		p[i] = i;
	}
	while (m--) {
		scanf("%d%d", &i, &j);
		i = find(p, i);
		j = find(p, j);
		if (i < j) {
			p[j] = i;
		}else{
			p[i] = j;
		}
	}
	for (j = 0, i =2; i <= n; i++) {
		if (find(p,i) == 1)j++;
	}
	printf("%d", j);
}
