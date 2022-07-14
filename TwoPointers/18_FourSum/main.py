def fourSum(self, nums, target):
    nums.sort()
    n, ans = len(nums), []
    for i in range(n):
        for j in range(i + 1, n):
            goal = target - nums[i] - nums[j]
            beg, end = j + 1, n - 1

            while beg < end:
                if nums[beg] + nums[end] < goal:
                    beg += 1
                elif nums[beg] + nums[end] > goal:
                    end -= 1
                else:
                    ans.append((nums[i], nums[j], nums[beg], nums[end]))
                    beg += 1
                    end -= 1

    return set(ans)