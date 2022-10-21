#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct NODE {
	char val;
	int freq;
	struct NODE* left;
	struct NODE* right;
}node;

char* getFrequency(const char* str);
char* huffmanEncoding(const char* str, node* map);
char* huffmanDecoding(const char* str, node* map);

void preOrder(node* Node) {
	if (Node != NULL) {
		printf("[%c%c%c]", Node->left!=NULL?'o':'x',Node->val?Node->val:' ', Node->right != NULL ? 'o' : 'x');
		preOrder(Node->left);
		preOrder(Node->right);
	}
}

int main() {
	char sample1[] = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.";
	char sample2[] = "I am free today.";
	char sample3[] = "aBcDeFgHIjK";
	printf("기존 텍스트 길이 : %d\n", strlen(sample3));

	node* root = getFrequency(sample3);
}

char* huffmanEncoding(const char* str, node* map) {
	char* ch;
	ch = str;
}

char* huffmanDecoding(const char* str, node* map);

char* getFrequency(const char* str) {
	node** table = malloc(sizeof(node*) * 27);
	node** heap = malloc(sizeof(node*) * (27+1));
	int size = 0;
	char* ch;
	ch = str;

	//table 초기화
	for (int i = 0; i < 27; i++) {
		node* newNode = malloc(sizeof(node));
		if (i == 26) {
			newNode->val = ' ';
		}
		else {
			newNode->val = ('A' + i);
		}
		newNode->freq = 0;
		newNode->left = NULL;
		newNode->right = NULL;
		table[i] = newNode;
	}

	//빈도수 계산
	while (*ch != '\0') {
		if ((*ch >= 'A' && *ch <= 'Z') || (*ch >= 'a' && *ch <= 'z')) {
			//printf("%2d ", ((*ch) & (~('a' - 'A'))) - 'A');
			table[((*ch) & (~('a' - 'A'))) - 'A']->freq += 1;
		}
		else {
			table[26]->freq += 1;
		}
		ch++;
	}

	//insert heap
	int tmpIdx;
	node* tmpNode;
	for (int i = 0; i < 27; i++) {
		if (table[i]->freq != 0) {
			tmpIdx = size + 1;
			heap[tmpIdx]=table[i];
			while (tmpIdx > 1 && (heap[tmpIdx / 2]->freq < heap[tmpIdx]->freq)) {
				tmpNode = heap[tmpIdx / 2];
				heap[tmpIdx / 2] = heap[tmpIdx];
				heap[tmpIdx] = tmpNode;
				tmpIdx /= 2;
			}
			size++;
		}
	}

	//코드 트리 구성
	while (size > 1) {
		node* newNode = malloc(sizeof(node));
		size -= 1;
		newNode->val = 0;
		newNode->freq = heap[size]->freq + heap[size + 1]->freq;
		newNode->left = heap[size];
		newNode->right = heap[size + 1];
		heap[size] = newNode;

		tmpIdx = size;
		while (tmpIdx > 1 && (heap[tmpIdx / 2]->freq < heap[tmpIdx]->freq)) {
			tmpNode = heap[tmpIdx / 2];
			heap[tmpIdx / 2] = heap[tmpIdx];
			heap[tmpIdx] = tmpNode;
			tmpIdx /= 2;
		}
	}

	//for (int i = 0; i < 27; i++) {
	//	printf("%d : %c[%2d]\n", i, table[i]->val, table[i]->freq);
	//}
	//preOrder(heap[1]);
	return heap[1];
}
