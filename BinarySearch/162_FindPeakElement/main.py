
def findPeakElement(self, nums: List[int]) -> int:
    ## peak element 1 2 1
    l, r = 0, len(nums)-1
    ## Check 
    while(l < r):
        m = l +(r-l)//2
        if (nums[m+1]<nums[m] and nums[m]>nums[m-1]): return m
        if (nums[m+1]<nums[m]): ## 2 3 
            r = m
        else: 
            l = m + 1
    return l
            