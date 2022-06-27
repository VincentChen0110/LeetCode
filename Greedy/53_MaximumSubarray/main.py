def maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    cur = res = nums[0]
    for item in nums[1:]:
        if cur > 0 :
            cur += item
        else:
            cur = item
        if cur > res:
            res = cur
    return res