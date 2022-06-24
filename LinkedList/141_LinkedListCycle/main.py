# Solution 1, Use hashmap
def hasCycle(head):
    dic = {}
    while head:
        if head in dic:
            return True
        if head not in dic:
            dic[head] = 1
        head = head.next
    return False

## Solution 2, changed visited to None
def hasCycle(head):
    while head:
        if head.val == None:
            return True
        head.val = None
        head = head.next
    return False