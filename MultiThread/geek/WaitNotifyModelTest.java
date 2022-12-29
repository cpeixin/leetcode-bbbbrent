/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-12-16 15:47:44
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-12-16 21:53:50
 * @Descripttion: 
 */
package MultiThread.geek;

import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

public class WaitNotifyModelTest {
    // 存储生产者产生的数据
    static List<String> list = new ArrayList<>();

    public static void main(String[] args) {

        new Thread(() -> {
            while (true) {
                synchronized (list) {
                    // 判断 list 中是否有数据，如果有数据的话，就进入等待状态，等数据消费完
                    if (list.size() != 0) {
                        try {
                            list.wait();
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                    }

                    // list 中没有数据时，产生数据添加到 list 中
                    list.add(UUID.randomUUID().toString());
                    list.notify();
                    System.out.println(Thread.currentThread().getName() + list);
                }
            }
        }, "生产者线程 A ").start();

        new Thread(() -> {
            while (true) {
                synchronized (list) {
                    // 如果 list 中没有数据，则进入等待状态，等收到有数据通知后再继续运行
                    if (list.size() == 0) {
                        try {
                            list.wait();
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                    }

                    // 有数据时，读取数据
                    System.out.println(Thread.currentThread().getName() + list);
                    list.notify();
                    // 读取完毕，将当前这条 UUID 数据进行清除
                    list.clear();
                }
            }
        }, "消费者线程 B ").start();

    }
}
