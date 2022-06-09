class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, item in enumerate(nums):
            if target-item in dic:
                return [dic[target-item],i];
            else:
                dic[item] = i
        return dic