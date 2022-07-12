def minSubArrayLen(self, target, nums):
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """
    ### Slide Window
    ### [2,3,1,2,4,3] --> [2,5,6,8,12,15]
    ### Search if r-l > target 
    i, res = 0, len(nums) + 1
    for j in range(len(nums)):
        target -= nums[j]
        while target <= 0:
            res = min(res, j - i + 1)
            target += nums[i]
            i += 1
    return res % (len(nums) + 1)