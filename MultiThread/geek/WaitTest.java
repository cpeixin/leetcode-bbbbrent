/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-12-16 14:41:32
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-12-16 14:56:46
 * @Descripttion: 
 */
package MultiThread.geek;

public class WaitTest {

    static Object object = new Object();

    public static void main(String[] args) {

        new Thread(() -> {
            synchronized (object) {
                System.out.println("开始线程 A");
                System.out.println("线程 A 暂停 1 秒");
                try {
                    object.wait(1000);
                    Thread.sleep(2000L);
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

                System.out.println("结束线程 B");
            }
        }, "线程 B").start();

    }

}