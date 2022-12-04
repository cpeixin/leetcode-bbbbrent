import java.util.ArrayDeque;
import java.util.Deque;

/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-11-09 21:01:36
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-12-03 22:22:41
 * @Descripttion: 
 */
public class evalRPNSolution {
    public int evalRPN(String[] tokens) {
        Deque<Integer> stack = new ArrayDeque<Integer>();
        for (String s : tokens) {
            switch (s) {
                case "+":
                    stack.addLast(stack.pollLast() + stack.pollLast());
                    break;
                case "-":
                    int a = stack.pollLast();
                    int b = stack.pollLast();
                    stack.addLast(b - a);
                    break;
                case "*":
                    stack.addLast(stack.pollLast() * stack.pollLast());
                    break;
                case "/":
                    int c = stack.pollLast();
                    int d = stack.pollLast();
                    stack.addLast(d / c);
                    break;
                default:
                    stack.addLast(Integer.valueOf(s));
                    break;
            }
        }

        return stack.pollLast();
    }

    public static void main(String[] args) {
        // String demo = "(()))(()))()())))";
        String[] demo = new String[] { "4", "13", "5", "/", "+" };
        evalRPNSolution solution = new evalRPNSolution();
        int res = solution.evalRPN(demo);
        System.out.println(res);
    }

}
