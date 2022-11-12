/*
 * @Author: congpeixin congpeixin@dongqiudi.com
 * @Date: 2022-11-06 08:38:23
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-11-11 21:04:17
 * @FilePath: /leetcode-bbbbrent/stack/calculate.java
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
import java.util.ArrayDeque;
import java.util.Deque;

public class calculate {
    public static void main(String[] args) {

        // char - '0'是用了ascii码位置索引计算，将字符转换为数字。
        String s = "3+2*2";
        Deque<Integer> stack = new ArrayDeque<Integer>();
        char preSign = '+';
        int num = 0;
        int n = s.length();
        for (int i = 0; i < n; ++i) {
            char ss = s.charAt(i);
            if (Character.isDigit(s.charAt(i))) {
                num = num * 10 + s.charAt(i) - '0';
            }
            if (!Character.isDigit(s.charAt(i)) && s.charAt(i) != ' ' || i == n - 1) {
                switch (preSign) {
                case '+':
                    stack.push(num);
                    break;
                case '-':
                    stack.push(-num);
                    break;
                case '*':
                    stack.push(stack.pop() * num);
                    break;
                default:
                    stack.push(stack.pop() / num);
                }
                preSign = s.charAt(i);
                num = 0;
            }
        }
        int ans = 0;
        while (!stack.isEmpty()) {
            ans += stack.pop();
        }
        System.out.println(ans);
    }
}
