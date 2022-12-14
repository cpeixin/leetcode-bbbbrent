/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-12-10 08:43:42
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-12-10 21:27:22
 * @Descripttion: 
 */
package quick_sort;

import java.util.Random;

/**
 * 912. 排序数组
 * 给你一个整数数组 nums，请你将该数组升序排列。
 * 
 * 示例 1：
 * 输入：nums = [5,2,3,1]
 * 输出：[1,2,3,5]
 * 
 * 示例 2：
 * 输入：nums = [5,1,1,2,0,0]
 * 输出：[0,0,1,1,2,5]
 * 
 * 1 <= nums.length <= 5 * 104
 * -5 * 104 <= nums[i] <= 5 * 104
 * 
 * 利用这个范围，尝试计数排序
 */
public class sortArraySolution_Count {
    public int[] sortArray(int[] nums) {
        // 计算数组长度
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;

        for (int i = 0; i < nums.length; i++) {
            min = Math.min(min, nums[i]);
            max = Math.max(max, nums[i]);
        }

        int[] counts = new int[max - min + 1];

        // 计数
        for (int num : nums) {
            counts[num - min] += 1;
        }

        int j = 0;
        // 排序
        for (int i = min; i <= max; i++) {
            while (counts[i - min] > 0) {
                nums[j++] = i;
                counts[i - min] -= 1;
            }
        }

        return nums;

    }

    public static void main(String[] args) {
        int[] array = { 5, 2, 3, 1 };
        sortArraySolution_Count solution = new sortArraySolution_Count();
        int[] res = solution.sortArray(array);
        for (int num : res) {
            System.out.println(num);
        }
        System.out.println(res);
    }
}
