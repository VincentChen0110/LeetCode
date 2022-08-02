def findKthLargest(self, nums: List[int], k: int) -> int:
    ## Use Prioity Queue
    # newnums = [-x for x in nums]
    # heapq.heapify(newnums)
    # while k>1:
    #     heapq.heappop(newnums)
    #     k-=1
    # return -newnums[0]
    ## Use Quick Select
    return self.findKthSmallest(nums, 0, len(nums)-1, len(nums)-k)

def findKthSmallest(self, nums, left, right, k):
    
    def partition(left, right, pivotIndex):
        pivot = nums[pivotIndex]
        
        # move pivotindex to the right
        nums[pivotIndex], nums[right] = nums[right], nums[pivotIndex]
        pivotIndex = left
        
        # swap items less than pivot to left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[i], nums[pivotIndex] = nums[pivotIndex], nums[i]
                pivotIndex+=1
        # return pivot index to original place
        nums[pivotIndex], nums[right] = nums[right], nums[pivotIndex]
        return pivotIndex
    
    if left == right:
        return nums[left]
    pivotIndex = random.randint(left, right)
    pivotIndex = partition(left, right, pivotIndex)
    if pivotIndex ==k:
        return nums[pivotIndex]
    if k < pivotIndex:
        return self.findKthSmallest(nums,left, pivotIndex-1, k)
    return self.findKthSmallest(nums, pivotIndex+1, right, k)