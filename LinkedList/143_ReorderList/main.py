## Three Step
def reorderList(self, head):
    """
    :type head: ListNode
    :rtype: None Do not return anything, modify head in-place instead.
    """
    #step 1: find middle
    if not head: return []
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    #step 2: reverse second half
    prev, curr = None, slow.next
    while curr:
        nextt = curr.next
        curr.next = prev
        prev = curr
        curr = nextt
    slow.next = None
    
    #step 3: merge lists
    head1, head2 = head, prev
    while head2:
        nextt = head1.next
        head1.next = head2
        head1 = head2
        head2 = nextt

### Use additional O(n) array
def reorderList(self, head):
    """
    :type head: ListNode
    :rtype: None Do not return anything, modify head in-place instead.
    """
    arr = []
    cur , length = head, 0
    while cur:
        arr.append(cur)
        cur = cur.next
        length += 1
    
    l , r = 0, length-1
    last = head
    while(l<r):
        arr[l].next = arr[r]
        l += 1
        if l==r:
            last = arr[r]
            break
        arr[r].next = arr[l]
        r-=1
        last = arr[l]
        
    if last:
        last.next = None