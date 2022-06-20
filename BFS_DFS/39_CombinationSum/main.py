# Solution 2
def dfs2(nums, target, index, path, res):
    if sum(path) == target:
        res.append(path[:])
        return
    if sum(path) > target:
        return
    for i in range(index, len(nums)):
        path.append(nums[i])
        dfs2(nums, target, i, path, res)
        path.pop()

# Solution 1:
def dfs1(self, nums, target,index, path, res):
    if target==0:
        res.append(path)
        return
    if target<0:
        return
    for i in range(index,len(nums)):
        self.dfs(nums,target-nums[i],i,path+[nums[i]],res)

def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    candidates.sort()
    #self.dfs1(candidates, target, 0, [], res)
    dfs2(candidates, target, 0, [], res)
    return res
res = []
candidates = [2,3,6,7]
target = 7
print(combinationSum(candidates,target))