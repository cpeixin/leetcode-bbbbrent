/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-12-07 21:20:52
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-12-13 21:54:21
 * @Descripttion: 
 * https://labuladong.oschina.io/algo/2/21/45/
 * 
 * 
 * 
 * 看看JDK里面的快排
 */
package quick_sort;

import java.util.Random;

public class quickSortSolution {

    public int[] quick(int[] nums) {
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
        int pivot = partition_random(nums, left, right);
        // int pivot = partition(nums, left, right);
        quickSort(nums, left, pivot - 1);
        quickSort(nums, pivot + 1, right);
    }

    public static void main(String[] args) {
        int[] array = { 2, 1 };
        quickSortSolution solution = new quickSortSolution();
        int[] res = solution.quick(array);
        for (int num : res) {
            System.out.println(num);
        }
        System.out.println(res);
    }
}
