def rob(self, nums: List[int]) -> int:
    @cache
    def f(i):
        if i <len(nums):
            return max(f(i+1),f(i+2)+nums[i])
        else:
            return 0
    return f(0)