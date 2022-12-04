import java.util.ArrayDeque;
import java.util.Deque;

/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-11-12 16:05:31
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-12-03 21:57:19
 * @Descripttion: 给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。

示例 1:

输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]

 */
public class dailyTemperaturesStack {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] res = new int[temperatures.length];

        Deque<Integer> stack = new ArrayDeque<Integer>();
        for (int i = 0; i < temperatures.length; i++) {
            while (!stack.isEmpty() && temperatures[stack.peekLast()] < temperatures[i]) {
                int pre_index = stack.pollLast();
                res[pre_index] = i - pre_index;
            }
            stack.addLast(i);
        }
        return res;
    }

    public static void main(String[] args) {
        // int[] heights = { 2, 1, 5, 6, 2, 3 };
        // dailyTemperaturesStack solution = new dailyTemperaturesStack();
        // int[] area = solution.dailyTemperatures(heights);
        // System.out.println(area);

        int[] res = new int[5];

        for (int a : res) {
            System.out.println(a);
        }

    }
}
