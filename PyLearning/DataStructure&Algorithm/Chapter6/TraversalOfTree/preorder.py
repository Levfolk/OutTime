#树的前序遍历

#Code_6.11 将前序遍历算法实现为外部函数（将二叉树作为参数）
def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

#Code_6.12 将前序遍历算法实现为BinaryTree类的方法
def preorder1(self):
    print(self.key)
    if self.leftChild:
        self.left.preorder()
    if self.rightChild:
        self.right.preorder()