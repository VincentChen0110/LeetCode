def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
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
    
    ## WithoutHashMap
    # https://leetcode.com/problems/copy-list-with-random-pointer/discuss/1059384/Python-Optimal-2-pass-O(1)-space-w-diagram-%2B-explanation
    if not head: return
    
    copy = preroot = Node(-1,head,None)
    
    while head:
        orig_next = head.next
        head.next = copy.next = Node(head.val, None, head.random)
        head, copy = orig_next, copy.next
    
    copy = preroot.next
    
    while copy:
        if copy.random!=None:
            copy.random = copy.random.next
        copy = copy.next
    
    return preroot.next