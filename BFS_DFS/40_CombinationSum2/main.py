def combinationSum2(self, candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    res = []
    self.dfs(sorted(candidates),target, [], res)
    return res
def dfs(self, nums, target,  path, res):
    if target==0:
        res.append(path)
        return
    if target<0:
        return
    for i in range(len(nums)):
        if i>0 and nums[i]==nums[i-1]:
            continue
        self.dfs(nums[i+1:],target-nums[i],path+[nums[i]],res)