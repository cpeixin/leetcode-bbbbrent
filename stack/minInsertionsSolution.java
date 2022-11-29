/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-11-29 22:25:25
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-11-29 22:52:55
 * @Descripttion: 
 * 给你一个括号字符串 s ，它只包含字符 '(' 和 ')' 。一个括号字符串被称为平衡的当它满足：

任何左括号 '(' 必须对应两个连续的右括号 '))' 。
左括号 '(' 必须在对应的连续两个右括号 '))' 之前。
比方说 "())"， "())(())))" 和 "(())())))" 都是平衡的， ")()"， "()))" 和 "(()))" 都是不平衡的。

你可以在任意位置插入字符 '(' 和 ')' 使字符串平衡。

请你返回让 s 平衡的最少插入次数。

 

示例 1：

输入：s = "(()))"
输出：1
解释：第二个左括号有与之匹配的两个右括号，但是第一个左括号只有一个右括号。我们需要在字符串结尾额外增加一个 ')' 使字符串变成平衡字符串 "(())))" 。
示例 2：

输入：s = "())"
输出：0
解释：字符串已经平衡了。
示例 3：

输入：s = "))())("
输出：3
解释：添加 '(' 去匹配最开头的 '))' ，然后添加 '))' 去匹配最后一个 '(' 。
示例 4：

输入：s = "(((((("
输出：12
解释：添加 12 个 ')' 得到平衡字符串。
示例 5：

输入：s = ")))))))"
输出：5
解释：在字符串开头添加 4 个 '(' 并在结尾添加 1 个 ')' ，字符串变成平衡字符串 "(((())))))))" 。
 */
public class minInsertionsSolution {
    public int minInsertions(String s) {
        int res = 0;
        int need = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                need += 2;
                if (need % 2 == 1) { // 右括号数量只能为偶数，但只能添（右括号少了）
                    res++; // 插入一个右括号
                    need--; // 对右括号的需求-1
                }
            } else {
                need--;
                // need不可能小于-1，因为此处-1后若走上面必有+2
                if (need == -1) { // 右括号多了
                    res++; // 插入一个左括号
                    need = 1;
                }
            }
        }
        return res + need;
    }

    public static void main(String[] args) {
        String demo = "(()))";
        minInsertionsSolution solution = new minInsertionsSolution();
        int res = solution.minInsertions(demo);
        // System.out.println(res);
        System.out.println(res);
    }
}
