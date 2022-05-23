#接BinarySearchTree.py中delete

# 找到呆删除节点后，分三种情况：（1）待删除节点没有子节点；（2）待删除节点有一个子节点；（3）待删除节点有两个子节点
# Code_6.30 情况（1）
if currentNode.isLeaf():
    if currentNode == currentNode.parent.leftChild:
        currentNode.parent.leftChild = None
    else:
        currentNode.parent.rightChild = None

#Code_6.32 情况（3）
elif currentNode.hasBothChildren():
    succ = currentNode.findSuccessor()
    succ.spliceOut()
    currentNode.key = succ.key
    currentNode.payload = succ.payload

#Code_6.31 情况（2）
else:
    if currentNode.hasLeftChild(): #待删除节点有一个左子节点
        if currentNode.isLeftChild(): #待删除节点为某一节点的左子节点
            currentNode.leftChild.parent = currentNode.parent
            currentNode.parent.leftChild = currentNode.leftChild
        elif currentNode.isRightChild(): #待删除节点为某一节点的右子节点
            currentNode.leftChild.parent = currentNode.parent
            currentNode.parent.rightChild = currentNode.leftChild
        else: #待删除节点为根节点
            currentNode.replaceNodeData(currentNode.leftChild.key, currentNode.leftChild.payload,
                                        currentNode.leftChild.leftChild, currentNode.leftChild.rightChild)
    else: #待删除节点有一个右子节点
        if currentNode.isLeftChild(): #待删除节点为某一节点的左子节点
            currentNode.rightChild.parent = currentNode.parent
            currentNode.parent.leftChild = currentNode.rightChild
        elif currentNode.isRightChild(): #待删除节点为某一节点的右子节点
            currentNode.rightChild.parent = currentNode.parent
            currentNode.parent.rightChild = currentNode.rightChild
        else: #待删除节点为根节点
            currentNode.replaceNodeData(currentNode.rightChild.key, currentNode.rightChild.payload,
                                        currentNode.rightChild.leftChild, currentNode.rightChild.rightChild)

#Code_6.33 寻找后继节点
def findSuccessor(self):
    succ = None
    if self.hasRightChild():
        succ = self.rightChild.findMin()
    else:
        if self.parent:
            if self.isLeftChild():
                succ = self.parent
            else:
                self.parent.rightChild = None
                succ = self.parent.findSuccessor()
                self.parent.rightChild = self
    return succ

def findMin(self):
    current = self
    while current.hasLeftChild():
        current = current.leftChild
    return current

#Code_6.34 spliceOut方法，移除待删除节点
def spliceOut(self):
    if self.isLeaf():
        if self.isLeftChild():
            self.parent.leftChild = None
        else:
            self.parent.rightChild = None
    elif self.hasAnyChildren():
        if self.hasLeftChild():
            if self.isLeftChild():
                self.parent.leftChild = self.leftChild
            else:
                self.parent.rightChild = self.leftChild
            self.leftChild.parent = self.parent
        else:
            if self.isLeftChild():
                self.parent.leftChild = self.rightChild
            else:
                self.parent.rightChild = self.rightChild
            self.rightChild.parent = self.parent