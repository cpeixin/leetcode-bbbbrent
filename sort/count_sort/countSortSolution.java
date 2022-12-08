/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-12-04 21:02:50
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-12-04 22:05:07
 * @Descripttion: 
 * 计数排序的基本思想是先统计数组中每个整数在数组中出现的次数，然后按照从小到大的顺序将每个整数按照它出现的次数填到数组中。
 * 例如，如果输入整数数组[2，3，4，2，3，2，1]，扫描一次整个数组就能知道数组中1出现了1次，2出现了3次，3出现了2次，4出现了1次，
 * 于是先后在数组中填入1个1、3个2、2个3及1个4，就可以得到排序后的数组[1，2，2，2，3，3，4]。
 */
package count_sort;

public class countSortSolution {
    public int[] sort(int[] array) {
        // 借用最大值和最小值来实现下标对应
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        for (int num : array) {
            min = Math.min(min, num);
            max = Math.max(max, num);
        }

        // 统计array每个数字出现的次数
        int[] counts = new int[max - min + 1];
        for (int num : array) {
            counts[num - min] += 1;
        }

        // 数组填数
        int i = 0;
        for (int num = min; num < max; num++) {
            while (counts[num - min] > 0) {
                array[i++] = num;
                counts[num - min] -= 1;
            }
        }

        return array;
    }

    public static void main(String[] args) {
        int[] demo = { 2, 3, 4, 2, 3, 2, 1 };
        countSortSolution solution = new countSortSolution();
        int[] res = solution.sort(demo);
        System.out.println(res);
    }
}
