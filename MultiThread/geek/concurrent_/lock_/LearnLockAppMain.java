/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-12-21 22:20:17
 * @LastEditors: 
 * @LastEditTime: 2022-12-21 22:20:19
 * @Descripttion: 
 */
package MultiThread.geek.concurrent_.lock_;

import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

/**
 * 
 */
public class LearnLockAppMain {
    public static void main(String[] args) {
        Lock lock = new ReentrantLock();
        for (int i = 0; i < 3; i++) {
            Thread thread = new Thread(new WorkWithLock(lock), "Worker-" + i);
            thread.start();
        }
    }
}