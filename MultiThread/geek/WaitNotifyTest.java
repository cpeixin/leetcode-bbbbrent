/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-12-16 14:58:01
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-12-16 15:08:58
 * @Descripttion: 
 */
package MultiThread.geek;

public class WaitNotifyTest {
    static Object object = new Object();

    public static void main(String[] args) {
        System.out.println();

        new Thread(() -> {
            synchronized (object) {
                System.out.println("开始线程 A");
                try {
                    object.wait();
                    System.out.println("A 线程重新获取到锁，继续进行");
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                System.out.println("结束线程 A");
            }
        }, "线程 A").start();

        new Thread(() -> {
            try {
                Thread.sleep(500L);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            synchronized (object) {
                System.out.println("开始线程 B");
                object.notify();
                System.out.println("线程 B 通知完线程 A");
                try {
                    // 试验执行完 notify() 方法后，A 线程是否能立即获取到锁
                    Thread.sleep(4000L);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                System.out.println("结束线程 B");
            }
        }, "线程 B").start();
    }
}
