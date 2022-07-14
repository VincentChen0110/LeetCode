def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # if len(nums) < 1:
        #     return -1,-1
        # n = len(nums)
        # left, right = -1, -1
        # l, r = 0, n-1
        # while l < r:
        #     m = (l+r)/2
        #     if nums[m] < target: l = m+1
        #     else: r = m
        # if nums[l] != target: return -1, -1
        # left = l
        # l, r = left, n-1
        # while l < r:
        #     m = (l+r)/2+1
        #     if nums[m] == target: l = m
        #     else: r = m-1
        # right = l
        # return left, right
        def search(x):
            l, r = 0, len(nums)       
            while l < r:
                mid = l + (r-l)//2
                if nums[mid] < x:
                    l = mid+1
                else:
                    r = mid                    
            return l

        l = search(target)
        r = search(target+1)-1

        if l <= r:
            return [l, r]

        return [-1, -1]    