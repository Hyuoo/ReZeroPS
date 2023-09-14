//아니 이거 왜안풀림ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ
//
#include <string.h>
#define check(p) ((p[0]>='A' && p[0]<='H') && (p[1]>='1' && p[1]<='8'))
char* moveTo(char* pos, char* mov) {
	char* n = malloc(3);
	memcpy(n, pos, 3);
	n[mov[0] == 'T' || mov[0] == 'B' ? 1 : 0] += mov[0] == 'T' || mov[0] == 'R' ? 1 : -1;
	if (mov[1] == 'T' || mov[1] == 'B') n[1] += mov[1] == 'T' ? 1 : -1;
	return n;
}
main(){
	char K[3], S[3], N, Ktmp[3], Stmp[3];
	char ch[4];
	scanf("%s%s%d ", K, S, &N);
	while (N--) {
		scanf("%s", ch);
		memcpy(Ktmp, moveTo(K, ch), 3);
		memcpy(Stmp, moveTo(S, ch), 3);
		if (check(Ktmp) && memcmp(Ktmp, S, 3))
			memcpy(K, Ktmp, 3);
		else if (!memcmp(Ktmp, S, 3) && check(Stmp)) {
			memcpy(K, Ktmp, 3);
			memcpy(S, Stmp, 3);
		}
	}
	printf("%s\n%s", K, S);
}
