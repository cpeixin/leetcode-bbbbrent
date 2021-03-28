<a name="EIrHQ"></a>
### 心得总结
经历算法训练营这段时间的训练，先不说过程，直接看结果的话，那就是我对算法没有畏惧的感觉了，这也是我最欣慰的。<br />
<br />我是知道算法与数据结构重要的，当时百度来学校校招，就只是简简单单的考了一个冒泡排序，当时能答出来的基本都去百度实习了。从大学毕业到现在，我重启了四次数据结构与算法的学习，第一次，第二次没有买任何辅助课程，这两次都是从数组开始，再到链表，随后直接在栈和队列放弃了，那时不知道刷题的概念，只是看完相关知识点的概念就以为掌握了，真的太天真了。<br />
<br />第三次重启是在极客时间上买了王争老师《数据结构与算法》，这次按照课程大纲，一直的学下去，每天都会保证学习，而且每个结构通过王争老师的文字讲解，确实很容易的就吸收和记住了，这时信心满满的去leetcode做题检测一下，真的是当头一棒啊~~，原来做题和理解数据结构和算法并不是一回事。<br />
<br />第四次重启就是算法训练营了，也是感觉近几年学的最值的课程，第一节课覃超老师讲的五毒神掌，也就是五遍做题法，打破了我这么多年一直找不到原因的屏障。我想了各种怎么去学好数据结构与算法的方法，唯独没有去考虑一道题做N遍，这可能就是盲目的自信吧，一直以为自己可以用理解的方式去学会，不用过遍数也能畅游leetcode。覃超老师也在知乎上找了一些学算法的建议，其实也是想让我们放下固化的思维，能踏踏实实的去过边数，形成肌肉记忆👍👍。<br />

<a name="Wmg70"></a>
### 学习总结
<a name="NqDgw"></a>
#### 数组链表

- 左右夹逼

盛最多水的容器（数组） 三数之和（数组），回文串

- 快慢指针

环形链表 删除排序数组中的重复项

- 借助Map

两数之和  有效的括号

- 单调栈

柱状图中最大的矩形<br />

- 两数之和相关的题，考虑用哈希表
- 最小K，最大K值，考虑用堆或者快排。
- 关于递归，虽然多度几遍，就能看懂，但是执行的步骤则看着看着就乱了。下面有个带着分析过程的视频，个人感觉很好，能帮助理解。[https://www.bilibili.com/video/BV1g741137Wq?from=search&seid=8033860015351616278](https://www.bilibili.com/video/BV1g741137Wq?from=search&seid=8033860015351616278)



<a name="tAzYH"></a>
#### 回溯
回溯算法真的有套路的～～
```python
class Solution(object):
    def function(self, nums):
		if 特例条件: return []
		result = []
		def backtrack(路径, 选择列表):
    		if 满足结束条件:
        		result.add(路径)
        		return
    		for 选择 in 选择列表:
        		做选择
        		backtrack(路径, 选择列表)
        		撤销选择
        backtrack(....)# 初始化
        return result
```


<a name="IvGuc"></a>
#### 二分法
[团灭二分查找](https://github.com/cpeixin/leetcode-bbbbrent/blob/master/binary_search/%E5%9B%A2%E7%81%AD%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE.md)<br />

<a name="SMSJP"></a>
#### 深广度优先
DFS代码模版<br />[https://shimo.im/docs/UdY2UUKtliYXmk8t/read](https://shimo.im/docs/UdY2UUKtliYXmk8t/read)<br />BFS代码模板<br />[https://shimo.im/docs/ZBghMEZWix0Lc2jQ/read](https://shimo.im/docs/ZBghMEZWix0Lc2jQ/read)<br />
<br />

<a name="wX4U3"></a>
#### 动态规划
**模板**<br />**自底向上dp数组法**
```python
class solution:
    def userDefineFunction(self, nums or List[List[int]]):
        # 边界条件
        if not nums: return
        # 创建dp数组，根据题目，判断创建一维或者是二维dp数组
        # 一维 
        dp = [0 or float('-inf')] * len(nums) or len(nums)+1
        # 二维
        dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        
        # 初始化 有时可能需要对dp[0], dp[1]进行初始化
        dp[0] = 0
        
        for i in range(len(nums))
        or 
        for i in range(1, len(list)):
        	for h in range(len(list[0])):
                # ！！！dp方程！！！
                dp[i][j] = dp..............
        return dp[-1]
```
**对于有些可以进行空间优化的，一般都是当前状态只和前面一个或两个状态有关系的时候。**
```python
class solution:
    def userDefineFunction(self, nums or List[List[int]]):
        pre, cur = ...
        for num in nums:
            change(cur, pre)
            # eg:cur, pre = max(..), cur
        return cur
```

<br />**动态规划题目，一定要想清楚dp方程应该如何定义，首先应该考虑可不可以，题目让求什么，就将动态方程定义成什么~~，还有就是动态方程的逻辑，大多数情况需要我们利用填表法来找出规律，可以使一维的，可以是二维的，同时二维的情况下，有时候也可以用滚动数组法来降为一维的，降低空间复杂度。**<br />

<a name="4ajeO"></a>
### 结束
感谢覃超老师，真的感谢，改变了我对算法的态度，交给了我超级实用的方法，授人鱼不如授人以渔，这是覃超老师常说的，覃超老师不光指引了我怎么学习算法，我也将五毒法用在了其他学习中，简直不要太好用。同时也感谢我的助教-嘟嘟老师，期中考试后，嘟嘟老师的鼓励和学习方法的指导，给了我很大的信心和动力。<br />
<br />虽然现在还不是算法大牛，但是算法营的结束正是我算法之路的开始，加油💪<br />
<br />![截屏2020-08-23 下午12.08.35.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1598157064173-bb6bea59-f581-4675-accc-b45a1d7aa49b.png#align=left&display=inline&height=1704&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-08-23%20%E4%B8%8B%E5%8D%8812.08.35.png&originHeight=1704&originWidth=2404&size=483587&status=done&style=none&width=2404)
