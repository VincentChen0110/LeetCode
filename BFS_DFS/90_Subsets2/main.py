## Back-Tracking Approach
def subsetsWithDup(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    dfs(sorted(nums),[],res)
    return res
def dfs(nums, path, res):
    res.append(path)
    for i in range(len(nums)):
        if i > 0 and nums[i]==nums[i-1]: 
            continue
        dfs(nums[i+1:], path+[nums[i]], res)
## Bit Masking appraoch
# def subsetsWithDup(self, nums):
#     n = len(nums)
#     nums.sort()
#     seen = set()

#     for mask in range(1 << n):
#         subset = []
#         for i in range(n):
#             bit = (mask >> i) & 1  # Get i_th bit of mask
#             if bit == 1:
#                 subset.append(nums[i])

#         seen.add(tuple(subset))

#    return seen
nums = [1,2,2]
print(subsetsWithDup(nums))