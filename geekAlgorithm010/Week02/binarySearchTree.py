class Node:
    def __init__(self, value, left_child_node=None, right_child_node=None):
        self.value = value
        self.left_child_node = left_child_node
        self.right_child_node = right_child_node


class BinarySearchTree:
    def __init__(self, value, left_child_node=None, right_child_node=None):
        self.root = Node(value, left_child_node, right_child_node)

    def find_elem(self, value, node, parent_node, node_type):
        if node is None:
            return False, node, parent_node, node_type
        elif node.value == value:
            return True, node, parent_node, node_type
        elif value > node.value:
            return self.find_elem(value, node.right_child_node, node, "right_child_node")
        elif value < node.value:
            return self.find_elem(value, node.left_child_node, node, "left_child_node")

    def insert_elem(self, value):
        flag, node, parent_node, node_type = self.find_elem(value, self.root, self.root, None)
        if node_type == "left_child_node":
            parent_node.left_child_node = Node(value)
        else:
            parent_node.right_child_node = Node(value)

    def delete_elem(self, value):
        """Delete
        1). 无子节点
        2). 一个子节点
        3). 两个子节点
        """
        flag, node, parent_node, node_type = self.find_elem(value, self.root, self.root, None)
        if flag is False:
            return
        else:
            if node.left_child_node == None and node.right_child_node == None:
                if node_type == "left_child_node":
                    parent_node.left_child_node = None
                else:
                    parent_node.right_child_node = None

            elif node.left_child_node != None and node.right_child_node == None:
                parent_node.left_child_node = node.left_child_node
            elif node.left_child_node == None and node.right_child_node != None:
                parent_node.right_child_node = node.right_child_node
            else:
                min_node = self.find_min_node(node.right_child_node)
                self.delete_elem(min_node.value)
                if node_type == "left_child_node":
                    parent_node.left_child_node = min_node
                else:
                    parent_node.right_child_node = min_node
                min_node.left_child_node = node.left_child_node
                min_node.right_child_node = node.right_child_node

    def find_min_node(self, node):
        """查找最小值"""
        if node.left_child_node == None:
            return node
        else:
            return self.find_min_node(node.left_child_node)

    def find_max(self, root):
        if root.right_child_node is None:
            return root
        else:
            return self.find_max(root.right_child_node)

    def preTraverse(self, root):
        '''
        前序遍历
        中左右
        '''
        if root == None:
            return
        print(root.value)
        self.preTraverse(root.left_child_node)
        self.preTraverse(root.right_child_node)

    def midTraverse(self, root):
        '''
        中序遍历
        左中右
        '''
        if root == None:
            return
        self.midTraverse(root.left_child_node)
        print(root.value)
        self.midTraverse(root.right_child_node)

    def afterTraverse(self, root):
        '''
        后序遍历
        左右中
        '''
        if root == None:
            return
        self.afterTraverse(root.left_child_node)
        self.afterTraverse(root.right_child_node)
        print(root.value)

    def levelOrder(self, root):
        """
        层序遍历
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        res = []
        #       初始化队列
        queue = [root]
        while queue:
            parent_node = []
            next_level_node = []
            #遍历此层所有节点
            for node in queue:
                parent_node.append(node.value)
                #               获取下一层节点
                if node.left:
                    next_level_node.append(node.left_child_node)
                if node.right:
                    next_level_node.append(node.right_child_node)

            res.append(parent_node)
            queue = next_level_node
        return res

    def max_deep_num(self, root):
        """最大深度"""
        if not root:
            return 0
        left = self.max_deep_num(root.left_child_node) + 1
        right = self.max_deep_num(root.right_child_node) + 1
        return max(left, right)

    def min_deep_num(self, root):
        """最小深度"""
        if not root:
            return 0
        left = self.min_deep_num(root.left_child_node) + 1
        right = self.min_deep_num(root.right_child_node) + 1
        return min(left, right)


    def isSymmetric_recursion(self, root):
        """对称二叉树 递归解法"""
        if not root: return True
        return self.isSymmetricTree(root.left_child_node, root.right_child_node)

    def isSymmetricTree(self, left, right):
        if left is None and right is None: return True  # 同时为空
        if left is None or right is None: return False  # 一个为空
        if left.value != right.value: return False  # 值不相等 ！！
        # 这里就是left节点和right节点相同了。
        return self.isSymmetricTree(left.left_child_node, right.right_child_node) and self.isSymmetricTree(left.right_child_node, right.left_child_node)


    def isSymmetric_iteration(self, root):
        """对称二叉树 迭代解法"""
        """
        		:type root: TreeNode
        		:rtype: bool
        		"""
        if not root or not (root.left_child_node or root.right_child_node):
            return True
        # 用队列保存节点
        queue = [root.left_child_node, root.right_child_node]
        while queue:
            # 从队列中取出两个节点，再比较这两个节点
            left = queue.pop(0)
            right = queue.pop(0)
            # 如果两个节点都为空就继续循环，两者有一个为空就返回false
            if not (left or right):
                continue
            if not (left and right):
                return False
            if left.value != right.value:
                return False
            # 将左节点的左孩子， 右节点的右孩子放入队列
            queue.append(left.left_child_node)
            queue.append(right.right_child_node)
            # 将左节点的右孩子，右节点的左孩子放入队列
            queue.append(left.right_child_node)
            queue.append(right.left_child_node)
        return True

    def hasPathSum(self, root, sum):
        """路径和"""
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        sum -= root.value
        if not root.left_child_node and not root.right_child_node:  # 检测，当到达叶子节点时，判断sum是否为0
            return sum == 0
        return self.hasPathSum(root.left_child_node, sum) or self.hasPathSum(root.right_child_node, sum)

    def hasPathSum_Iterator(self, root, sum):
        """
        路径和
                :type root: TreeNode
                :type sum: int
                :rtype: bool
        """
        if not root:
            return False

        de = [(root, sum - root.value), ]
        while de:
            node, curr_sum = de.pop()
            if not node.left_child_node and not node.right_child_node and curr_sum == 0:
                return True
            if node.right_child_node:
                de.append((node.right_child_node, curr_sum - node.right_child_node.value))
            if node.left_child_node:
                de.append((node.left_child_node, curr_sum - node.left_child_node.value))
        return False

    def in_post_order(self):
        def buildTree(self, inorder, postorder):
            self.memo = {val: idx for idx, val in enumerate(inorder)}
            self.post = postorder
            root = self.helper(0, len(inorder) - 1, 0, len(self.post) - 1)
            return root

        def helper(self, istart, iend, pstart, pend):
            if istart > iend or pstart > pend:
                return None
            root = self.post[pend]  # 获取根结点的val
            ri = self.memo[root]  # 获取根结点的索引
            node = Node(self.post[pend])
            node.left = self.helper(istart, ri - 1, pstart, pstart + ri - istart - 1)
            node.right = self.helper(ri + 1, iend, pstart + ri - istart, pend - 1)
            return node




def test():
    list1 = [2, 3]

    list1.reverse()
    list2 = [3, 2]
    print(list1)
    # if list1.reverse() == list2:
    #     print("okokok")
    # else:
    #     print("nono")


if __name__ == '__main__':
    tree = BinarySearchTree(33, Node(16, Node(13, right_child_node=Node(15)),
                                     Node(18, Node(17), right_child_node=Node(25, Node(19), Node(27)))),
                            Node(50, Node(34), Node(58, Node(51), Node(66))))
    tree_2 = BinarySearchTree(1, Node(2, Node(3), Node(4)), Node(2, Node(4), Node(3)))

    tree_3 = BinarySearchTree(5, Node(4, Node(11, Node(7), Node(2))), Node(8, Node(13), Node(4)))
    # flag, *rest = tree.find_elem(19, tree.root, tree.root, None)
    # print(flag, rest[0].value, rest[1].value, rest[2])

    # tree.insert_elem(100)
    # flag, *rest = tree.find_elem(100, tree.root, tree.root, None)
    # print(flag, rest[0].value, rest[1].value, rest[2])

    # tree.delete_elem(18)
    """
                               33
                      /                  \
                    16                    50
                  /    \                 /   \
                13     18              34    58
                  \    / \                   / \
                  15  17  25                51  66
                          / \                 \ 
                        19  27                 55
    
    
    """

    # print("前序")
    # tree.preTraverse(tree.root)
    # print("中序")
    # tree.midTraverse(tree.root)
    # print("后序")
    # tree.afterTraverse(tree.root)

    # max = tree.find_max(tree.root)
    #
    # print(max)
    #
    # depth = tree.max_deep_num(tree.root)
    # print(depth)

    # depth = tree.min_deep_num(tree.root)
    # print(depth)

    # result = tree_2.symmetric(tree_2.root)
    # print(result)

    # test()

    # tree_2.isSymmetric_iteration(tree_2.root)

    tree_3.hasPathSum_Iterator(tree_3.root, 22)