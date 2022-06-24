# Tortoise Hare Solution
#  This is pretty classical and well-know problem about linked list. One way is just to put all linked list to for example hash table and check if we have repeating elements. However it will take O(n) space. There is better solution with only O(1) complexity. Imagine the following example:
# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 3, the list with loop. Idea is to use two pointers, one is slow and one is fast, let us do several steps:

# At the beginning, both of them at number 1.
# Next step, slow pointer at 2 and fast at 3.
# Next step, slow pointer at 3 and fast at 5.
# Next step, slow pointer at 4 and fast at 3.
# Next step, slow pointer at 5 and fast is also 5, so we have the same element and we return True.
# If we do not have loop we will never have equal elements, if we have loop, because slow pointer moves with speed 1 and fast with speed 2, fast pointer will always gain slow one.
def hasCycle(head):
    try:
        slow = head
        fast = head.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except:
        return False