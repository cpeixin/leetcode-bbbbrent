/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-12-21 21:09:16
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-12-21 21:17:36
 * @Descripttion: 
 */
package MultiThread.geek.synchronization_;

public class sychronizationCase {
    static int balance = 500;

    public static int withdraw(int amount) {
        if (amount < balance) {
            balance -= amount;
        }
        return balance;
    }

    public static void main(String[] args) {

        Thread b = new Thread(new Runnable() {
            @Override
            public void run() {
                // TODO Auto-generated method stub
                int res = withdraw(200);
                System.out.println(res);
            }
        });
        b.start();

        Thread a = new Thread(new Runnable() {

            @Override
            public void run() {
                // TODO Auto-generated method stub
                int res = withdraw(400);
                System.out.println(res);
            }
        });

        a.start();

    }
}
