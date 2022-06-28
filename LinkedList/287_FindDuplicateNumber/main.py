def findDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    slow, fast = nums[0], nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if fast==slow: break
    print(fast)
    slow = nums[0]
    while slow!=fast:
        slow, fast = nums[slow], nums[fast]
    return slow
def findDuplicate(nums):
    l, r = 1, len(nums)-1
    while l < r:
        m = l+(r-l)/2
        count = 0
        for i in nums:
            if i <= m:
                count +=1
        if count <= m:
            l = m+1
        else:
            r = m
    return r
nums = [1,3,4,2,2]
print(findDuplicate(nums))