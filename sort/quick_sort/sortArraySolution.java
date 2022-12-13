package quick_sort;

import java.util.Arrays;
import java.util.Random;
/**
 * 912. 排序数组
给你一个整数数组 nums，请你将该数组升序排列。

示例 1：
输入：nums = [5,2,3,1]
输出：[1,2,3,5]

示例 2：
输入：nums = [5,1,1,2,0,0]
输出：[0,0,1,1,2,5]

此题正常的快排写法不能通过，而是起码需要对分区函数做随机化。


 */
public class sortArraySolution {
    public int[] sortArray(int[] nums) {
        Arrays.sort(nums);
        return nums;
    }

    public static void main(String[] args) {
        int a = new Random().nextInt(10);
        System.out.println(a);
    }
}
