// Description 冒泡排序
// Author
// Date

// """
// 第一个(外层)for循环作用：控制排序的轮数
// 第二个(内层)for循环作用：控制每一轮里的每一个比较步骤
// """

/**
 * 时间复杂度 & 空间复杂度
冒泡排序从 1956 年就有人开始研究，之后经历过多次优化。它的空间复杂度为 O(1)，时间复杂度为 O(n^2)

第二种、第三种冒泡排序由于经过优化，最好的情况下只需要 O(n) 的时间复杂度。

最好情况：在数组已经有序的情况下，只需遍历一次，由于没有发生交换，排序结束。
最差情况：数组顺序为逆序，每次比较都会发生交换。

优化后的冒泡排序平均时间复杂度仍然是 O(n^2)
 
所以这些优化对算法的性能并没有质的提升。
正如 Donald E. Knuth（19741974 年图灵奖获得者）所言：“冒泡排序法除了它迷人的名字和导致了某些有趣的理论问题这一事实外，似乎没有什么值得推荐的。”

 */


public class bubbleSortClass {
    // 原始方法
    public static void bubbleSort(int[] arr) {
        for(int i=0; i<arr.length; i++){
            for (int j = 0; j < arr.length-i-1; j++){
                if (arr[j] > arr[j+1]){
                    swap(arr,j, j+1);
                }
            }  
        }
    }

    // 轮数优化，如果当前轮次没有发生交换，则整体排序完成
    public static void bubbleSort_1(int[] arr) {
        for(int i=0; i<arr.length; i++){
            boolean flag = false;
            for (int j = 0; j < arr.length-i-1; j++){
                if (arr[j] > arr[j+1]){
                    swap(arr,j, j+1);
                    flag = true;
                }
            }
            if(!flag){
                break;
            }
        }
    }

    // 在第二种方法上做优化，记录最后一次交换的位置
    public static void bubbleSort_2(int[] arr) {
        boolean swapped = true;
        // 最后一个没有经过排序的元素的下标
        int indexOfLastUnsortedElement = arr.length - 1;
        // 上次发生交换的位置
        int swappedIndex = -1;
        while (swapped) {
            swapped = false;
            for (int i = 0; i < indexOfLastUnsortedElement; i++) {
                if (arr[i] > arr[i + 1]) {
                    // 如果左边的数大于右边的数，则交换，保证右边的数字最大
                    swap(arr, i, i + 1);
                    // 表示发生了交换
                    swapped = true;
                    // 更新交换的位置
                    swappedIndex = i;
                }
            }
            // 最后一个没有经过排序的元素的下标就是最后一次发生交换的位置
            indexOfLastUnsortedElement = swappedIndex;
        }
    }

    // 两个数字交换（普通方法，引入第三个变量）
    public static void swap(int[] arr, int a, int b) {
        int tmp = arr[a];
        arr[a] = arr[b];
        arr[b] = tmp;
    }

    // 利用位运算，不引入第三个变量的情况下，来进行两个数字的交换
    public static void swap_bit(int[] arr, int a, int b) {
        arr[a] = arr[a] ^ arr[b];
        arr[b] = arr[b] ^ arr[a];
        arr[a] = arr[a] ^ arr[b];
        System.out.println(arr[a]);
        System.out.println(arr[b]);
    }

    // 位运算，两数交换
    // 异或运算： 两位不同-值为1 两位相同-值为0
    public static void swap_bit(int a, int b) {
        a = a ^ b;
        b = b ^ a;
        a = a ^ b;
        System.out.println(a);
        System.out.println(b);
    }


    public static void main(String[] args){
        int[] arr = {45, 71, 51, 84, 79, 97};
        // long start = System.currentTimeMillis();

        bubbleSortClass.bubbleSort_1(arr);
        // for(int num: arr){
        //     System.out.println(num);
        // }
        // // some code
        // long finish = System.currentTimeMillis();
        // long timeElapsed = finish - start;
        // System.out.println(timeElapsed);
        
        // swap_bit(2,6);
        
    }
    
}
