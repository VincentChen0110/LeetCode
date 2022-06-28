## Solution1 : find length and then del
## Solution2: use slow, fast to keep n between 2 pointers

def removeNthFromEnd(self, head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    #Solutioni 1
    # count = 0
    # dummy = cur = head
    # while cur:
    #     count += 1
    #     cur = cur.next
    # if count==n:return head.next
    # for _ in range(1,count-n):
    #     head = head.next
    # head.next = head.next.next
    # return dummy
    # Solution 2
    fast = slow = head
    for _ in range(n):
        fast = fast.next
    if not fast: return head.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head