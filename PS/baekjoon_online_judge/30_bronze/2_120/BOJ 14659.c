#include <stdio.h>
#include <stdlib.h>

int main() {
    int N,i;
    scanf("%d", &N);
    int* ar = malloc(sizeof(int)*N+1);
    for (int i = 0; i < N; i++)
        scanf("%d", ar + i);
    ar[N] = 100001;
    int* flag = calloc(sizeof(int), N+1);
    flag[N] = 1;
    int tmp;
    int count = 0;
    while (1) {
        count++;
        for (i = 0; i+count<=N ; i++) {
            if (!flag[i]&&(ar[i] <= ar[i + count])) {
                flag[i] = 1;
            }
        }
        for (i = 0, tmp=1; i < N; i++) {
            tmp *= flag[i];
        }
        if (tmp)
            break;
    }
    printf("%d", count-1);
}
