/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-12-16 09:03:57
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-12-16 09:32:56
 * @Descripttion: 
 */
package everyday_one_leco;

public class minElementsSolution {
    public int minElements(int[] nums, int limit, int goal) {
        long sum = 0;
        for (int x : nums) {
            sum += x;
        }
        long diff = Math.abs(sum - goal);
        return (int) ((diff + limit - 1) / limit);
    }

    public static void main(String[] args) {
        int[] nums = { 1, -1, 1 };
        int limit = 3;
        int goal = -4;
        minElementsSolution solution = new minElementsSolution();
        int res = solution.minElements(nums, limit, goal);
        System.out.println(res);
    }
}
