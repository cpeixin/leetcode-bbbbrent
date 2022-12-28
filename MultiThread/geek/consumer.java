/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-12-16 22:09:27
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-12-17 16:52:37
 * @Descripttion: 
 */
package MultiThread.geek;

import java.util.Queue;

public class consumer<T> {
    public Queue<T> tasks;

    public consumer(Queue<T> tasks) {
        this.tasks = tasks;
    }

    /**
     * @return
     * @throws InterruptedException
     */
    public T consume() throws InterruptedException {
        synchronized (tasks) {
            while (tasks.size() == 0) {
                System.out.println("队列为空....等待队列中生成消息....");
                tasks.wait();
            }

            T task = tasks.poll();
            tasks.notifyAll();

            return task;
        }
    }
}