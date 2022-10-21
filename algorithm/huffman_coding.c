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
void asdf(const char* sample);

int main() {
	char sample1[] = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.";
	char sample2[] = "I am free today.";
	char sample3[] = "aBcDeFgHIjK";
	
	asdf(sample1);
	asdf(sample2);
	asdf(sample3);
}

void asdf(const char* sample) {
	node* root;
	char* code;
	char* originText;

	printf("--------------------------\n");
	printf("원래 문자열 : %s\n", sample);
	printf("기존 텍스트 길이 : %d\n", strlen(sample));

	root = getFrequency(sample);
	code = huffmanEncoding(sample, root);
	printf("CODE : %s\n", code);

	originText = huffmanDecoding(code, root);
	printf("ORIGIN : %s\n", originText);
	printf("--------------------------\n");
	free(root);
	free(code);
	free(originText);
}

void getCode(node* Node, char code, char depth, char table[27][2]) {
	if (Node != NULL) {
		if (Node->val != 0) {
			if (Node->val == ' ') {
				table[26][0] = code;
				table[26][1] = depth;
			}
			else {
				table[Node->val - 'A'][0] = code;
				table[Node->val - 'A'][1] = depth;
			}
		}
		else {
			if (Node->left != NULL) {
				getCode(Node->left, code, depth + 1, table);
			}
			if (Node->right != NULL) {
				getCode(Node->right, code | (1 << depth), depth + 1, table);
			}
		}
	}
}

char* huffmanEncoding(const char* str, node* map) {
	//8개 비트, char형으로 경로 설정.
	char table[27][2] = { 0, };
	//[0]code [1]depth
	getCode(map, 0, 0, table);
	//코드 확인용
	//for (int i = 0; i < 27; i++) {
	//	printf("[%c : %d_%d]\n", i+'A', table[i][0],table[i][1]);
	//}
	char* encoded = malloc(sizeof(char)*2000);
	int size = 0;
	
	char* ch;
	char tmp;
	ch = str;
	//01문자열로 만들기
	while (*ch != '\0') {
		tmp = *ch==' '?26:((*ch) & (~('a' - 'A'))) - 'A';
		for (int i = 0; i < table[tmp][1]; i++) {
			encoded[size++] = table[tmp][0] & (1 << i) ? '1' : '0';
		}
		ch++;
	}
	encoded[size] = '\0';
	return encoded;
}

char* huffmanDecoding(const char* str, node* map) {
	node* tmp;
	char* ch;
	char* string = malloc(sizeof(char) * 100);
	int size = 0;
	
	tmp = map;
	ch = str;

	while (*ch != '\0') {
		if(*ch=='0'){
			tmp = tmp->left;
		}
		else {
			tmp = tmp->right;
		}
		if (tmp->val) {
			//printf("%c", tmp->val);
			string[size++] = tmp->val;
			tmp = map;
		}
		ch++;
	}
	string[size] = '\0';

	return string;
}

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
