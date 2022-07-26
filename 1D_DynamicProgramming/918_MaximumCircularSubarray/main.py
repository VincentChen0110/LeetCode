def maxSubarraySumCircular(self, nums: List[int]) -> int:
    currentSum = nums[0]
    maxSum = nums[0]
    for i in range(1, len(nums)):
        currentSum = max(nums[i], nums[i]+currentSum)
        maxSum = max(currentSum, maxSum)
    
    # Assume the array is not circular and calculate min sub array sum.
    currentSum = nums[0]
    minSum = nums[0]
    for i in range(1, len(nums)):
        currentSum = min(nums[i], nums[i]+currentSum)
        minSum = min(currentSum, minSum)
    
    # Max sub array sum of a cirular array = max(maxSum, totalSum-minSum)

    circularMaxSum = sum(nums)-minSum
    if circularMaxSum == 0:
        return maxSum
    return max(maxSum, circularMaxSum)