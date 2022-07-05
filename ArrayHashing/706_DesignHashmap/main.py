class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap(object):

    def __init__(self):
        #self.dic = {}
        self.size = 1000
        self.hash_table = [None] * self.size 
    
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        #self.dic[key] = value
        index = key % self.size
        if self.hash_table[index] == None:
            self.hash_table[index] = ListNode(key, value)

        else:
            curr_node = self.hash_table[index]
            while True:
                if curr_node.key == key:
                    curr_node.value = value
                    return
                if curr_node.next == None: break
                curr_node = curr_node.next
            curr_node.next = ListNode(key, value)
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # if key not in self.dic: return -1
        # return self.dic[key]
        index = key % self.size
        if self.hash_table[index]==None: return -1
        else:
            curr_node = self.hash_table[index]
            while True:
                if curr_node.key == key:
                    return curr_node.value
                if curr_node.next==None:return -1
                curr_node = curr_node.next
                

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        # if key in self.dic:
        #     del self.dic[key]
        index = key%self.size
        prev_node = curr_node = self.hash_table[index]
        if not curr_node: return
        
        if curr_node.key == key:
            self.hash_table[index] = curr_node.next
            return
        else:
            curr_node = curr_node.next
            
            while curr_node:
                if curr_node.key == key:
                    prev_node.next = curr_node.next 
                    break
                else:
                    prev_node, curr_node = prev_node.next, curr_node.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)