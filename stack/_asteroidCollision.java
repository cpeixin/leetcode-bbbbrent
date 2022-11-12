import java.util.ArrayDeque;
import java.util.Deque;

/*
 * @Author: congpeixin congpeixin@dongqiudi.com
 * @Date: 2022-11-10 08:48:44
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-11-12 10:00:31
 * @FilePath: /leetcode-bbbbrent/stack/_asteroidCollision.java
 * @Description: 给定一个整数数组 asteroids，表示在同一行的行星。

对于数组中的每一个元素，其绝对值表示行星的大小，正负表示行星的移动方向（正表示向右移动，负表示向左移动）。每一颗行星以相同的速度移动。

找出碰撞后剩下的所有行星。碰撞规则：两个行星相互碰撞，较小的行星会爆炸。如果两颗行星大小相同，则两颗行星都会爆炸。两颗移动方向相同的行星，永远不会发生碰撞。

 

示例 1：

输入：asteroids = [5,10,-5]
输出：[5,10]
解释：10 和 -5 碰撞后只剩下 10 。 5 和 10 永远不会发生碰撞。


示例 2：

输入：asteroids = [8,-8]
输出：[]
解释：8 和 -8 碰撞后，两者都发生爆炸。
示例 3：

输入：asteroids = [10,2,-5]
输出：[10]
解释：2 和 -5 发生碰撞后剩下 -5 。10 和 -5 发生碰撞后剩下 10 。
 

提示：

2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0

   此题解法选择
   eg. 4,5,-6 三颗行星
       4向右，暂时不发生碰撞
       5向右，暂时不发生碰撞
       -6向左，发生碰撞，而且和相邻的5发生碰撞！！！ |-6| > 5 所以 5 弹射出栈！！，这里体现了后入先出的特性，以及符合【最近相关性】
       所以选择【栈】来实现

    解法细节：
    首先是行星的遍历入栈
    这道题的关键点在于遍历条件：
    起初思考大意，以为当栈顶行星和正在准备入栈行星之间的符号相反时，就会发生碰撞💥，其实不然，这里也要分两种情况的。
        1. 当初次入栈或者栈顶元素符号为负数，则不用考虑行星碰撞。
            （1）因为当栈为空时，负号行星入栈直接向右飞，不用考虑后续行星的符号问题。
             (2)当栈顶行星为负数行星时，证明栈底其他行星也肯定是负数行星，这时飞入行星无论为正负，都不会与栈顶负数行星发生碰撞。
        2. 当栈顶行星为正数，正在飞入行星为负数时，则会发生碰撞。

    这里还要引入一个布尔变量flying_asteroid_alive，来判断正在飞行的行星每次碰撞后，是否还存在，对于此飞行行星是否继续遍历碰撞，是否入栈作为条件。

    题解： https://leetcode.cn/problems/asteroid-collision/solution/zui-jin-xiang-guan-xing-by-bbbbrent-5x10/
 */
public class _asteroidCollision {
    public int[] asteroidCollision(int[] asteroids) {
        // 特例判断
        if (asteroids.length == 0 || asteroids.length == 1)
            return asteroids;

        // 创建栈
        Deque<Integer> asteroids_stack = new ArrayDeque<Integer>();

        for (int flying_asteroid : asteroids) {
            // 正在飞行的行星是否还存在
            boolean flying_asteroid_alive = true;
            // 注意：!asteroids_stack.isEmpty()条件要放在前面
            while (flying_asteroid_alive && !asteroids_stack.isEmpty() && flying_asteroid < 0
                    && asteroids_stack.peekLast() > 0) {
                flying_asteroid_alive = asteroids_stack.peekLast() < -flying_asteroid;
                if (asteroids_stack.peekLast() <= -flying_asteroid) {
                    // 栈顶行星质量小于飞进来的行星，栈顶行星出栈
                    asteroids_stack.pollLast();
                }
            }
            if (flying_asteroid_alive) {
                asteroids_stack.addLast(flying_asteroid);
            }
        }
        return asteroids_stack.stream().mapToInt(x -> x).toArray();
    }

    public static void main(String[] args) {
        int[] asteroids = { 10, 2, -5 };
        _asteroidCollision solution = new _asteroidCollision();
        int[] res = solution.asteroidCollision(asteroids);
        System.out.println(res);

        for (int i : res) {
            System.out.println(i);
        }
    }
}
