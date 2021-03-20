<a name="FEymP"></a>
### 大纲
- Trie
- 并查集


<br />
<br />Trie 树的本质，就是利用字符串之间的公共前缀，将重复的前缀合并在一起<br />
![截屏2020-07-21 上午10.34.31.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1595299387148-b353a37e-eb37-4738-b4fd-97f75e2042e7.png#align=left&display=inline&height=372&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-07-21%20%E4%B8%8A%E5%8D%8810.34.31.png&originHeight=372&originWidth=1392&size=239614&status=done&style=none&width=1392)
![截屏2020-07-21 上午10.25.21.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1595298824025-e676663e-6fd4-408e-aa31-6ee060d9ba60.png#align=left&display=inline&height=702&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-07-21%20%E4%B8%8A%E5%8D%8810.25.21.png&originHeight=702&originWidth=1418&size=641905&status=done&style=none&width=1418)<br />
<br />![截屏2020-07-21 上午10.20.22.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1595299396299-a32d3257-f5d0-4bbe-a7da-dd21533f10e6.png#align=left&display=inline&height=716&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-07-21%20%E4%B8%8A%E5%8D%8810.20.22.png&originHeight=716&originWidth=1458&size=289414&status=done&style=none&width=1458)<br />
<br />向 Trie 树中插入键<br />我们通过搜索 Trie 树来插入一个键。我们从根开始搜索它对应于第一个键字符的链接。有两种情况：<br />
<br />链接存在。沿着链接移动到树的下一个子层。算法继续搜索下一个键字符。<br />链接不存在。创建一个新的节点，并将它与父节点的链接相连，该链接与当前的键字符相匹配。<br />重复以上步骤，直到到达键的最后一个字符，然后将当前节点标记为结束节点，算法完成。<br />![截屏2020-07-21 下午2.56.21.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1595314794942-3f6c475b-d68d-48f4-a041-fe29cdcf6f67.png#align=left&display=inline&height=1134&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-07-21%20%E4%B8%8B%E5%8D%882.56.21.png&originHeight=1134&originWidth=1176&size=442788&status=done&style=none&width=1176)<br />

<a name="JXKh2"></a>
### 题解


<a name="LhZMD"></a>
#### [实现 Trie (前缀树)](https://leetcode-cn.com/problems/implement-trie-prefix-tree/)
题解：实现一个 Trie (前缀树)，包含 `insert`, `search`, 和 `startsWith` 这三个操作。<br />
<br />代码：
```python
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end_word = False
class Trie:
    def __init__(self):
        # 初始化根节点
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for char in word:
            # node 不断的指向下一级
            node = node.children[char]
        node.is_end_word = True
        
    def search(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                # 如果这个字符存在，那么node指向下一级，继续遍历下一级字符
                node = node.children[char]
            else: return False
        return node.is_end_word
        
    def startwith(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else: return False
        return True
        
```
**复杂度分析：**<br />**插入操作**

- 时间复杂度：O(m)，其中 m 为键长。在算法的每次迭代中，我们要么检查要么创建一个节点，直到到达键尾。只需要 m 次操作。
- 空间复杂度：O(m)。最坏的情况下，新插入的键和 Trie 树中已有的键没有公共前缀。此时需要添加 mm 个结点，使用 O(m) 空间。


<br />**查找操作**

- 时间复杂度 : O(m)。算法的每一步均搜索下一个键字符。最坏的情况下需要 m 次操作。
- 空间复杂度 : O(1)。


<br />**查找前缀**

- 时间复杂度 : O(m)。
- 空间复杂度 : O(1)。


<br />**总结：其实设计的原理和链表差不多，只不过Trie中使用字典来实现嵌套关系，不怎么容易被接受。**
> python里面, `list`, `dict`, `set`都是可变类型的，`int`, `string`,`tuple`是不可变类型，比如`t1 = t2 = {'a':1, 'b':2}`里面`t1`,`t2`指向同一个内存地址:`id(t1) = id(t2)`， `t1.update(b=2)`之后`t2`跟着改变，因为`t1`修改了同一个内存地址的数据；但是如果`t1=t2=100`, `t2+=200`，那么`t1`还是`100`，而且`t1`,`t2`指向不同的内存地址了；

**<br />**还有一点就是对python **defaultdict() , dict{}  数据结构不了解造成的困扰<br />defaultdict()： children[char] 返回的是 char对应的value值<br />dict{} ：node.setdefault(char, {})  返回的也是char对应的value值<br />
<br />

<a name="s2GWY"></a>
#### [单词搜索 II](https://leetcode-cn.com/problems/word-search-ii/)
**题解：**<br />给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。<br />单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。<br />示例:<br />输入: <br />words = ["oath","pea","eat","rain"] and board =<br />[<br />  ['o','a','a','n'],<br />  ['e','t','a','e'],<br />  ['i','h','k','r'],<br />  ['i','f','l','v']<br />]<br />输出: ["eat","oath"]<br />
<br />**解题关键： 字典树+DFS**<br />**将words构建成字典树，随后在board中遍历每个字符以及字符的水平相邻垂直相邻的字符，进行DFS**<br />![截屏2020-07-22 上午8.03.15.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1595376747112-4008b990-1062-41d4-9c1a-ac0810e7f15e.png#align=left&display=inline&height=762&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-07-22%20%E4%B8%8A%E5%8D%888.03.15.png&originHeight=762&originWidth=1554&size=173720&status=done&style=none&width=1554)

代码：
```python
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}  # 构造字典树
        for word in words:
            node = trie
            for char in word:
                """!!!setdefault:如果字典中包含有给定键，则返回该键对应的值，否则返回为该键设置的值。
                    node.setdefault(char, {}) 返回的是 char对应的value值，而不是整个node
                """
                node = node.setdefault(char, {})

            node['#'] = True

        def search(i, j, node, pre, visited):  # (i,j)当前坐标，node当前trie树结点，pre前面的字符串，visited已访问坐标
            if '#' in node:  # 已有字典树结束
                res.add(pre)  # 添加答案
            for (di, dj) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                _i, _j = i + di, j + dj
                if -1 < _i < h and -1 < _j < w and board[_i][_j] in node and (_i, _j) not in visited:  # 可继续搜索
                    search(_i, _j, node[board[_i][_j]], pre + board[_i][_j], visited | {(_i, _j)})  # dfs搜索, 取并集 visited | {(_i, _j)}

        res, h, w = set(), len(board), len(board[0])
        for i in range(h):
            for j in range(w):
                if board[i][j] in trie:  # 可继续搜索
                    search(i, j, trie[board[i][j]], board[i][j], {(i, j)})  # dfs搜索
        return list(res)
```
复杂度分析：<br />![截屏2020-07-22 上午9.20.42.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1595380918532-21145d73-2935-4ff4-ada4-b2bceb4c95e5.png#align=left&display=inline&height=1494&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-07-22%20%E4%B8%8A%E5%8D%889.20.42.png&originHeight=1494&originWidth=1576&size=418320&status=done&style=none&width=1576)<br />总结：<br />**
