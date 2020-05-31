class Node:
    def __init__(self,value, left_child_node=None, right_child_node=None):
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










if __name__ == '__main__':
    tree = BinarySearchTree(33, Node(16, Node(13,right_child_node=Node(15)), Node(18,Node(17),right_child_node=Node(25, Node(19), Node(27)))), Node(50, Node(34), Node(58, Node(51), Node(66))))
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

    max = tree.find_max(tree.root)

    print(max.value)





