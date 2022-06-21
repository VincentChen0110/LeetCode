def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l, r = 0, len(nums)-1
    ## If l<=r will not converge
    while(l<r):
        m = l+(r-l)//2 ##This could avoid overflow if we use l+r
        if(nums[m]>nums[r]): ### If this is True then the pivot point must be on the right side
            l = m+1 
        else: # else it must be on the left side
            r = m
    return nums[l]

nums = [4,5,6,7,0,1,2]
print(findMin(nums))