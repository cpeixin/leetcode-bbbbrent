/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-12-15 19:51:25
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-12-15 19:55:45
 * @Descripttion: 线程中断的几个实际应用场景：

                在处理Web请求时，可能将请求分配到多个线程去处理，实现请求执行的超时机制；
                实现线程池时，关闭线程池中的线程任务。
 */
package MultiThread.geek;

public class interruptCase {
    public static void main(String[] args) throws InterruptedException {
        Thread thread = new Thread() {
            @Override
            public void run() {
                try {
                    Thread.sleep(10000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }

                System.out.println("interrupt");

                try {
                    Thread.sleep(10000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        };
        thread.start();

        thread.interrupt();
        Thread.sleep(5000);
        thread.interrupt();
    }
}
