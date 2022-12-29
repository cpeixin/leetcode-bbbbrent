/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-12-20 21:45:20
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-12-20 22:35:05
 * @Descripttion: 
 */
package MultiThread.geek.volatile_;

public class volatileApp {
    public static void main(String[] args) {
        DataHolder dataHolder = new DataHolder();

        Thread operator = new Thread(() -> {
            while (true) {
                dataHolder.operateData();
            }
        });
        operator.start();

        Thread checker = new Thread(() -> {
            while (true) {
                dataHolder.check();
            }
        });
        checker.start();
    }
}
