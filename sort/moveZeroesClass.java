public class moveZeroesClass {
    public void moveZeroes(int[] nums) {

        int zeroIndex = 0;
        if (nums.length!=1){
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                swap(nums,i, zeroIndex);
                zeroIndex++;
            }
        }
    }
    }

    public void swap(int[] nums, int left, int right) {
        int temp = nums[left];
        nums[left] = nums[right];
        nums[right] = temp;
    }

    public static void main(String[] args) {

    }
}
