from sys import *

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def recur(cur, pre):
            if not cur: return pre  # 终止条件
            res = recur(cur.next, cur)  # 递归后继节点
            cur.next = pre  # 修改节点引用指向
            return res  # 返回反转链表的头节点

        return recur(head, None)  # 调用递归并返回

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

head = node1

node1.next = node2
node2.next = node3
node3.next = None
while head:
    print(head.val)
    head = head.next

A = Solution()
A.reverseList(node1)

asd = node3
while asd:
    print(asd.val)
    asd = asd.next


