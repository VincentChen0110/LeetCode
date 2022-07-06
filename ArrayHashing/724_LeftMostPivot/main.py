def pivotIndex(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    lsum ,rsum = 0, sum(nums)
    for i, num in enumerate(nums):
        rsum-=num
        if lsum==rsum:return i
        lsum+=num
    return -1