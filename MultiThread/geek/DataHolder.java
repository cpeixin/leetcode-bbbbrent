/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-12-15 20:08:01
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-12-16 11:48:57
 * @Descripttion: 
 */
package MultiThread.geek;

public class DataHolder {
    private static long number = 0;

    // synchronized 在这个方法中是实例级别控制
    public synchronized void change(long delta) {
        number += delta;
    }

    public void print() {
        System.out.println(number);
    }
}
