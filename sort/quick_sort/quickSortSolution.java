/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-12-07 21:20:52
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-12-07 22:44:03
 * @Descripttion: 
 * https://labuladong.oschina.io/algo/2/21/45/
 * 
 * 
 * 
 * 看看JDK里面的快排
 */
package quick_sort;

public class quickSortSolution {

    // 划分
    public int partition(int arr[], int head, int tail) {
        int low = head;
        int pivot = arr[tail];

        for (int i = head; i < tail; i++) {
            if (arr[i] < pivot) {
                int tmp = arr[i];
                arr[i] = arr[low];
                arr[low] = tmp;
                low += 1;
            }
        }

        arr[tail] = arr[low];
        arr[low] = pivot;

        return low;
    }

    public void quickSort(int[] array, int head, int tail) {
        if (head >= tail)
            return;
        int pivot = partition(array, head, tail);
        quickSort(array, head, pivot - 1);
        quickSort(array, pivot + 1, tail);
    }

    public int[] quick(int[] array) {
        int head = 0;
        int tail = array.length - 1;
        quickSort(array, head, tail);
        return array;
    }

    public static void main(String[] args) {
        int[] array = { 3, 2, 3, 1, 2, 4, 5, 5, 6 };
        quickSortSolution solution = new quickSortSolution();
        int[] res = solution.quick(array);
        for (int num : res) {
            System.out.println(num);
        }
        System.out.println(res);
    }
}
