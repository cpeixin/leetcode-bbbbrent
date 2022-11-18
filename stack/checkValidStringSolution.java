import java.util.ArrayDeque;
import java.util.Deque;

/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-11-16 22:08:24
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-11-16 23:01:49
 * @Descripttion: 给定一个只包含三种字符的字符串：（ ，） 和 *，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则：

任何左括号 ( 必须有相应的右括号 )。
任何右括号 ) 必须有相应的左括号 ( 。
左括号 ( 必须在对应的右括号之前 )。
* 可以被视为单个右括号 ) ，或单个左括号 ( ，或一个空字符串。
一个空字符串也被视为有效字符串。
示例 1:

输入: "()"
输出: True
示例 2:

输入: "(*)"
输出: True
示例 3:

输入: "(*))"
输出: True



题解：想到栈，但是没有想到要用两个栈
     想到栈，但是没有想到要存储下标
     最后还是因为无处安放的 ‘*’号，选择去看题解。
     
     
 */
public class checkValidStringSolution {
    public boolean checkValidString(String s) {
        Deque<Integer> left_char_stack = new ArrayDeque<Integer>();
        Deque<Integer> star_char_stack = new ArrayDeque<Integer>();
        // 一次遍历结束
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            // 左括号和星号都是直接入栈
            if (c == '(') {
                left_char_stack.addLast(i);
            } else if (c == '*') {
                star_char_stack.addLast(i);
            } else {
                // 遇到右括号
                // 优先左括号出栈
                if (!left_char_stack.isEmpty()) {
                    left_char_stack.pollLast();
                } else if (!star_char_stack.isEmpty()) {
                    // 左括号栈为空时，这是 * 号则化身左括号
                    star_char_stack.pollLast();
                } else {
                    // 当 ）出现，但是左括号和*号全没了，直接返回false
                    return false;
                }
            }
        }

        // 一次遍历结束后，左括号栈和星号栈可能都不为空
        while (!left_char_stack.isEmpty() && !star_char_stack.isEmpty()) {
            int left_index = left_char_stack.pollLast();
            int star_index = star_char_stack.pollLast();
            // 当两个栈都不为空时，每次从左括号栈和星号栈分别弹出栈顶元素，对应左括号下标和星号下标
            // 左括号下标应小于星号下标
            if (left_index > star_index) {
                return false;
            }
        }

        // 如果星号栈为空，左括号栈不为空，则false。
        // 如果左括号栈为空，星号栈不为空，则星号栈的星号，全部充当为 空字符串。
        return left_char_stack.isEmpty();
    }

    public static void main(String[] args) {
        String demo = "(*))";
        checkValidStringSolution solution = new checkValidStringSolution();

        boolean res = solution.checkValidString(demo);
        // System.out.println(res);
        System.out.println(res);
    }

}
