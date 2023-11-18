int main(){
  int h, m, mm;
	scanf("%d %d\n%d", &h, &m, &mm);
	printf("%d %d", (h+(mm/60)+(m+(mm%60))/60)%24, (m+(mm%60))%60);
}
