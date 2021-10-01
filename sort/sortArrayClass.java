// 给你一个整数数组 nums，请你将该数组升序排列。 选择排序会超时
public class sortArrayClass {
    public int[] sortArray(int[] nums) {
        for(int i=0; i < nums.length; i++){
            int min = i;
            for(int j=i; j<nums.length; j++){
                if(nums[min] > nums[j]){
                    min = j;
                }
            }
            swap(nums, i, min);
        }
        return nums;
    }

    public void swap(int[] nums, int a, int b){
        int tmp = nums[a];
        nums[a] = nums[b];
        nums[b] = tmp;
    }

    public static void main(String[] args) {
        int[] nums = {5,2,3,1};
        int[] res = new sortArrayClass().sortArray(nums);
        System.out.println(res);
    }
}
