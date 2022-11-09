// 堆化
// public class Heapify {
//   private int[] a; // 数组，从下标1开始存储数据
//   private int n;  // 堆可以存储的最大数据个数
//   private int count; // 堆中已经存储的数据个数

//   public Heap(int capacity) {

//     a = new int[capacity + 1];
//     n = capacity;
//     count = 0;
//   }

//   public void insert(int data) {
//     if (count >= n) return; // 堆满了
//     ++count;
//     a[count] = data;
//     int i = count;
//     // 自下往上堆化
//     // i/2 > 0 ：表示还没到达根节点 
//     // a[i] > a[i/2]：表示子节点大于根节点，根据最大堆规范，需要交换
//     while (i/2 > 0 && a[i] > a[i/2]) { 
//       // swap()函数作用：交换下标为i和i/2的两个元素（根节点和左子节点？）
//       // 子节点 i , 父节点 i/2， 插入的位置是左节点或者右节点没有关系，i/2 取整
//       swap(a, i, i/2); 
//       i = i/2;
//     }
//   }
// }
