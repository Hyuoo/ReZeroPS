#typedef SIZE 10000
#include <math.h>
a[SIZE]={0,1};i,j;
main(){
  for(i=2;i<=sqrt(SIZE);i++)if(!a[i])for(j=i*i;j<=SIZE;j+=i)a[j]=1;
}
