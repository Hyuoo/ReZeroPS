int main() {
	/*
	목표 : arr 모든 값 똑같이 만들기
	-=1 cost 2
	+=1 cost 1 need B1
	*/
	int N, M, B, tmp;
	int h, i, b, cnt;
	int best_h=256, best_cnt=2000000000;
	short *arr;
	scanf("%d%d%d", &N, &M, &B);
	arr = malloc(sizeof(short*)*N*M);

	for (i = 0; i < N*M; i++) {
		scanf("%d", &tmp);
		arr[i] = tmp;
	}
	h = 0;
	for (i = 0; i < N*M; i++) {
		h = h > arr[i] ? h : arr[i];
	}
	
	while (h >= 0) {
		b = B;
		for (cnt = i = 0; i < N*M; i++) {
			if (arr[i] > h) {
				tmp = arr[i] - h;
				b += tmp;
				cnt += tmp*2;
			}
			else {
				tmp = h - arr[i];
				cnt += tmp;
				b -= tmp;
			}
		}
		if (cnt <= best_cnt && b>=0) {
			if(cnt!=best_cnt)
				best_h = h;
			best_cnt = cnt;
		}
		h--;
	}
	printf("%d %d", best_cnt, best_h);
}
