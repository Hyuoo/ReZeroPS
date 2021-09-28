#https://www.acmicpc.net/problem/1157

int main() {
    int c;
    int m=0,i=-1;
    int a[26]={0,};
    while((c=getchar())!=i)a[(c|32)-'a']++;
    for(c=0;c<26;c++)m=a[c]>m?a[c]:m;
    for(c=0;c<26;c++)i=a[c]==m?i==-1?c:-2:i;
    putchar('A'+i);
}
