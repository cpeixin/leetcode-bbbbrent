import java.util.ArrayDeque;
import java.util.Deque;

/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-11-17 22:17:00
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-11-17 22:22:27
 * @Descripttion: 
 */
public class scoreOfParenthesesSolution {
    public int scoreOfParentheses(String s) {
        Deque<Integer> st = new ArrayDeque<Integer>();
        st.push(0);
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                st.push(0);
            } else {
                int v = st.pop();
                int top = st.pop() + Math.max(2 * v, 1);
                st.push(top);
            }
        }
        return st.peek();
    }

    public static void main(String[] args) {
        String demo = "(()(()))";
        scoreOfParenthesesSolution solution = new scoreOfParenthesesSolution();

        int res = solution.scoreOfParentheses(demo);
        // System.out.println(res);
        System.out.println(res);
    }
}
