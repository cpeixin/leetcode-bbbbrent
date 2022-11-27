import java.util.ArrayDeque;
import java.util.Deque;
import java.util.LinkedList;

/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-11-26 16:54:12
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-11-26 18:50:28
 * @Descripttion: 
 */
public class longestValidParenthesesSolution {
    public int longestValidParentheses(String s) {
        char[] chars = s.toCharArray();
        Deque<Integer> stack = new ArrayDeque<Integer>();
        int max = 0;
        int start = 0;
        for (int i = 0; i < chars.length; i++) {
            if (s.charAt(i) == '(') {
                stack.push(i);
            } else {
                if (stack.isEmpty()) {
                    start = i + 1;
                } else {
                    stack.pop();
                    if (stack.isEmpty()) {
                        max = Math.max(max, i - start + 1);
                    } else {
                        max = Math.max(max, i - stack.peek());
                    }
                }
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
