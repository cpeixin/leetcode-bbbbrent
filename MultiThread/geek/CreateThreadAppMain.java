/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-12-14 20:33:53
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-12-15 16:27:18
 * @Descripttion: 
 * Java 提供了两种类型的线程：守护线程 和 用户线程

用户线程 是高优先级线程。JVM 会在终止之前等待任何用户线程完成其任务。
守护线程 是低优先级线程。其唯一作用是为用户线程提供服务。
由于守护线程的作用是为用户线程提供服务，并且仅在用户线程运行时才需要，因此一旦所有用户线程完成执行，JVM 就会终止。也就是说 守护线程不会阻止 JVM 退出。

这也是为什么通常存在于守护线程中的无限循环不会导致问题，因为任何代码（包括 finally 块 ）都不会在所有用户线程完成执行后执行。

这也是为什么我们并不推荐 在守护线程中执行 I/O 任务 。因为可能导致无法正确关闭资源。

但是，守护线程并不是 100% 不能阻止 JVM 退出的。守护线程中设计不良的代码可能会阻止 JVM 退出。例如，在正在运行的守护线程上调用Thread.join() 可以阻止应用程序的关闭。


 */
package MultiThread.geek;

public class CreateThreadAppMain {
    public static final String TEXT = "计数排序是一种线性时间的整数排序算法。如果数组的长度为n，整数范围（数组中最大整数与最小整数的差值）为k，对于k远小于n的场景（如对某公司所有员工的年龄排序），那么计数排序的时间复杂度优于其他基于比较的排序算法（如归并排序、快速排序等）";

    public static void main(String[] args) {
        // 每行代码都是通过线程进行执行的。可以通过Thread.currentThread()获取当前执行线程
        System.out.println(Thread.currentThread().getName() + "线程正在执行");
        for (int i = 0; i < 1; i++) {
            Thread thead = new Thread(new printThread(TEXT, 200));
            // 设置当前线程为守护线程
            // 设置当前线程为守护线程后，上面的打印线程会随着main线程的结束而退出，如果不是守护线程，则不会。
            thead.setDaemon(true);
            thead.start();
        }

        System.out.println(Thread.currentThread().getName() + "线程执行结束");
    }

    public static class printThread implements Runnable {
        private String text;
        private int interval;

        public printThread(String text, int interval) {
            this.text = text;
            this.interval = interval;
        }

        @Override
        public void run() {
            // TODO Auto-generated method stub
            try {
                System.out.println(Thread.currentThread().getName() + "当前线程马上开始执行....");
                for (int i = 0; i < text.length(); i++) {
                    System.out.print(text.charAt(i));
                    Thread.sleep(interval);
                }
                System.out.println(Thread.currentThread().getName() + "当前线程执行完毕！！！");
            } catch (InterruptedException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }

        }

    }

}
