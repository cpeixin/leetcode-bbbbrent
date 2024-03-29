// /*
//  * @version: 
//  * @Author: Brent
//  * @Date: 2020-12-05 13:50:15
//  * @LastEditors: Please set LastEditors
//  * @LastEditTime: 2020-12-05 13:51:42
//  * @Descripttion: 
//  */
// import java.util.ArrayList;
// import java.util.Arrays;
// import java.util.Collections;
// import java.util.Comparator;
// import java.util.List;
// import java.util.Stack;


// public class merge_array {

//     public int[][] merge(int[][] intervals) {
//         int len = intervals.length;
//         if (len < 2) {
//             return intervals;
//         }

//         // 按照起点排序
//         Arrays.sort(intervals, Comparator.comparingInt(o -> o[0]));

//         // 也可以使用 Stack，因为我们只关心结果集的最后一个区间
//         List<int[]> res = new ArrayList<>();
//         res.add(intervals[0]);

//         for (int i = 1; i < len; i++) {
//             int[] curInterval = intervals[i];

//             // 每次新遍历到的列表与当前结果集中的最后一个区间的末尾端点进行比较
//             int[] peek = res.get(res.size() - 1);

//             if (curInterval[0] > peek[1]) {
//                 res.add(curInterval);
//             } else {
//                 // 注意，这里应该取最大
//                 peek[1] = Math.max(curInterval[1], peek[1]);
//             }
//         }
//         return res.toArray(new int[res.size()][]);
//     }

//     public static void main(String[] args) {
//         merge_array solution = new merge_array();
//         int[][] intervals = {{1, 3}, {2, 6}, {8, 10}, {15, 18}};
//         int[][] res = solution.merge(intervals);
//         for (int i = 0; i < res.length; i++) {
//             System.out.println(Arrays.toString(res[i]));
//         }
//     }
// }