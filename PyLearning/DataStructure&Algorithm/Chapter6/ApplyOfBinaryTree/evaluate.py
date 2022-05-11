#Code_6.10 计算二叉解析树的递归函数
import operator  #opers定义中需要用到

def evaluate(parseTree):
    opers = {'+' : operator.add, '-' : operator.sub, '*' : operator.mul, '/' : operator.truediv}
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootVal()