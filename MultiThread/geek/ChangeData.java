/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-12-16 10:03:14
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-12-16 10:54:33
 * @Descripttion: 
 */
package MultiThread.geek;

public class ChangeData implements Runnable {
    private long delta;
    private long loopCount;
    private DataHolder dataHolder;

    public ChangeData(long delta, long loopCount, DataHolder dataHolder) {
        this.delta = delta;
        this.loopCount = loopCount;
        this.dataHolder = dataHolder;
    }

    @Override
    public void run() {
        System.out.println("当前线程： " + Thread.currentThread().getName());
        // TODO Auto-generated method stub
        for (int i = 0; i < loopCount; i++) {
            dataHolder.change(delta);
        }
        dataHolder.print();
    }

}
