import java.util.Deque;
import java.util.Map;
import java.util.ArrayDeque;

/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-11-19 08:55:01
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-11-19 11:38:35
 * @Descripttion: 
 * 
 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。
 

示例 1：
输入：s = "()"
输出：true

示例 2：
输入：s = "()[]{}"
输出：true

示例 3：
输入：s = "(]"
输出：false


题解：正常的遍历入栈，出栈判断栈顶时候是匹配的字符，遍历结束后，判断栈是否为空。

 */
public class isValidSolution {
    public boolean isValid(String s) {
        boolean res = true;
        // 特例判断
        if (s.length() == 0)
            return true;
        if (s.length() == 1)
            return false;

        Deque<Character> char_stack = new ArrayDeque<Character>();

        for (int i = 0; i < s.length(); i++) {
            Character c = s.charAt(i);
            switch (c) {
                case '(':
                case '[':
                case '{':
                    char_stack.addLast(c);
                    break;
                case ')':
                    if (!char_stack.isEmpty() && char_stack.peekLast() == '(') {
                        char_stack.pollLast();
                    } else {
                        res = false;
                        return res;
                    }
                    break;
                case ']':
                    if (!char_stack.isEmpty() && char_stack.peekLast() == '[') {
                        char_stack.pollLast();
                    } else {
                        res = false;
                        return res;
                    }
                    break;
                case '}':
                    if (!char_stack.isEmpty() && char_stack.peekLast() == '{') {
                        char_stack.pollLast();
                    } else {
                        res = false;
                        return res;
                    }
                    break;
            }
        }

        if (!char_stack.isEmpty()) {
            res = false;
        }
        return res;
    }

    public boolean isValid_1(String s) {
        // 特例判断
        if (s.length() == 0)
            return true;
        if (s.length() == 1)
            return false;

        // 定义栈
        Deque<Character> char_stack = new ArrayDeque<Character>();
        // 先添加一个占位符，方便判空
        char_stack.addLast('?');

        Map<Character, Character> char_map = Map.of('(', ')', '[', ']', '{', '}');

        for (Character c : s.toCharArray()) {
            if (char_map.containsKey(c)) {
                char_stack.addLast(c);
            } else {
                Character left_char = char_stack.pollLast();
                if (char_map.get(left_char) != c) {
                    return false;
                }
            }
        }

        return char_stack.size() == 1;
    }

    public static void main(String[] args) {
        String demo = "()[]{}";
        isValidSolution solution = new isValidSolution();
        boolean res = solution.isValid_1(demo);
        System.out.println(res);
    }
}
