
/*
 * @version: 
 * @Author: Brent
 * @Date: 2020-12-05 12:07:32
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2020-12-05 12:37:21
 * @Descripttion: 给定一个整数类型的数组 nums，请编写一个能够返回数组 “中心索引” 的方法。

我们是这样定义数组 中心索引 的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和。

如果数组不存在中心索引，那么我们应该返回 -1。如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个。

 

示例 1：

输入：
nums = [1, 7, 3, 6, 5, 6]
输出：3
解释：
索引 3 (nums[3] = 6) 的左侧数之和 (1 + 7 + 3 = 11)，与右侧数之和 (5 + 6 = 11) 相等。
同时, 3 也是第一个符合要求的中心索引。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-pivot-index
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 */

public class mid_index {
    public int pivotIndex(int[] nums) {
        if (nums.length == 0)
            return -1; 
        int sum = 0, left_sum = 0;
        for (int x: nums) {sum += x;}
        for (int i = 0; i < nums.length; i++){
            if(left_sum == sum - nums[i] - left_sum){return i;}
            left_sum += nums[i];
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] nums = {1,2, 3};
        int index = new mid_index().pivotIndex(nums);
        System.out.println(index);
    }
}
