import java.util.Deque;
import java.util.LinkedList;

/*
 * @Author: your name
 * @Date: 2021-09-30 11:24:46
<<<<<<< HEAD
 * @LastEditTime: 2022-11-08 21:41:37
 * @LastEditors: Please set LastEditors
=======
 * @LastEditTime: 2022-11-05 21:48:04
 * @LastEditors: congpeixin congpeixin@dongqiudi.com
>>>>>>> 84afc6f33d30f688b55b4f21343006d4fe80acbf
 * @Description: In User Settings Edit
 * @FilePath: /leetcode-bbbbrent/stack/CQueue.java
 */
public class CQueue {
    Deque<Integer> appendTailStack;
    Deque<Integer> deleteHeadStack;

    public CQueue() {
        appendTailStack = new LinkedList<Integer>();
        deleteHeadStack = new LinkedList<Integer>();
    }

    public void appendTail(int value) {
        appendTailStack.push(value);
    }
    
    public int deleteHead() {
        if(!deleteHeadStack.isEmpty()){
            return deleteHeadStack.pop();
        }
        if(appendTailStack.isEmpty()){
            return -1;
        }
        while(appendTailStack.size()>0){
            deleteHeadStack.push(appendTailStack.pop());
        }
        return deleteHeadStack.pop();
    }
}
