def rob(nums):
    def simple_rob(nums):
        rob, not_rob = 0, 0
        for num in nums:
            rob, not_rob = not_rob + num, max(rob, not_rob)
        return max(rob, not_rob)

    if len(nums) == 1:
        return nums[0]
    else:
        return max(simple_rob(nums[1:]), simple_rob(nums[:-1]))