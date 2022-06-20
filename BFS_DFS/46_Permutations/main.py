def permute(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    if not nums: return []
    self.dfs(nums, [], res) 
    return res

def dfs(self, nums, path, res):
    if not nums:
        res.append(path)
        return
    
    for i in range(len(nums)):
        self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
def dfs(self, nums, path, res):
    if not nums:
        res.append(path[:])
        return
    
    for i in range(len(nums)):
        path.append(nums[i])
        self.dfs(nums[:i]+nums[i+1:], path, res)
        path.pop()
