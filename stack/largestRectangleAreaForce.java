/*
 * @Author: congpeixin congpeixin@dongqiudi.com
 * @Date: 2022-11-08 09:20:57
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-11-09 21:37:41
 * @FilePath: /leetcode-bbbbrent/stack/largestRectangleArea.java
 * @Description: 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
                求在该柱状图中，能够勾勒出来的矩形的最大面积。
                输入：heights = [2,1,5,6,2,3]
                输出：10
                解释：最大的矩形为图中红色区域，面积为 10
 */
import java.util.ArrayDeque;
import java.util.Deque;

/*
 * 暴力法
 * 依次遍历柱形的高度，对于每一个高度分别向两边扩散，求出以当前高度为矩形的最大宽度多少。
*/
public class largestRectangleAreaForce {

    public int largestRectangleArea(int[] heights) {
        int n = heights.length;
        if (heights.length == 0) return 0;
        if (heights.length == 1) return heights[0];

        int max_area = 0;
        for (int i = 0; i < n; i++) {
            int height = heights[i];
            int width = 0;
            int left_index = i;
            int right_index = i;
            while(left_index>0 && heights[left_index-1] >= heights[i]){
                left_index -= 1;
            }
            while(right_index<n-1 && heights[right_index+1] >= heights[i]){
                right_index += 1;
            }
            
            width = right_index - left_index + 1;
            max_area = Math.max(max_area, width*height);
        }
        return max_area;
    }
    public static void main(String[] args) {
        int[] heights = {2, 1, 5, 6, 2, 3};
        largestRectangleAreaForce solution = new largestRectangleAreaForce();
        int area = solution.largestRectangleArea(heights);
        System.out.println(area);
    }
}
