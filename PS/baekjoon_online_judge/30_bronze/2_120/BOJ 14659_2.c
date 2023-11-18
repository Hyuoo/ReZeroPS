////기존코드 1352KB/1164ms -> 1116KB/4ms 개선
int main() {
    int i,h=0,c=0,a=0;//input, high, count, answer
    for (gets(&i);~scanf("%d",&i);a=c<a?a:c)
        h<i?c=0,h=i:c++;
    printf("%d", a);
}
