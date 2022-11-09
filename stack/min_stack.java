import java.util.Deque;
import java.util.LinkedList;

/*
 * @Author: your name
 * @Date: 2021-09-30 15:35:24
 * @LastEditTime: 2022-11-05 21:48:21
 * @LastEditors: congpeixin congpeixin@dongqiudi.com
 * @Description: In User Settings Edit
 * @FilePath: /leetcode-bbbbrent/stack/min_stack.java
 */
class MinStack {
    Deque<Integer> stack;
    Deque<Integer> min_stack;
    /** initialize your data structure here. */
    public MinStack() {
        stack = new LinkedList<Integer>();
        min_stack = new LinkedList<Integer>();
    }
    
    public void push(int x) {
        stack.push(x);
        if (min_stack.isEmpty() || x <= min_stack.getFirst()) {
            min_stack.push(x);
        }
    }
    
    public void pop() {
        if(stack.pop() == min_stack.getFirst()){
            min_stack.pop();
        }
    }
    
    public int top() {
        return stack.getFirst();
    }
    
    public int min() {
        return min_stack.getFirst();
    }
}