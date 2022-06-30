def copyRandomList(self, head):
    """
    :type head: Node
    :rtype: Node
    """
    # Solution1: Time O(2n)
    # dic = {}
    # m = n = head
    # while m:
    #     dic[m] = Node(m.val)
    #     m = m.next
    # while n:
    #     dic[n].next = dic.get(n.next)
    #     dic[n].random = dic.get(n.random)
    #     n = n.next
    # return dic.get(head)
    # Solution1: Time O(n)
    dic = collections.defaultdict(lambda: RandomListNode(0))
    dic[None] = None
    n = head
    while n:
        dic[n].label = n.label
        dic[n].next = dic[n.next]
        dic[n].random = dic[n.random]
        n = n.next
    return dic[head]