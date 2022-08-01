class LRUCache:

    def __init__(self, capacity: int):
        self.dic = {}
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.dic:
            val = self.dic[key]
            self.dic.pop(key)
            self.dic[key] = val
            return val
        return -1
            

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.pop(key)
        self.dic[key] = value
        if len(self.dic) > self.cap:
            del self.dic[next(iter(self.dic))]  
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)