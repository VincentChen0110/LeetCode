def threeSumClosest(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    nums.sort() # O(nlgn)
    ans = float('inf')
    
    for i in range(len(nums) - 2): # O(n)
        l, r = i+1, len(nums)-1
        # print(ans)
        while(l<r): #O(n)
            temp_sum = nums[l]+nums[r] +nums[i]
            if (temp_sum==target): return target
            if abs(temp_sum-target) < abs(ans-target): ans = temp_sum
            if(temp_sum > target): r -= 1
            else: l += 1
        
    return ans