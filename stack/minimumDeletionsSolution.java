import java.util.ArrayDeque;
import java.util.Deque;

/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-11-30 22:03:23
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-11-30 22:27:41
 * @Descripttion: 给你一个字符串 s ，它仅包含字符 'a' 和 'b'​​​​ 。

你可以删除 s 中任意数目的字符，使得 s 平衡 。我们称 s 平衡的 当不存在下标对 (i,j) 满足 i < j 且 s[i] = 'b' 同时 s[j]= 'a' 。

请你返回使 s 平衡 的 最少 删除次数。

 

示例 1：

输入：s = "aababbab"
输出：2
解释：你可以选择以下任意一种方案：
下标从 0 开始，删除第 2 和第 6 个字符（"aababbab" -> "aaabbb"），
下标从 0 开始，删除第 3 和第 6 个字符（"aababbab" -> "aabbbb"）。
示例 2：

输入：s = "bbaaaaabb"
输出：2
解释：唯一的最优解是删除最前面两个字符。

核心思路：给a前面的b，全干掉！！！！
 */
public class minimumDeletionsSolution {
    public int minimumDeletions(String s) {
        char[] cs = s.toCharArray();
        int ans = 0, b = 0;
        for (int i = 0; i < cs.length; i++) {
            if (cs[i] == 'b') {
                b++;
            } else if (b > 0) {
                ans++;
                b--;
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        String demo = "aababbab";
        minimumDeletionsSolution solution = new minimumDeletionsSolution();

        int res = solution.minimumDeletions(demo);
        // System.out.println(res);
        System.out.println(res);
    }
}
