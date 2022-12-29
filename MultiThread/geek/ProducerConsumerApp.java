/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-12-17 16:18:36
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-12-18 16:12:25
 * @Descripttion: 
 */
package MultiThread.geek;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Random;

public class ProducerConsumerApp {
    public static final Object lock = new Object();

    public static void main(String[] args) {
        Queue<String> tasks = new LinkedList<String>();
        producer<String> producer = new producer<String>(tasks, 10);
        consumer<String> consumer = new consumer<String>(tasks);

        for (int i = 0; i < 4; i++) {
            Thread consumerThread = new Thread(() -> {
                while (true) {
                    try {
                        String url = consumer.consume();
                        processing(url);
                    } catch (InterruptedException e) {
                        // TODO Auto-generated catch block
                        e.printStackTrace();
                    }
                }
            }, "消费者 " + String.valueOf(i));
            consumerThread.start();
        }

        for (int i = 0; i < 3; i++) {
            Thread producerThread = new Thread(() -> {
                while (true) {
                    String url = getUrl();
                    try {
                        producer.produce(url);
                    } catch (InterruptedException e) {
                        // TODO Auto-generated catch block
                        e.printStackTrace();
                    }
                }
            }, "生产者 " + String.valueOf(i));
            producerThread.start();
        }
    }

    public static void processing(String url) throws InterruptedException {
        System.out.println(Thread.currentThread().getName() + "  正在消费url: " + url);
        System.out.println();
        Thread.sleep(5000);
        System.out.println(url + "  消费结束！！");
    }

    public static String getUrl() {
        int nums = new Random().nextInt(100000);
        String url = "www." + String.valueOf(nums) + ".com";
        System.out.println("生产消息 url : " + url);
        return url;
    }

}
