/*
 * @version: 
 * @Author: Brent
 * @Date: 2020-11-21 11:04:58
 * @LastEditors: congpeixin congpeixin@dongqiudi.com
 * @LastEditTime: 2022-11-05 21:48:38
 * @Descripttion: 
 * 输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。要求时间复杂度为O(n)。
 */

class Solution {

    public static int max3(int num1, int num2, int num3) {
        return Math.max(num1, Math.max(num2, num3));
    }
    public int maxSubArray(int[] nums) {

        return maxSumRec(nums, 0, nums.length-1);

    }

    public static int maxSumRec(int[] a, int left, int right){
        if (left < right)
            if (a[left] > 0)
                return a[left];
            else
                return 0;
        
        int center = (left + right) / 2;
        int maxLeftSum = maxSumRec(a, left, center);
        int maxRightSum = maxSumRec(a, center + 1, right);

        int maxLeftBorderSum = 0, leftBorderSum = 0;
        for(int i = center; i >= left; i--){
            leftBorderSum += a[i];
            if (leftBorderSum > maxLeftSum)
                maxLeftBorderSum = leftBorderSum;
        }

        int maxRightBorderSum =0, rightBorderSum = 0;
        for(int i = center + 1; i <= right; i++){
            rightBorderSum += a[i];
            if (rightBorderSum > maxRightSum)
                maxRightBorderSum = rightBorderSum;
        }
        return max3(maxLeftSum, maxRightSum, maxRightBorderSum+maxLeftBorderSum);
    }
}