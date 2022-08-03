    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        queue = deque()
        ans = []
        for i, num in enumerate(nums):
            while queue and nums[queue[-1]]< num:
                queue.pop()
            queue.append(i)
            if queue[0] == i-k:
                queue.popleft()
            if i>=k-1:
                ans.append(nums[queue[0]])
        return ans