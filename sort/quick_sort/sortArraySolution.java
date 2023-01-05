/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-12-10 08:43:42
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-12-10 20:44:39
 * @Descripttion: 
 */
package quick_sort;

import java.util.Arrays;
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
 * 此题正常的快排写法不能通过，而是起码需要对分区函数做随机化。
 * 
 * 
 */
public class sortArraySolution {
    public int[] sortArray(int[] nums) {
        quickSort(nums, 0, nums.length - 1);
        return nums;
    }

    public void swap(int[] nums, int a, int b) {
        int temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;
    }

    public int partition_middle(int[] nums, int left, int right) {
        int pivot_index = (right + left) / 2;
        int pivot_value = nums[pivot_index];
        // 将随机选出的主元交换到数组最右端
        swap(nums, pivot_index, right);

        int head = left;

        // 遍历+小于nums[pivot_index]放在pivot_index左侧，大于nums[pivot_index]的放在右侧
        for (int i = left; i < right; i++) {
            if (nums[i] <= pivot_value) {
                swap(nums, head, i);
                head++;
            }
        }
        nums[right] = nums[head];
        nums[head] = pivot_value;
        return head;
    }

<<<<<<< HEAD
 */
public class sortArraySolution {
    public int[] sortArray(int[] nums) {
        Arrays.sort(nums);
        return nums;
=======
    public int partition_random(int[] nums, int left, int right) {
        int pivot_index = new Random().nextInt(right - left) + left;
        int pivot_value = nums[pivot_index];
        // 将随机选出的主元交换到数组最右端
        swap(nums, pivot_index, right);

        int head = left;

        // 遍历+小于nums[pivot_index]放在pivot_index左侧，大于nums[pivot_index]的放在右侧
        for (int i = left; i < right; i++) {
            if (nums[i] <= pivot_value) {
                swap(nums, head, i);
                head++;
            }
        }
        nums[right] = nums[head];
        nums[head] = pivot_value;
        return head;
    }

    public int partition(int[] nums, int left, int right) {
        int pivot_value = nums[right];

        int head = left;

        // 遍历+小于nums[pivot_index]放在pivot_index左侧，大于nums[pivot_index]的放在右侧
        for (int i = left; i < right; i++) {
            if (nums[i] <= pivot_value) {
                swap(nums, head, i);
                head++;
            }
        }
        swap(nums, head, right);
        return head;
    }

    public void quickSort(int[] nums, int left, int right) {
        // 递归终止条件
        if (left >= right) {
            return;
        }
        int pivot = partition_middle(nums, left, right);
        // int pivot = partition(nums, left, right);
        quickSort(nums, left, pivot - 1);
        quickSort(nums, pivot + 1, right);
>>>>>>> 6d806b042276bfd829ab2c3470788a5193bdccd1
    }

    public static void main(String[] args) {
        int[] array = { 5, 2, 3, 1 };
        sortArraySolution solution = new sortArraySolution();
        int[] res = solution.sortArray(array);
        for (int num : res) {
            System.out.println(num);
        }
        System.out.println(res);
        Arrays.sort(res);
    }
}
