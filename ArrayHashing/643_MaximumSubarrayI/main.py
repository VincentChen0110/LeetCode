def findMaxAverage(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    maxi = summ = sum(nums[:k])
    
    for i in range(1,len(nums)-k+1):
        summ-=nums[i-1]
        summ+=nums[i+k-1]
        maxi = max(summ, maxi)
    return float(maxi)/k
    
nums = [1,12,-5,-6,50,3]
k=4
print(findMaxAverage(nums,k))
