def combine(self, n, k):
        ret = []
        self.dfs(list(range(1, n+1)), k, [], ret)
        return ret
    
    def dfs(self, nums, k, path, ret):
        if len(path) == k:
            ret.append(path)
            return 
        for i in range(len(nums)):
            self.dfs(nums[i+1:], k, path+[nums[i]], ret)