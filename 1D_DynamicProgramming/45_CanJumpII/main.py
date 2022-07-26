def jump(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums)==1: return 0
    maxi = 0
    end = 0
    jumps = 0
    for i in range(0,len(nums)-1):
        maxi = max(maxi, nums[i]+i)
        ### Reach end of this jump
        if(i==end):
            jumps+=1
            end = maxi
    return jumps
    ## BFS Solution
    # if len(nums)==1: return 0
    # end, start, jump = 0, 0, 0
    # while end < len(nums) -1:
    #     jump += 1
    #     maxend = end + 1
    #     for i in range(start,end+1):
    #         if nums[i] + i >= len(nums)-1:
    #             return jump
    #         maxend = max(maxend, nums[i]+i)
    #     start, end = end +1, maxend
    # return jump