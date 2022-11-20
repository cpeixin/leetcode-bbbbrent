import java.util.ArrayDeque;
import java.util.Deque;

/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-11-19 16:07:02
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-11-19 17:17:06
 * @Descripttion: 
 * 
 *     // 题解：首先题目保证所给的字符串为有效字符串
    // 观察有效字符串，所以不用考虑字符串构成的细节问题，可以跳过其他字符。
    // 错误想法：最大嵌套深度其实就是连续遇到右括号的个数
    // 遍历字符串 s，如果遇到了一个左括号，那么就将其入栈；如果遇到了一个右括号，那么就弹出栈顶的左括号，与该右括号匹配。这一过程中的栈的大小的最大值，即为 s 的嵌套深度
    // 实践：代码的实现过程中，发现其实利用栈的思想就可以，不用具体的实现栈和入栈出栈的操作。只维护一栈最大深度变量即可

 */
public class maxDepthSolution {

    public int maxDepth(String s) {
        // 特例判断
        if (s.length() == 0)
            return 0;

        int max_depth = 0;
        int depth = 0;
        for (Character c : s.toCharArray()) {
            if (c == '(') {
                depth += 1;
                max_depth = Math.max(max_depth, depth);
            } else if (c == ')') {
                depth -= 1;
            }
        }
        return max_depth;
    }

    public static void main(String[] args) {
        String demo = "8*((1*(5+6))*(8/6))";
        maxDepthSolution solution = new maxDepthSolution();
        int res = solution.maxDepth(demo);
        System.out.println(res);
    }
}
