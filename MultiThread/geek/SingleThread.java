/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-12-16 10:31:38
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-12-16 10:43:24
 * @Descripttion: 
 */
package MultiThread.geek;

public class SingleThread {
    public static void main(String[] args) {
        DataHolder dataHolder = new DataHolder();
        ChangeData increas = new ChangeData(2, 50, dataHolder);
        increas.run();
        ChangeData dec = new ChangeData(-2, 50, dataHolder);
        dec.run();
    }
}