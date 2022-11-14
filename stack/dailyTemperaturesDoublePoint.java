/*
 * @version: 
 * @Author: Brent
 * @Date: 2022-11-12 16:04:22
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-11-12 17:30:37
 * @Descripttion: 给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。

 

示例 1:

输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]

超时超时超时！！！ 暴力解法！！O（n2）
 */
public class dailyTemperaturesDoublePoint {
    public int[] dailyTemperatures(int[] temperatures) {
        // 特例判断
        if (temperatures.length == 0)
            return new int[] { 0 };
        int[] res = new int[temperatures.length];
        // 双指针
        for (int i = 0; i < temperatures.length - 1; i++) {
            int slow = i;
            int fast = slow + 1;

            while (fast <= temperatures.length - 1) {
                if (temperatures[fast] > temperatures[slow]) {
                    res[slow] = fast - slow;
                    break;
                }
                fast += 1;
            }
        }
        res[temperatures.length - 1] = 0;
        return res;
    }
}
