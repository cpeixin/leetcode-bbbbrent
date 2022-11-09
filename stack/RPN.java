/*
 * @Author: congpeixin congpeixin@dongqiudi.com
 * @Date: 2022-11-05 18:08:16
 * @LastEditors: congpeixin congpeixin@dongqiudi.com
 * @LastEditTime: 2022-11-06 08:39:24
 * @FilePath: /leetcode-bbbbrent/stack/RPN.java
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
import java.util.Stack;

/**
 * 题目：后缀表达式是一种算术表达式，它的操作符在操作数的后面。
 * 输入一个用字符串数组表示的后缀表达式，请输出该后缀表达式的计算结果。假设输入的一定是有效的后缀表达式。
 * 例如，后缀表达式["2"，"1"，"3"，"*"，"+"]对应的算术表达式是“2+1*3”，因此输出它的计算结果5。分析：后缀表达式又叫逆波兰式（Reverse Polish Notation，RPN）
 * 
 * 如果输入数组的长度是n，那么对其中的每个字符串都有一次push操作；
 * 如果是操作符，那么还需要进行数学计算和两次push操作。由于每个push操作、pop操作和数学计算都是O（1），因此总体时间复杂度是O（n）。
 * 由于栈中可能有O（n）个操作数，因此这种解法的空间复杂度也是O（n）
 */
public class RPN {
    public static void main(String[] args) {
        String[] chars =  {"2","1","+","3","*"};
        
        // 创建操作数栈
        // 创建运算符栈
        Stack<Integer> num_stack = new Stack<Integer>();

        for (String s: chars) {
            if(s.equals("+") || s.equals("-") || s.equals("*") || s.equals("/")){
                int num1 = num_stack.pop();
                int num2 = num_stack.pop();
                if(s.equals("+")){
                    num_stack.push(num1+num2);
                    // continue;
                }else if(s.equals("-")){
                    num_stack.push(num2-num1);
                    // continue;
                }else if(s.equals("*")){
                    num_stack.push(num1*num2);
                    // continue;
                }else if(s.equals("/")){
                    num_stack.push(num2/num1);
                    // continue;
                }
            }else{
                num_stack.push(Integer.valueOf(s));
            }            
        }
        System.out.println(num_stack.pop());
    }
}
