def pairSum(self, head):
    """
    :type head: Optional[ListNode]
    :rtype: int
    """
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    
    prev = None
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt
        
    max_now = -float('inf')
    while prev:
        max_now = max(max_now, prev.val+head.val)
        prev = prev.next
        head = head.next
    return max_now