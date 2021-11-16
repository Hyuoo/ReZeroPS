#include <stdio.h>
#include <stdlib.h>
int main() {
	int n, s, tmp, m;
	unsigned int *h;
	int c;
	scanf("%d", &n);
	h = malloc(sizeof(unsigned int) * (n+1));
	h[0] = 0xFFFFFFFF;
	s = 0;
	while(n--){
		scanf("%d", &c);
		if(c){
			tmp = ++s;
			while(h[tmp/2] < c){
				h[tmp] = h[tmp/2];
				tmp /= 2;
			}
			h[tmp] = c;
		}
		else{
			if(s){
				printf("%d\n", h[1]);
				if(s-- > 1){
					tmp = 1;
					while(tmp * 2 <= s){
						m = tmp*2;
						if(tmp*2+1 <= s && h[tmp*2]<h[tmp*2+1]){
							m++;
						}
						if(h[m] > h[s+1]){
							h[tmp] = h[m];
							tmp = m;
						}else{
                            break;
                        }
					}
					h[tmp] = h[s+1];
				}
			}
			else{
				printf("0\n");
			}
		}
	}
}
