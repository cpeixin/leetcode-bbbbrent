/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-12-05 22:17:18
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-12-07 22:19:05
 * @Descripttion: 
 */
package count_sort;

public class heightCheckerSolutiuon {
    public int heightChecker(int[] heights) {
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;

        for (int num : heights) {
            min = Math.min(min, num);
            max = Math.max(max, num);
        }

        int[] counts = new int[max - min + 1];

        // 计数
        for (int num : heights) {
            counts[num - min]++;
        }

        // 排完序
        int i = 0;
        int ans = 0;
        for (int num = min; num <= max; num++) {
            while (counts[num - min] > 0) {
                if (heights[i++] != num) {
                    ans += 1;
                }
                counts[num - min] -= 1;
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        int[] arr1 = { 1, 1, 4, 2, 1, 3 };

        heightCheckerSolutiuon solution = new heightCheckerSolutiuon();
        int res = solution.heightChecker(arr1);
        System.out.println(res);
    }
}
