void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n){
    int* ans = malloc(sizeof(int)*(n+m));
    int i=0, j=0, k=0;
    while(i<m && j<n){
        if(nums1[i] <= nums2[j]){
            ans[k++] = nums1[i++];
        }else{
            ans[k++] = nums2[j++];
        }
    }
    while(i<m)
        ans[k++] = nums1[i++];
    while(j<n)
        ans[k++] = nums2[j++];
    memcpy(nums1, ans, sizeof(int)*nums1Size);
}
