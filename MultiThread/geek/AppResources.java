/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-12-18 22:53:49
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-12-28 21:27:56
 * @Descripttion: 
 */
package MultiThread.geek;

public class AppResources {

    // TODO 系统中有两个或者多个资源，如果不按照顺序申请，而且申请到一个后，再申请另一个的时候不释放原来的资源锁，就可能会死锁
    private Object resourcePrinter = new Object();

    private Object resourceInput = new Object();

    public Object getResourcePrinter() {
        return resourcePrinter;
    }

    public void setResourcePrinter(Object resourcePrinter) {
        this.resourcePrinter = resourcePrinter;
    }

    public Object getResourceInput() {
        return resourceInput;
    }

    public void setResourceInput(Object resourceInput) {
        this.resourceInput = resourceInput;
    }
}