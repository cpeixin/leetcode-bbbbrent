package count_sort;
/**
 * 
给定两个数组，arr1 和 arr2，

arr2 中的元素各不相同
arr2 中的每个元素都出现在 arr1 中
对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。


示例：
输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19]
     arr2 = [2,1,4,3,9,6]
输出：[2,2,2,1,4,3,3,9,6,7,19]


提示：

1 <= arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
arr2 中的元素 arr2[i] 各不相同
arr2 中的每个元素 arr2[i] 都出现在 arr1 中



 */
public class relativeSortArraySolution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        // 统计arr1各个数字出现了几次
        int[] counts = new int[1001];
        // 这里直接使用数字本身当做下标，来统计本身出现的次数
        for(int num: arr1){
            counts[num] += 1;
        }

        int i=0;
        for(int num: arr2){
            while(counts[num] > 0){
                arr1[i++] = num;
                counts[num] -= 1;
            }
        }

        for(int num=0; num < counts.length; num++){
            while(counts[num] > 0){
                arr1[i++] = num;
                counts[num] -= 1;
            }
        }

        for(int num=0; num < counts.length; num++){
            while(counts[num] > 0){
                arr1[i++] = num;
                counts[num] -= 1;
            }
        }

        return arr1;
    }


    public static void main(String[] args) {
        int[] arr1 = {2,3,1,3,2,4,6,7,9,2,19};
        int[] arr2 = {2,1,4,3,9,6};

        relativeSortArraySolution solution = new relativeSortArraySolution();
        int[] res = solution.relativeSortArray(arr1, arr2);
        System.out.println(res);
    }
}
