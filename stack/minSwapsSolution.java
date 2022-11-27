/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-11-25 10:49:16
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-11-25 10:50:46
 * @Descripttion: 
 */
public class minSwapsSolution {
    public int minSwaps(String s) {
        int cnt = 0;
        for (char c : s.toCharArray()) {
            if (c == ']') {
                if (cnt > 0) {
                    cnt--;
                }
            } else {
                cnt++;
            }
        }
        return cnt % 2 + cnt / 2;
    }

    public static void main(String[] args) {
        String demo = "]]][[[";
        minSwapsSolution solution = new minSwapsSolution();

        int res = solution.minSwaps(demo);
        // System.out.println(res);
        System.out.println(res);
    }
}
