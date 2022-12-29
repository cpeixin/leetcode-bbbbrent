/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-12-18 16:15:41
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-12-18 18:04:03
 * @Descripttion: 
 */
package MultiThread.geek;

import java.util.ArrayList;
import java.util.List;

public class ThreadJoinAppMain {
    private static final List<String> CONTENTS = new ArrayList<String>();
    private static long WORKING_DURATION = 0;

    public static void main(String[] args) throws InterruptedException {
        long mainStart = System.currentTimeMillis();
        List<Thread> threads = new ArrayList<Thread>();

        for (int i = 0; i < 10; i++) {
            Thread thread = new Thread(() -> {
                System.out.println(Thread.currentThread().getName() + "  线程开始抓取！！");
                long start = System.currentTimeMillis();
                String content = getContents();
                long threadDuration = System.currentTimeMillis() - start;
                System.out.println(Thread.currentThread().getName() + " 抓取网页内容结束！！");
                synchronized (CONTENTS) {
                    CONTENTS.add(content);
                    WORKING_DURATION += threadDuration;
                }
            }, "Thread-" + i);

            thread.start();
            threads.add(thread);
        }

        Thread.sleep(2000);

        System.out.println("===========主线程开始join===========");

        for (Thread thread : threads) {
            String name = thread.getName();
            System.out.println("======== 主线程开始join  " + name + " =============");
            thread.join();
            System.out.println("======== 主线程join  " + name + " 结束=============");

        }
        System.out.println("======== 主线程join结束  获取的内容为 : =============");

        CONTENTS.forEach((content) -> {
            System.out.print(content.length() + ": ");
            System.out.println(content);
        });

        System.out.print("主线程耗时: ");
        System.out.println(System.currentTimeMillis() - mainStart);

        System.out.print("子线程耗时: ");
        System.out.println(WORKING_DURATION);

    }

    public static String getContents() {
        StringBuilder ret = new StringBuilder();
        int len = ((int) (Math.random() * 1000000)) % 4096 + 1024;
        for (int i = 0; i < len; i++) {
            int rand = ((int) (Math.random() * 1000)) % 26;
            char ch = (char) (rand + 'a');
            ret.append(ch);
            try {
                Thread.sleep(1);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        return ret.toString();
    }
}
