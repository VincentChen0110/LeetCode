def canJump(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    ## Algorithm1: Continue updating maxindex that we can reach
    # maxi = 0
    # index = 0
    # while(index<len(nums) and index <= maxi):
    #     maxi = max(maxi,nums[index]+index)
    #     index += 1
    # if index == len(nums): return True
    # return False
    ## Algo2: Backwards
    l = len(nums)-1
    for i in range(len(nums)-2,-1,-1):
        if (nums[i]+i>=l):
            l = i;
    if(l==0): return True
    return False