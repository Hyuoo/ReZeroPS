#include <stdio.h>
#include <string.h>
int main() {
    char str[101];
    char* alph[] = { "c=","c-","dz=","d-","lj","nj","s=","z=" };
    int count=0;
    fgets(str, 101, stdin);
    if(str[strlen(str) - 1] == '\n')
        str[strlen(str)-1]=0;
    for (int i = 0; i < strlen(str); i++) {
        count++;
        for (int j = 0; j < sizeof(alph) / sizeof(char*); j++) {
            if(strncmp(str+i,alph[j],strlen(alph[j]))==0)
                i+=strlen(alph[j])-1;
        }
    }
    printf("%d",count);
}
