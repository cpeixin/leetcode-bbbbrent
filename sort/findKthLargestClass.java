public class findKthLargestClass {

    public int findKthLargest(int[] nums, int k) {
        for (int i=0;i<nums.length;i++){
            int minIndex = i;
            for (int j=i+1; j<nums.length; j++){
                if (nums[minIndex] > nums[j]){
                    minIndex = j;
                }
            }
            swap(nums, i, minIndex);
        }
        return nums[nums.length-k];
    }

    public void swap(int[] nums, int a, int b){
        // nums[a] = nums[a] ^ nums[b];
        // nums[b] = nums[b] ^ nums[a];
        // nums[a] = nums[a] ^ nums[b];
        int tmp = nums[a];
        nums[a] = nums[b];
        nums[b] = tmp;
    }

    public static void main(String[] args) {
        int[] nums = {3,2,3,1,2,4,5,5,6};
        int res = new findKthLargestClass().findKthLargest(nums, 4);
        System.out.println(res);
    }
}