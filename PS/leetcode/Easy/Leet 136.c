int singleNumber(int* nums, int numsSize){
    int tmp=0;
    while(numsSize--)
        tmp^=nums[numsSize];
    return tmp;
}
