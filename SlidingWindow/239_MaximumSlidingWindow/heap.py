def maxSlidingWindow(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
        heap = []
        for i in range(k-1):
            heapq.heappush(heap,(-nums[i],i))
        res = []
        for i in range(k-1,len(nums)):
            heapq.heappush(heap,(-nums[i],i))
            print(heap)
            while i - k >= heap[0][1]:
                heapq.heappop(heap)

            res.append(-heap[0][0])
        return res 