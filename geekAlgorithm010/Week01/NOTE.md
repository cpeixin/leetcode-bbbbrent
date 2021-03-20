

<a name="zAMBQ"></a>
### 复杂度
|  | array | linked list | skip list | stack | queue |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 查找-时间复杂度 | O(1) | O(n) | O(logn) | O(n) | O(n) |
| 插入-时间复杂度 | O(n) | O(1) | O(logn) | O(1) | O(1) |
| 删除-时间复杂度 | O(n) | O(1) | O(logn) | O(1) | O(1) |




---

<a name="3SZ8A"></a>
### 工程中的应用


- LRU Cache - 链表
- SkipList - Redis set

---

<a name="Gz2z7"></a>
### 跳表的核心思想


- 升维
- 空间换时间

---

<a name="ZVcxe"></a>
### 解题思路


<a name="5Fqeq"></a>
#### 移动零
两次遍历<br />第一次先把所有非0元素往前移 记录下标位置<br />第二次遍历直接把下标往后的元素全部置为0<br />
<br />**关于p的位置**，我Debug看流程，调试了几遍才看懂
```python
for i in range(len(nums)):    
    if nums[i] != 0:       
        nums[p] = nums[i]       
        p += 1        
for j in range(p, len(nums)):
```


这里我总结，对于数组问题，遍历是不可少的，其中要注意遍历的长度以及遍历的起始点问题。例如老师下面强调过的代码
```python
for i in range(len(list)-1):
    for j in range(i+1, len(list)):
```


<a name="thv0O"></a>
#### 盛最多水的容器
当然也可以用枚举来做，但是时间复杂度太高。O(n^2)<br />一个技巧点：**左右夹逼**，也就是使用双指针，根据左右指针对应数值大小，动态移动，再向中间靠拢<br />

<a name="gTFAp"></a>
#### 爬楼梯
很难想到用斐波那契数列，我其实还不知道斐波那契数列是什么。后来搞懂了斐波那契数列后，感觉如果以后再次碰到题目中有类似于 f(n) = f(n-1)+f(n-2)  ,也就是如果第n步的结果，等于n-1和n-2步骤和的情况下，可以套入斐波那契数列。
```python
1，1，2，3，5，8，13......
```


<a name="nMc1G"></a>
#### 三数之和
这道题之前，还有一道【两数之和】，两数之和的巧妙解法是利用了 HashMap来辅助存储（也就是老师讲到的"**空间换时间**"）<br />
<br />**【三数之和】解题有三个巧妙点：**

- a+b+c=0   转化成  a+b = -c
- 对数组先排序
- 单层遍历a+双指针(b,c)左右夹逼，双指针动态向中间靠拢。


<br />**其中的细节点：**<br />

- 单层遍历 a
```python
for i in range(len(nums)-2)
```


- 双指针左右移动是根据 abc对应数字之和来决定
- a，b, c移动过程中，跳过相同元素（可选项）


<br />时间复杂度 O(N^2)：其中固定指针k循环复杂度 O(N)O(N)，双指针 i，j 复杂度 O(N)O(N)。<br />空间复杂度 O(1)：指针使用常数大小的额外空间。<br />

<a name="xe4Ta"></a>
#### 反转链表、环形链表
两道题都是基于遍历的方法<br />
<br />反转链表要复杂点在于 节点之间的next反转，借助临时节点来完成<br />
<br />环形链表的巧妙点在于 双指针-快慢指针。这里对于快指针，要再次前进两个节点时，注意None的判断
```python
 while slow_node != fast_node:
            # 这里的判断要记住
      if fast_node == None or fast_node.next == None:
             return False
      fast_node = fast_node.next.next
      slow_node = slow_node.next
```
**<br />
<br />**<br />不管是顺序栈还是链式栈，入栈、出栈只涉及栈顶个别数据的操作，所以时间复杂度都是 O(1)。<br />在入栈和出栈过程中，只需要一两个临时变量存储空间，所以空间复杂度是 O(1)

<a name="zHruP"></a>
#### 有效的括号

<br />解题巧妙点：单栈即可实现。此外借助 dict字典，char_dict = {"{":"}", "(":")", "[":"]"} 存储对应的符号。注意栈空情况下的判断，也可以使用哨兵节点，免去栈空的判断。

<a name="frf0J"></a>
#### 最小栈


此题读完题意，我一度以为需要自己手动根据API实现一个栈。但是init函数并没有给初始化数组的size，此时又考虑使用链表实现栈。但是对于链表栈，查询最小元素并不能在常数时间内完成。这时果断去看题解。

两个让我醒悟的点：

- 可以直接使用stack栈，无需自己实现，只是在规定接口内，实现功能即可。
- 关于最小值，借助辅助栈。（这一点也就是优化方法中的“空间换时间”，自己还是不能灵活运用啊～～）

<br />
<a name="04jHe"></a>
#### [滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum/)

<br />最简单，最容易想到的解法为什么总是暴力解法？？？？？<br />双层遍历，直接超出时间限制。

这里使用 空间换时间 的巧妙点在于使用双端队列：<br />
<br />双端队列和普通队列最大的不同在于，它允许我们在队列的头尾两端都能在 O(1) 的时间内进行数据的查看、添加和删除。<br />
<br />与队列相似，我们可以利用一个双链表实现双端队列。双端队列最常用的地方就是实现一个长度动态变化的窗口或者连续区间，而动态窗口这种数据结构在很多题目里都有运用。<br />
<br />双向队列的操作<br />[https://www.cnblogs.com/saolv/p/9839711.html](https://www.cnblogs.com/saolv/p/9839711.html)<br />
<br />![27af2b52e80803bcb7a8285dbd27cfa9292a6cf6dd0a6454454d6d3357da15c6-image.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1591893210515-ee122dc5-52cd-4bc5-bfd2-e3be0ec64534.png#align=left&display=inline&height=824&margin=%5Bobject%20Object%5D&name=27af2b52e80803bcb7a8285dbd27cfa9292a6cf6dd0a6454454d6d3357da15c6-image.png&originHeight=824&originWidth=1406&size=78263&status=done&style=none&width=1406)<br />
<br />虽然已经在审题10分钟后，直接去看了题解，但还是被这道题困扰了半天的时间，主要不懂的点在于窗口中，出队和入队的临界条件。deque[0] <= i-k  和  i>=k-1  分别是队列中窗口左临界点出队和第一个窗口的右临界点开始选择最大值。<br />
<br />后来还是放下浮躁的心，**手动在纸上debug流程，效果真的显著，真的显著！！！！**。在idea中分析流程总有着一种雾里看花的感觉。随后有手写了两边代码，又在leetcode上打了一遍，直接运行通过。<br />
<br />**时间复杂度：O(N)**，每个元素被处理两次- 其索引被添加到双向队列中和被双向队列删除。<br />
<br />**空间复杂度：O(N)**，输出数组使用了 O(N−k+1) 空间，双向队列使用了O(k)。<br />

<a name="0zSVK"></a>
#### 柱状图中最大的矩形

<br />看见这道题后，心里一阵欢喜，因为最先想到的不再是**暴力解法**了。而是双指针！！这是因为我想到了“<br />**盛最多水的容器**”这道题，但是开始写程序后，发现并不一样，盛最多水的容器这道题中的双指针移动可以不在乎中间节点的高低。想到这里，又陷入了懵逼～～～

看了下面的题解，类似与双指针的解法，反而是暴力解法😅<br />![截屏2020-06-12 上午12.46.33.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1591894036805-3dbec814-a8ce-4880-a524-a9fcf59bf8aa.png#align=left&display=inline&height=1494&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-06-12%20%E4%B8%8A%E5%8D%8812.46.33.png&originHeight=1494&originWidth=1562&size=271105&status=done&style=none&width=1562)

那么这道题优化的方向也是“空间换时间”，利用单调栈，维护一个单调递增的栈。这里要记录一下，关于为什么选择单调栈，我看了很多题解，都是说，此题的计算方式和单调栈的特性符合，所以此题选择单调栈。<br />
<br />单调栈是一个定义简单但应用起来比较复杂的数据结构，其根本应用可以概括为：在一个一维数组中，帮助我们找到某个元素的左侧或右侧第一个大于或小于该元素的数。

这题理解的关键在于，元素出栈，出栈的同时，则要计算了以它的顶为上边框的最大矩形。基于各个高度的最大矩形是在出栈的时候计算的，因此必须要让所有高度都出栈。这里是利用单调栈的性质让其全部出栈，即在原始数组后添一个0.

详细的讲解：<br />[https://blog.csdn.net/Zolewit/article/details/88863970](https://blog.csdn.net/Zolewit/article/details/88863970)<br />
<br />

<a name="az6q4"></a>
#### 删除排序数组中的重复项

<br />想到了双指针。。但是思维方向走向了左右夹逼方法，手写代码的时候，发现左右指针无法控制条件移动。<br />
<br />题解中的双指针，利用了**快慢针**的方法。<br />
<br />核心逻辑：
```python
if nums[slow_index] != nums[fast_index]:
	slow_index += 1
    nums[slow_index] = nums[fast_index]
```


<a name="7U7MF"></a>
#### 旋转数组

<br />此题基本上大家统一的解法就是三段反转。其中有些人取巧用python切片来实现，但是貌似就不满足要求使用空间复杂度为 O(1) 的 原地 算法了。<br />
<br />解题中有两点核心：

- k%n
- 数组的反转


<br /> k%n个尾部元素会被移动到头部，剩下的元素会被向后移动

数组的反转：
```python
def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start+=1
            end-=1
```

<br />

<a name="8M9Q6"></a>
#### 合并两个有序数组

<br />双指针，从后向前遍历，比较两个数组尾元素的大小<br />

<a name="clUBu"></a>
#### 合并两个有序链表

<br />递归递归递归～～～ 为什么我想不到递归，即使想到了递归，重复最小项也没有想到～～！！～～！！<br />

<a name="L1AB1"></a>
#### [验证回文串](https://leetcode-cn.com/problems/valid-palindrome/)

<br />此题利用双指针，栈，或者reverse都可以。其中对于初始字符串的处理可以优雅一些。
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = "".join(char.lower() for char in s if char.isalnum())
        n = len(str)
        left, right = 0, n-1
        while left<right:
            if str[left] != str[right]:
                return False
            left+=1
            right-=1
        return True
```



---

<a name="K9nMb"></a>
### 总结

<br />简单总结一下这周做的这些题用到的方法，慢慢积累，希望以后做的题多了，能总结出一些算法的套路，加油！<br />

- 左右夹逼

盛最多水的容器（数组） 三数之和（数组），回文串<br />

- 快慢指针

环形链表 删除排序数组中的重复项<br />

- 借助Map

两数之和  有效的括号<br />

- 单调栈

柱状图中最大的矩形
