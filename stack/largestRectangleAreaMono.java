/*
 * @Author: congpeixin congpeixin@dongqiudi.com
 * @Date: 2022-11-08 09:20:57
 * @LastEditors: congpeixin congpeixin@dongqiudi.com
 * @LastEditTime: 2022-11-08 09:36:08
 * @FilePath: /leetcode-bbbbrent/stack/largestRectangleArea.java
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
import java.util.ArrayDeque;
import java.util.Deque;

/*
 *
        想到单调栈：主要是在经过暴力解法后，我们时候可以找到办法，可不可以在一次遍历中就确定其左右边界呢？
                  在经历画图的过程中，发现这符合栈的性质，后进先出。
        3.单调栈优化:因为最终的目的是寻找对应柱子height[i]右边首个严格小于height[i]的柱子height[r]
            左边同理找到首个严格小于height[i]的柱子height[l]
            维护一个单调递增栈(栈底->栈顶),那么每当遇到新加入的元素<栈顶便可以确定栈顶柱子右边界
            而栈顶柱子左边界就是栈顶柱子下面的柱子(<栈顶柱子)
            左右边界确定以后就可以进行面积计算与维护最大面积
        时间复杂度:O(N),空间复杂度:O(N)
*/
public class largestRectangleAreaMono {
    public int largestRectangleArea(int[] heights) {

        // 特殊条件判断
        if(heights.length==0) return 0;
        if(heights.length==1) return heights[0];
        Deque<Integer> stack = new ArrayDeque<Integer>();

        // 遍历数组，判断栈顶与当前元素的大小关系
        for(int i=0; i<heights.length; i++){
            // 无论当前元素比栈顶元素大或者小，都是要入栈的。
            // 栈顶涉及到是否要弹出元素，所以要判空。
            int stack_top = heights[stack.peekLast()];
            int current_height = 0;
            int max_area = 0;
            while(!stack.isEmpty() && stack_top > heights[i]){
                int top_index = stack.pollLast();
                current_height = heights[top_index];
                max_area = Math.max(max_area, current_height * (i-top_index));
            }
            stack.addLast(i);
        }


        
        // 栈顶元素 > 当前元素, 则栈顶元素出！因为可以确定右边界，左边界也可确定，就是左边相邻的元素，因为栈是单调递增
        // 栈顶元素 < 当前元素, 则当前元素入栈！右侧元素比栈顶大，则右边界无法确定，左边界可确定，就是左边相邻的元素

        
        

        return 0;
    }
    public static void main(String[] args) {
        int[] heights = {2, 1, 5, 6, 2, 3};
        largestRectangleAreaMono solution = new largestRectangleAreaMono();
        int area = solution.largestRectangleArea(heights);
        System.out.println(area);
    }
}
