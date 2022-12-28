/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-12-19 10:32:02
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-12-19 11:59:21
 * @Descripttion: 
 */
package quick_sort;

public class sortColorsSolution {

    public void sortColors(int[] nums) {
        int n = nums.length;
        int p0 = 0, p1 = 0;
        for (int i = 0; i < n; ++i) {
            if (nums[i] == 1) {
                int temp = nums[i];
                nums[i] = nums[p1];
                nums[p1] = temp;
                ++p1;
            } else if (nums[i] == 0) {
                int temp = nums[i];
                nums[i] = nums[p0];
                nums[p0] = temp;
                if (p0 < p1) {
                    temp = nums[i];
                    nums[i] = nums[p1];
                    nums[p1] = temp;
                }
                ++p0;
                ++p1;
            }
        }
    }

    // // 双指针
    // public void sortColors(int[] nums) {
    // int len = nums.length;
    // int left = 0, right = len - 1;
    // for (int i = 0; i < len; i++) {
    // if (i >= left && nums[i] == 0) {
    // nums[i] = nums[left];
    // nums[left] = 0;
    // left++;
    // }
    // if (i <= right && nums[i] == 2) {
    // nums[i] = nums[right];
    // nums[right] = 2;
    // right--;
    // if (nums[i] != 1)
    // --i;
    // }
    // }
    // }

    // public void sortColors(int[] nums) {
    // quickSort(nums, 0, nums.length - 1);
    // }

    // public int partition(int[] nums, int left, int right) {
    // int pivot = (int) (Math.random() * (right - left + 1)) + left;
    // swap(nums, pivot, right);
    // int head = left;
    // for (int i = left; i < right; i++) {
    // if (nums[i] < nums[right]) {
    // swap(nums, i, head);
    // head += 1;
    // }
    // }
    // swap(nums, head, right);
    // return head;
    // }

    // public void quickSort(int[] nums, int left, int right) {
    // if (left >= right) {
    // return;
    // }
    // int pivot = partition(nums, left, right);
    // quickSort(nums, left, pivot - 1);
    // quickSort(nums, pivot + 1, right);
    // }

    // public void swap(int[] nums, int first, int second) {
    // int temp = nums[first];
    // nums[first] = nums[second];
    // nums[second] = temp;
    // }

    public static void main(String[] args) {
        int[] nums = { 2, 0, 2, 1, 1, 0 };
        sortColorsSolution solution = new sortColorsSolution();
        solution.sortColors(nums);
        System.out.println(nums);
        for (int num : nums) {
            System.out.println(num);
        }
    }
}
