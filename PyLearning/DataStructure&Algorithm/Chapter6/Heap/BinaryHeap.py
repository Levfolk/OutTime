#二叉堆的实现
class BinaryHeap:

#Code_6.17 新建二叉堆
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

#Code_6.18 percUP方法，为insert函数做准备
    def percUP(self, i):
        while i // 2 > 0: #若i的位置不位于根节点
            if self.heapList[i] < self.heapList[i // 2]:
                temp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = temp
                #self.heapList[i // 2], self.heapList[i] = self.heapList[i], self.heapList[i // 2]
            i = i // 2

#Code_6.19 insert函数，向二叉堆中加入新元素
    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUP(self.currentSize)

#Code_6,20 percDown方法和minChild方法，为delMin函数做准备
    def percDown(self, i):
        while(i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
                #self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

#Code_6.21 delMin函数，从二叉堆中删除最小的元素
    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

#Code_6.22 buildHeap函数，根据元素列表构建堆
    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while(i > 0):
            self.percDown(i)
            i = i - 1
