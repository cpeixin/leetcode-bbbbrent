/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-12-16 10:50:43
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-12-16 14:30:56
 * @Descripttion: 
 */
package MultiThread.geek;

public class TwoThread {
    public static void main(String[] args) {
        DataHolder dh = new DataHolder();

        Thread incres = new Thread(new ChangeData(2, 10000, dh));
        Thread decres = new Thread(new ChangeData(-2, 10000, dh));
        System.out.println("计数开始执行");
        incres.start();
        decres.start();

    }

}
