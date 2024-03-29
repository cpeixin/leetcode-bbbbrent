import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;

/*
 * @Author: congpeixin congpeixin@dongqiudi.com
 * @Date: 2022-11-14 09:17:08
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-11-17 09:12:51
 * @FilePath: /leetcode-bbbbrent/stack/nextGreaterElementSolution.java
 * @Description: nums1 中数字 x 的 下一个更大元素 是指 x 在 nums2 中对应位置 右侧 的 第一个 比 x 大的元素。

给你两个 没有重复元素 的数组 nums1 和 nums2 ，下标从 0 开始计数，其中nums1 是 nums2 的子集。

对于每个 0 <= i < nums1.length ，找出满足 nums1[i] == nums2[j] 的下标 j ，并且在 nums2 确定 nums2[j] 的 下一个更大元素 。如果不存在下一个更大元素，那么本次查询的答案是 -1 。

返回一个长度为 nums1.length 的数组 ans 作为答案，满足 ans[i] 是如上所述的 下一个更大元素 。

 

示例 1：

输入：nums1 = [4,1,2], nums2 = [1,3,4,2].
输出：[-1,3,-1]
解释：nums1 中每个值的下一个更大元素如下所述：
- 4 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。
- 1 ，用加粗斜体标识，nums2 = [1,3,4,2]。下一个更大元素是 3 。
- 2 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。


核心逻辑类似于 ”每日温度“

nums1是nums2的子集，并且求得是nums1中元素，在nums2中相应下一个最大值


时间复杂度：O(m + n)

O(m+n)，其中 mm 是 \textit{nums}_1nums 
1
​
  的长度，nn 是 \textit{nums}_2nums 
2
​
  的长度。我们需要遍历 \textit{nums}_2nums 
2
​
  以计算 \textit{nums}_2nums 
2
​
  中每个元素右边的第一个更大的值；需要遍历 \textit{nums}_1nums 
1
​
  以生成查询结果。

空间复杂度：O(n)
O(n)，用于存储哈希表。

 */
public class nextGreaterElementSolution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int[] res1 = new int[nums1.length];
        HashMap<Integer, Integer> nums2Map = new HashMap<Integer, Integer>();
        Deque<Integer> stack = new ArrayDeque<Integer>();

        for (int i = 0; i < nums2.length; i++) {
            while (!stack.isEmpty() && nums2[stack.peekLast()] < nums2[i]) {
                int pre_index = stack.pollLast();
                nums2Map.put(nums2[pre_index], nums2[i]);
            }
            stack.addLast(i);
        }

        for (int j = 0; j < nums1.length; j++) {
            res1[j] = (int) nums2Map.getOrDefault(nums1[j], -1);
        }

        return res1;
    }

    public static void main(String[] args) {
        int[] nums1 = { 4, 1, 2 };
        int[] nums2 = { 1, 3, 4, 2 };
        nextGreaterElementSolution solution = new nextGreaterElementSolution();

        int[] res = solution.nextGreaterElement(nums1, nums2);
        // System.out.println(res);

        for (int i = 0; i < res.length; i++) {
            System.out.println(res[i]);
        }
    }
}
