class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        '''哈希表方法
        if not head:
            return None
        dic = {}
        cur = head
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            cur = cur.next

        return dic[head]'''

        #拼接拆分方法，空间复杂度只有O(1)
        if not head:
            return None

        #复制节点并拼接到原始节点后
        cur = head
        while cur:
            temp = Node(cur.val)
            temp.next = cur.next
            cur.next = temp
            cur = temp.next

        #构建新节点的random指向
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        #拆分两个链表
        cur = res = head.next
        pre = head
        while cur.next:
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
        pre.next = None

        return res
