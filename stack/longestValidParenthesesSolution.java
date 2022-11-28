import java.util.ArrayDeque;
import java.util.Deque;
import java.util.LinkedList;

/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-11-26 16:54:12
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-11-28 22:18:32
 * @Descripttion: 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

 

示例 1：

输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"
示例 2：

输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"
示例 3：

输入：s = ""
输出：0

题解：遇到括号相关问题，大多数和栈相关，因为我现在在做【栈】专题，所以只写栈的解法

核心思路：
1. 遍历字符串
2. 匹配的字串弹出
3. 将未匹配上的括号的坐标存在栈中
4. 再次循环栈中未匹配括号之间的下标差，获取最大值。（这步调试了好久，面试手写的话，应该是废了）
 */
public class longestValidParenthesesSolution {
    public int longestValidParentheses(String s) {
        // 特例判断
        if (s.length() == 0)
            return 0;

        Deque<Integer> stack = new ArrayDeque<Integer>();
        for (int i = 0; i < s.length(); i++) {
            // 匹配上了
            if (s.charAt(i) == ')' && !stack.isEmpty() && s.charAt(stack.peekLast()) == '(') {
                stack.pollLast();
            } else {
                // 没匹配上的括号
                stack.addLast(i);
            }
        }

        int last_index = s.length();
        int max = 0;

        // 如果全部匹配完，没有多余未匹配的括号，则最大长度为字符串长度
        if (stack.isEmpty()) {
            max = last_index;
        }

        // 未匹配完
        while (!stack.isEmpty()) {
            // 栈中，最后一个未匹配括号下标
            int last_nomatch_index = stack.pollLast();
            // eg.()(()()
            max = Math.max(max, last_index - last_nomatch_index - 1);
            last_index = last_nomatch_index;
            // 这里是针对栈中只剩一个下标的时候
            if (stack.isEmpty()) {
                max = Math.max(max, last_index);
            }
        }
        return max;
    }

    public static void main(String[] args) {
        String demo = ")()())";
        longestValidParenthesesSolution solution = new longestValidParenthesesSolution();

        int res = solution.longestValidParentheses(demo);
        // System.out.println(res);
        System.out.println(res);
    }

}
