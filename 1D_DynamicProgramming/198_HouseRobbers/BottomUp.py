def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ### NOTES: DP: Recursion: rob[i] = max(rob[i-1], rob[i-2] + nums[i])
    n = len(nums)
    if n==1:return nums[0]
    if n==2:return max(nums[0],nums[1])
    dp = [0]*(n+1)
    dp[0], dp[1] = nums[0], max(nums[0],nums[1])
    for i in range(2, n):
        #print(i)
        dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        print(dp[i], i)
    return dp[n]
        ## Solution with Bottom Up Memoization 2 variables
#         prev1, prev2 = 0, 0
#         for num in nums:
#             prev1, prev2 = max(prev1, prev2+num), prev1
#         return prev1

nums = [1,2,3,1]
print(rob(nums))