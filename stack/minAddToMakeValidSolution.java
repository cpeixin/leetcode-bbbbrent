import java.util.ArrayDeque;
import java.util.Deque;

/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-11-22 22:21:03
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-11-22 22:25:55
 * @Descripttion: 
 */
public class minAddToMakeValidSolution {
    /**
     * 我们可以通过对字符串s进行每个字符的遍历，放到堆栈中。当发现栈顶字符是‘(’，待入栈的字符是‘)’，则符合括号匹配的情况。
     * 那么，此时我们只需将栈顶字符出栈即可。而针对于其他情况，我们都是将遍历的字符入栈即可。
     * 那么字符串s遍历完毕之后，我们来调用size()方法计算存储的字符长度，返回的长度就是这道题的结果
     */
    public int minAddToMakeValid(String s) {
        Deque<Character> deque = new ArrayDeque();
        for (char sc : s.toCharArray()) {
            if (deque.size() != 0 && (deque.peekLast()).equals('(') && sc == ')')
                deque.removeLast();
            else
                deque.addLast(sc);
        }
        return deque.size();
    }

    public int minAddToMakeValid_1(String s) {
        // 特例判断
        if (s.length() == 0)
            return 0;
        Deque<Integer> char_stack = new ArrayDeque<Integer>();
        int need_num = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                char_stack.addLast(i);
            } else {
                if (char_stack.isEmpty()) {
                    // 遇到右括号，但是栈为空的情况下，这里需要插入一个字符。
                    need_num += 1;
                } else {
                    char_stack.pollLast();
                }
            }
        }
        while (!char_stack.isEmpty()) {
            char_stack.pollLast();
            need_num += 1;
        }
        return need_num;
    }

}
