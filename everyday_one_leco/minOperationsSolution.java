package everyday_one_leco;
/**
 * 有 n 个盒子。给你一个长度为 n 的二进制字符串 boxes ，其中 boxes[i] 的值为 '0' 表示第 i 个盒子是 空 的，而 boxes[i] 的值为 '1' 表示盒子里有 一个 小球。

在一步操作中，你可以将 一个 小球从某个盒子移动到一个与之相邻的盒子中。第 i 个盒子和第 j 个盒子相邻需满足 abs(i - j) == 1 。注意，操作执行后，某些盒子中可能会存在不止一个小球。

返回一个长度为 n 的数组 answer ，其中 answer[i] 是将所有小球移动到第 i 个盒子所需的 最小 操作数。

每个 answer[i] 都需要根据盒子的 初始状态 进行计算。

 

示例 1：

输入：boxes = "110"
输出：[1,1,3]
解释：每个盒子对应的最小操作数如下：
1) 第 1 个盒子：将一个小球从第 2 个盒子移动到第 1 个盒子，需要 1 步操作。
2) 第 2 个盒子：将一个小球从第 1 个盒子移动到第 2 个盒子，需要 1 步操作。
3) 第 3 个盒子：将一个小球从第 1 个盒子移动到第 3 个盒子，需要 2 步操作。将一个小球从第 2 个盒子移动到第 3 个盒子，需要 1 步操作。共计 3 步操作。
示例 2：

输入：boxes = "001011"
输出：[11,8,5,4,3,4]


题解：
核心思路：[前缀和思想](https://juejin.cn/post/7005057884555837476)

先计算出第一个盒子的最小操作数operations
那么第二个盒子的最小操作数，就是在第一个盒子的最小操作数operations上进行加和减。

那么加和减维持这什么样的关系？

比如：boxes = "001011"
     第0位盒子，最小操作数为 11=5+4+3
     第1位盒子，最小操作数为 8=11-3 （减3，是核心。第1位盒子相对于第0位盒子右移一位，也就是右边有球的3个盒子每个盒子向第1位盒子移动就要比向第0位盒子移动少1步操作）

     同理:移动过程中要考虑左边盒子，左边盒子则是增加移动步数

最后总结核心公式：operations[i] = operations[i-1] + left_1_count - right_1_count

 */

public class minOperationsSolution {
    public int[] minOperations(String boxes) {
        int right = 0, operations = 0;
        int n = boxes.length();
        for (int i = 1; i < n; i++) {
            if (boxes.charAt(i) == '1') {
                right++;
                operations += i;
            }
        }
        int[] res = new int[n];
        res[0] = operations;
        // 从计算第1位操作步数开始，就需要统计左侧1的个数了
        int left = Integer.valueOf(boxes.charAt(0));
        for (int i = 1; i < n; i++) {
            operations += left - right;
            if (boxes.charAt(i) == '1') {
                left++;
                right--;
            }
            res[i] = operations;
        }
        return res;
    }

    public static void main(String[] args) {
        String boxes = "110";
        minOperationsSolution solution = new minOperationsSolution();
        int[] res = solution.minOperations(boxes);
        System.out.println(res);
    }
}
