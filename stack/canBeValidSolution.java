import java.util.ArrayDeque;
import java.util.Deque;

/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-11-16 22:08:24
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-11-16 23:01:49
 * @Descripttion:     
输入：s = "))()))", locked = "010100"
输出：true
解释：locked[1] == '1' 和 locked[3] == '1' ，所以我们无法改变 s[1] 或者 s[3] 。
我们可以将 s[0] 和 s[4] 变为 '(' ，不改变 s[2] 和 s[5] ，使 s 变为有效字符串。

本题解法同 https://leetcode.cn/problems/valid-parenthesis-string/

同样是利用双栈解决
左括号一个栈
万能符一个栈

最后如果左括号栈不为空，则返回FALSE
最后如果万能栈不为空，万能栈的长度不能为奇数。

超级容易明白的题解：https://leetcode.cn/problems/check-if-a-parentheses-string-can-be-valid/solution/chao-xiao-bai-pan-duan-gua-hao-zi-fu-chu-3jlb/


 */
public class canBeValidSolution {
    public boolean canBeValid(String s, String locked) {
        // 特例判断
        // 字符串长度为奇数，直接返回FALSE
        if(s.length()%2!=0) return false; 

        Deque<Integer> left_stack = new ArrayDeque<Integer>();
        Deque<Integer> zero_stack = new ArrayDeque<Integer>();

        for(int i=0; i< s.length();i++){
            char c = s.charAt(i);
            char lock_c = locked.charAt(i);
            // 不能变化的字符入栈
            if(lock_c == '1'){
                if(c=='('){
                    left_stack.addLast(i);
                }else{
                    // 右括号
                    if(!left_stack.isEmpty()){
                        left_stack.pollLast();
                    }else if(!zero_stack.isEmpty()){
                        zero_stack.pollLast();
                    }else return false;
                }
            } else {
                // 可以变化的字符入栈
                zero_stack.addLast(i);
            }
        }

        while(!left_stack.isEmpty() && !zero_stack.isEmpty()){
            int left_stack_top = left_stack.pollLast();
            int zero_stack_top = zero_stack.pollLast();
            if(left_stack_top>zero_stack_top){
                return false;
            }
        }

        return left_stack.isEmpty() && zero_stack.size()%2==0;
    }

    public static void main(String[] args) {
        String s = "))()))";
        String locked = "010100";
        canBeValidSolution solution = new canBeValidSolution();
        boolean res = solution.canBeValid(s, locked);
        System.out.println(res);
    }
}
