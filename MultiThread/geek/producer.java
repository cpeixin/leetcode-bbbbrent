/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-12-16 22:01:18
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-12-17 16:40:17
 * @Descripttion: 
 */
package MultiThread.geek;

import java.util.Queue;

public class producer<T> {
    public Queue<T> tasks;
    public int maxQueueSize;

    public producer(Queue<T> tasks, int maxQueueSize) {
        this.tasks = tasks;
        this.maxQueueSize = maxQueueSize;
    }

    public void produce(T task) throws InterruptedException {
        synchronized (tasks) {
            while (tasks.size() >= maxQueueSize) {
                System.out.println("队列已满...进入等待.....");
                tasks.wait();
            }
            tasks.add(task);
            tasks.notifyAll();
        }
    }
}
