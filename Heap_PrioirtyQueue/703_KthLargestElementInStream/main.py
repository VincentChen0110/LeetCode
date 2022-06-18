import heapq
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.pool = nums
        heapq.heapify(self.pool)
        self.k = k
        while len(self.pool) > k:
            heapq.heappop(self.pool)
            print(self.pool)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]

heap = KthLargest(3, [4, 5, 8, 2])
heap.add(3);   
heap.add(5);   
heap.add(10);  
heap.add(9);   
heap.add(4);   