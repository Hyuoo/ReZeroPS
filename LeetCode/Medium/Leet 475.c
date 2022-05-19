int abs(int n){
    return n>0?n:~n+1;
}
int cmp(int* a, int* b){
    return *a-*b;
}
int findRadius(int* houses, int housesSize, int* heaters, int heatersSize){
    int i,j;
    int left, right, min, max;
    
    qsort(houses, housesSize, sizeof(int), cmp);
    qsort(heaters, heatersSize, sizeof(int), cmp);
    left = right = heaters[0];
    
    for(max=i=j=0;i<housesSize;i++){
        while(houses[i]>right && j+1 < heatersSize){
            left = right;
            right = heaters[++j];
        }
        min = abs(houses[i]-left) < abs(houses[i]-right) ? abs(houses[i]-left) : abs(houses[i]-right);
        max = max>min?max:min;
    }
    return max;
}
