from collections import defaultdict
def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    set_nums, ans = set(nums), 0
    for num in nums:
        if num - 1 in set_nums: continue
            
        nxt = num
        while nxt + 1 in set_nums:
            nxt += 1
        ans = max(ans, nxt-num+1)
        

    return ans
print(longestConsecutive([100,4,200,1,3,2]))