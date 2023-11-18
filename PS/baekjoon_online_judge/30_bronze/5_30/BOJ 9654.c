#include <stdio.h>

int main() {
  char str[] = "SHIP NAME!CLASS!DEPLOYMENT!IN SERVICE!N2 Bomber!Heavy Fighter!Limited!21!J-Type 327!Light Combat!Unlimited!1!NX Cruiser!Medium Fighter!Limited!18!N1 Starfighter!Medium Fighter!Unlimited!25!Royal Cruiser!Light Combat!Limited!4!";
  char* cp = str;
  char length[] = {15,15,11,10};
  char i=0, len=0;
  while(*cp!=0){
    if(*cp=='!'){for(;i<length[len%4];i++)putchar(32);len++;i=0;if(!(len%4))puts("");}
    else{putchar(*cp);i++;}
    cp++;
  }
}
  
