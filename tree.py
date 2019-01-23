
class Node(object):
    def __init__(self,index):
        self.index = index
        self.left_child = None
        self.right_child = None


class BinaryTree(object):
    def __init__(self,root):
        self.root = root

    def pre_travel(self,node):
        if not node:
            return
        print(node.index)
        self.pre_travelTree(node.left_child)
        self.pre_travelTree(node.right_child)

node_dict = []
for i in range(1,10):
    node_dict[i] = node(i)

node_dict[1].left_child = node_dict[2]