from collections import Counter
import heapq
from itertools import chain
def topKFrequent(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ## SOLUTION 1: USE HEAP ##
        # res = []
        # dic = Counter(nums)
        # print(dic)
        # max_heap = [(-v, k) for k, v in dic.items()]
        # print(max_heap)
        # heapq.heapify(max_heap)
        # print(max_heap)
        # for i in range(k):
        #     res.append(heapq.heappop(max_heap)[1])
        # return res 
        ## SOlUTION 2: USE BUCKETSORT ##
        bucket = [[] for _ in range(len(nums) + 1)]
        Count = Counter(nums).items()  
        for num, freq in Count: bucket[freq].append(num) 
        print(bucket)
        flat_list = list(chain(*bucket))
        return flat_list[::-1][:k]

nums = [2,1,2,1,1,3]
print(topKFrequent(nums,2))