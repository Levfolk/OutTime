#树的后序遍历
import operator

#Code_6.13 后序遍历函数


def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

#Code_6.14 后序求值函数
def postordereval(tree):
    opers = {'+' : operator.add, '-' : operator.sub, '*' : operator.mul, '/' : operator.truediv}
    res1 = None
    res2 = None
    if tree:
        res1 = postordereval(tree.getLeftChild())
        res2 = postordereval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1, res2)
        else:
            return tree.getRootVal()