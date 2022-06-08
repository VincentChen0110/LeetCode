# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self): 
        self.head = None
        #self.tail = None

    def push(self, item):
        new_node = ListNode(item)
        new_node.next = self.head
        self.head = new_node

    def reverseList(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.val)
            temp = temp.next


list1 = LinkedList()
list1.push(1)
list1.push(2)
list1.push(3)
list1.push(4)
list1.push(5)

list1.printList()
list1.reverseList()
list1.printList()