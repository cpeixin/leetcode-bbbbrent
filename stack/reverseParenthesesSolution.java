import java.util.ArrayDeque;
import java.util.Deque;

/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-11-24 22:26:32
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-11-24 22:28:45
 * @Descripttion: 
 */
public class reverseParenthesesSolution {
    public String reverseParentheses(String s) {
        Deque<String> stack = new ArrayDeque<String>();
        StringBuilder sb = new StringBuilder();
        for (char w : s.toCharArray()) {
            if (w == '(') {
                stack.push(sb.toString());
                sb = new StringBuilder();
            } else if (w == ')') {
                sb = new StringBuilder(stack.pop() + sb.reverse());
            } else {
                sb.append(w);
            }
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        String demo = "(u(love)i)";
        reverseParenthesesSolution solution = new reverseParenthesesSolution();

        String res = solution.reverseParentheses(demo);
        // System.out.println(res);
        System.out.println(res);
    }
}
