## Solution 1: get the product and then divide
## Time Complexity O(n), Space O(1)
def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    prod = reduce(lambda a, b: a*(b if b else 1), nums, 1)             
    zero_cnt = nums.count(0)
    if zero_cnt > 1: return [0]*len(nums)
    for i, c in enumerate(nums):
        if zero_cnt: nums[i] = 0 if c else prod
        else: nums[i] = prod // c
    return nums

## Solution 2: get the ans[i] = pre[i-1]*suf[i+1]
def productExceptSelf(self, nums):
    pre, suf, n = list(accumulate(nums, mul)), list(accumulate(nums[::-1], mul))[::-1], len(nums)
    return [(pre[i-1] if i else 1) * (suf[i+1] if i+1 < n else 1) for i in range(n)]


## Solution 3: Opitimized Space of Solution 2
def productExceptSelf(self, nums):
        n, ans, suffix_prod = len(nums), [1]*len(nums), 1
        for i in range(1,n):
            ans[i] = ans[i-1] * nums[i-1]
        for i in range(n-1,-1,-1):
            ans[i] *= suffix_prod
            suffix_prod *= nums[i]
        return ans
