def findMaxConsecutiveOnes(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ans, final_ans = 0, 0
    for num in nums:
        if num==1:
            ans+=1
        else:
            ans=0
        if final_ans < ans: final_ans = ans
        
    return final_ans