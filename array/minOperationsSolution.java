/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-12-11 09:57:01
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-12-11 10:05:59
 * @Descripttion: 
 */
public class minOperationsSolution {
    public int minOperations(int[] nums) {
        // 特例
        if (nums.length == 1) {
            return 0;
        }

        int slow = 0;
        int fast = 1;
        int operations = 0;
        while (fast < nums.length) {
            if (nums[slow] >= nums[fast]) {
                operations += nums[slow] - nums[fast] + 1;
                nums[fast] = nums[slow] + 1;
            }
            slow += 1;
            fast += 1;
        }
        return operations;
    }

    public static void main(String[] args) {
        int[] array = { 1, 1, 1 };
        minOperationsSolution solution = new minOperationsSolution();
        int res = solution.minOperations(array);
        System.out.println(res);
    }
}
