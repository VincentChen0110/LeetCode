def findLHS(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # dic = {}
    # for num in nums:
    #     dic[num] = dic.get(num,0)+1
    dic = collections.Counter(nums)
    ans = 0
    for key in dic:
        if key+1 in dic:
            ans = max(ans, dic[key]+dic[key+1])
    return ans