class Stack:
    # 初始化
    def __init__(self):
        self.items = []

    # 判断是否为空
    def isEmpty(self):
        return self.items == []

    # 压入一个数据
    def push(self, item):
        self.items.append(item)

    # 将栈顶数据弹出
    def pop(self):
        return self.items.pop()

    # 返回栈顶数据，但不弹出
    def peek(self):
        return self.items[len(self.items) - 1]

    # 返回栈的长度
    def size(self):
        return len(self.items)
