import java.util.ArrayDeque;
import java.util.Deque;

/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-11-17 22:17:00
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-11-18 08:52:10
 * @Descripttion: 给定一个平衡括号字符串 S，按下述规则计算该字符串的分数：

() 得 1 分。
AB 得 A + B 分，其中 A 和 B 是平衡括号字符串。
(A) 得 2 * A 分，其中 A 是平衡括号字符串。
 

示例 1：
输入： "()"
输出： 1

示例 2：
输入： "(())"
输出： 2

示例 3：
输入： "()()"
输出： 2

示例 4：
输入： "(()(()))"
输出： 6
 * 
 * 
 * 
 * 
 * **关于0**
- 栈初始化添加0，起到了占位以及假象成整体字符串外面有一个空串的情况。如果不添加，（）情况下就会报错
- 遇到'('添加0,代表着（ 内部子串得分的占位，例如：(()(())) => (0(0)(0(0)))

**关于两次出栈**

第一次是当前括号内的总分数。第二次是当前括号外的、且同一层级（或者说在同一外层括号内）的、且已经计算过的总分数

 */
public class scoreOfParenthesesSolution {
    public int scoreOfParentheses(String s) {
        Deque<Integer> st = new ArrayDeque<Integer>();
        // st.push(0);
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
        String demo = "()";
        scoreOfParenthesesSolution solution = new scoreOfParenthesesSolution();

        int res = solution.scoreOfParentheses(demo);
        // System.out.println(res);
        System.out.println(res);
    }
}
