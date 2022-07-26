def maxSubArray(self, nums: List[int]) -> int:
    ## Bottom Up
    # max_sum = -float('inf')
    # max_now = 0
    # for num in nums: 
    #     if max_now <= 0:
    #         max_now = num 
    #     else:
    #         max_now += num
    #     max_sum = max(max_now, max_sum)
    # return max_sum
    dp = [*nums]
    for i in range(1, len(nums)):
        dp[i] = max(nums[i], nums[i] + dp[i-1])
    return max(dp)