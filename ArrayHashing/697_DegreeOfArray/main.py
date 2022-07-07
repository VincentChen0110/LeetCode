def findShortestSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # dic = {}
    # max_degree = 0
    # ans = float('inf')
    # for i, num in enumerate(nums):
    #     if num not in dic:
    #         dic[num] = [i]
    #         degree=1    
    #         max_degree = max(degree,max_degree)
    #     else:
    #         dic[num].append(i)
    #         max_degree = max(len(dic[num]),max_degree)
    # for k, v in dic.items():
    #     if len(v)==max_degree:
    #         ans = min(ans, v[-1]-v[0]+1)
    # return ans
    nums_map, deg, min_len = collections.defaultdict(list), 0, float('inf')
    for index, num in enumerate(nums):
        nums_map[num].append(index)
        if len(nums_map[num]) == deg:
            min_len = min(min_len, nums_map[num][-1] - nums_map[num][0] + 1)
        elif len(nums_map[num]) > deg:
            deg = len(nums_map[num])
            min_len = nums_map[num][-1] - nums_map[num][0] + 1
    return min_len 
nums = [3,3,4]
print(findShortestSubArray(nums))