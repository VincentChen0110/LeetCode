def runningSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ans = [nums[0]]
    for i, num in enumerate(nums[1:]):
        ans.append(ans[i]+num)
    return ans