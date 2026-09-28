class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        
        int [] copy = new int [1001];
        int [] result = new int [1001];
        int k= 0;

        for (int num: nums1){
            copy[num] ++;
        }
        for (int num : nums2){
            if (copy[num] > 0 ){
                result[k++] = num;
                copy[num]--;
            }
        }

        return Arrays.copyOf(result,k);
}
}