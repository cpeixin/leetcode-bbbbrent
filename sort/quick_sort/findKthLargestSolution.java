/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-12-12 22:20:34
 * @LastEditors: 
 * @LastEditTime: 2022-12-12 22:20:47
 * @Descripttion: 
 */
package quick_sort;

import java.util.Random;

/**
 * 数组中的第K个最大元素
 * 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k
 * 个不同的元素。你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。
 * 
 * 示例 1:
 * 输入: [3,2,1,5,6,4], k = 2
 * 输出: 5
 * 
 * 示例 2:
 * 输入: [3,2,3,1,2,4,5,5,6], k = 4
 * 输出: 4
 * 
 */
public class findKthLargestSolution {
    public int findKthLargest(int[] nums, int k) {
        // 特例判断
        if(nums.length==1){
            return nums[0];
        }
        int res = quickSort(nums, 0, nums.length-1, nums.length-k);
        return res;
    }

    public int partition(int[] nums, int left, int right, int k){
        int pivot_index = new Random().nextInt(right-left)+left;
        swap(nums, pivot_index, right);

        int head = left;
        for(int i=left; i<right; i++){
            if(nums[i]<=nums[right]){
                swap(nums, i, head);
                head += 1;
            }
        }
        swap(nums, head, right);
        return head;   
    }


    public int quickSort(int[] nums, int left, int right, int k){
        int pivot = partition(nums, left, right, k);
        if(pivot==k){
            return nums[pivot];
        }else if(pivot<k){
            return quickSort(nums, pivot+1, right, k);
        }else{
            return quickSort(nums, left, pivot-1, k);
        }
    }

    public void swap(int[] nums, int first, int second){
        int temp = nums[first];
        nums[first] = nums[second];
        nums[second] = temp;
    }

    public static void main(String[] args) {
        int[] nums = {2,1};
        findKthLargestSolution solution = new findKthLargestSolution();
        int res = solution.findKthLargest(nums, 2);
        System.out.println(res);
    }
}
