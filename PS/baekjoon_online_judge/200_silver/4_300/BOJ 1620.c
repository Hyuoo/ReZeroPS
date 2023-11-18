#include <stdio.h>
#include <stdlib.h>
//Trie 구조 모르고 일단 한번 만들어봄
typedef struct NODE {
	int number;
	char alpha;
	struct NODE *link;
	struct NODE *down;
}node;

int main() {
	int N, M, n, i, j;
	scanf("%d%d ",&N,&M);
	char **dict, *popopopo;
	node *trie, *ttmp;

	trie = malloc(sizeof(node));
	trie->number = 0;
	trie->alpha = 0;
	trie->link = NULL;
	trie->down = NULL;

	//생성
	dict = malloc(sizeof(char*)*N);
	for (i = 0; i < N; i ++) {
		popopopo = malloc(sizeof(char) * 21);
		scanf("%s ", popopopo);
		dict[i] = popopopo;
		ttmp = trie;
		while (*popopopo) {
			if (ttmp->down != NULL) {
				ttmp = ttmp->down;
			}
			while (ttmp->link != NULL && ttmp->alpha != *popopopo) {
				ttmp = ttmp->link;
			}
			if (ttmp->link == NULL && ttmp->alpha != *popopopo) {
				node *newNode = malloc(sizeof(node));
				node *dummy = malloc(sizeof(node));
				newNode->alpha = *popopopo;
				newNode->number = 0;
				newNode->link = NULL;
				newNode->down = dummy;
				dummy->alpha = 0;
				dummy->number = 0;
				dummy->link = NULL;
				dummy->down = NULL;
				ttmp->link = newNode;
				ttmp = newNode;
			}
			popopopo++;
		}
		ttmp->number = i+1;
	}

	//탐색
	popopopo = malloc(sizeof(char) * 21);
	char *ptmp;
	while (M--) {
		scanf("%s ", popopopo);
		ptmp = popopopo;
		N = 1;
		if (ptmp[0] >= '0' && ptmp[0] <= '9') {
			n = atoi(ptmp)-1;
			N = 0;
		}
		if (N) {//문자
			ttmp = trie;
			while (*ptmp) {
				if (ttmp->down != NULL)
					ttmp = ttmp->down;
				while (ttmp->alpha != *ptmp) {
					ttmp = ttmp->link;
				}
				ptmp++;
			}
			printf("%d\n", ttmp->number);
		}
		else {
			printf("%s\n", dict[n]);
		}
	}
}
