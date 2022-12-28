/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-12-20 22:19:59
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-12-20 22:36:24
 * @Descripttion: 
 */
package MultiThread.geek.concurrent_;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.atomic.AtomicLong;

public class AtomicNumberAppMain {
    private AtomicLong al = new AtomicLong(0);
    private volatile long longVar = 0;

    public static void main(String[] args) throws InterruptedException {
        AtomicNumberAppMain atomicNumberAppMain = new AtomicNumberAppMain();
        List<Thread> atomicThreads = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            Thread atomic = new Thread(() -> {
                long start = System.currentTimeMillis();
                for (int j = 0; j < 10; j++) {
                    atomicNumberAppMain.al.incrementAndGet();
                }
                System.out.println("Atomic takes " + (System.currentTimeMillis() - start));
            });
            atomic.start();
            atomicThreads.add(atomic);
        }

        Thread primary = new Thread(() -> {
            long start = System.currentTimeMillis();
            for (int i = 0; i < 100; i++) {
                atomicNumberAppMain.longVar++;
            }
            System.out.println("Primary var takes " + (System.currentTimeMillis() - start));
        });
        primary.start();

        for (Thread atomicThread : atomicThreads) {
            atomicThread.join();
        }
        primary.join();

        // TODO 结果是一样的
        System.out.println(atomicNumberAppMain.toString());
    }

    @Override
    public String toString() {
        return "AtomicNumberAppMain{" +
                "atomicLong=" + al +
                ", longVar=" + longVar +
                '}';
    }
}
