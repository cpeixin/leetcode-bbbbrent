import java.util.ArrayDeque;
import java.util.Deque;

/*
 * @Author: congpeixin congpeixin@dongqiudi.com
 * @Date: 2022-11-10 08:48:44
 * @LastEditors: congpeixin congpeixin@dongqiudi.com
 * @LastEditTime: 2022-11-11 18:54:04
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

   这题符合【最近相关性】
   eg. 4,5,-6 三颗行星
       4向右，暂时不发生碰撞
       5向右，暂时不发生碰撞
       -6向左，发生碰撞，而且和相邻的5发生碰撞！！！ |-6| > 5 所以 5 弹射出栈！！，这里体现了后入先出的特性，所以选择【栈】来实现
 */
public class _asteroidCollision {
    public int[] asteroidCollision(int[] asteroids) {
        // 特例判断
        if (asteroids.length == 0 || asteroids.length == 1)
            return asteroids;

        // 创建栈
        Deque<Integer> asteroids_stack = new ArrayDeque<Integer>();

        for (int i = 0; i < asteroids.length; i++) {
            // 正在飞行的行星
            int flying_asteroid = asteroids[i];
            // 正在飞行的行星时候还存在
            boolean flying_asteroid_alive = true;
            while(flying_asteroid_alive && flying_asteroid < 0 && asteroids_stack.peek() > 0 && !asteroids_stack.isEmpty()){
                flying_asteroid_alive = asteroids_stack.peek() < -flying_asteroid;
                if(asteroids_stack.peek() <= -flying_asteroid){
                    // 栈顶行星质量小于飞进来的行星，栈顶行星出栈
                    asteroids_stack.poll();
                }
            }
            asteroids_stack.push(flying_asteroid);

        }
        return asteroids_stack.stream().mapToInt(x -> x).toArray();

    }

    public static void main(String[] args) {
        int[] asteroids = {4,5,-6};
        _asteroidCollision solution = new _asteroidCollision();
        int[] res = solution.asteroidCollision(asteroids);
        System.out.println(res);

        for(int i: res) {
            System.out.println(i);
        }
    }
}
