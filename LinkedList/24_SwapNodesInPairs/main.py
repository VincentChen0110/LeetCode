# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ## Modify Values
        # prev = None
        # dummy = head
        # while head and head.next:
        #     head.val, head.next.val = head.next.val, head.val
        #     head = head.next.next
        # return dummy
        dummy = ListNode(0, head)
        cur = dummy
        while cur.next and cur.next.next:
            first = cur.next
            second = cur.next.next
            cur.next = second # Update cur
            first.next = second.next # Update first.next linking to second.next
            second.next = first #uudate second  next linking to first next
            cur = cur.next.next
        return dummy.next

        