def isPalindrome(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    # vals = []
    # while head:
    #     vals.append(head.val)
    #     head = head.next
    # return vals == vals[::-1]
    fast = slow = head
    # find the mid node
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    
    prev = None
    while slow:
        cur = slow.next
        slow.next = prev
        prev = slow
        slow = cur   

    while prev:
        if prev.val!= head.val:
            return False
        prev = prev.next
        head = head.next
    return True