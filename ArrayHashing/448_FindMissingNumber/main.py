def findDisappearedNumbers(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    dic = [0]*(len(nums)+1)
    ans = []
    for num in nums:
        dic[num]+=1
    for i, num in enumerate(dic[1:]):
        if num==0: ans.append(i+1)
    return ans