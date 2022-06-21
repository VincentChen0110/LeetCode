# Idea:
# We have an ascending array, which is rotated at some pivot.
# Let's call the rotation the inflection point. (IP)
# One characteristic the inflection point holds is: arr[IP] > arr[IP + 1] and arr[IP] > arr[IP - 1]
# So if we had an array like: [7, 8, 9, 0, 1, 2, 3, 4] the inflection point, IP would be the number 9.

# One thing we can see is that values until the IP are ascending. And values from IP + 1 until end are also ascending (binary search, wink, wink).
# Also the values from [0, IP] are always bigger than [IP + 1, n].

# intuition:
# We can perform a Binary Search.
# If A[mid] is bigger than A[left] we know the inflection point will be to the right of us, meaning values from a[left]...a[mid] are ascending.

# So if target is between that range we just cut our search space to the left.
# Otherwise go right.

# The other condition is that A[mid] is not bigger than A[left] meaning a[mid]...a[right] is ascending.
# In the same manner we can check if target is in that range and cut the search space correspondingly.
def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if not nums: return -1
    l, r = 0, len(nums)-1
    while(l<=r):
        m = l+(r-l)//2
        if(nums[m]==target): return m
        if nums[l] <= nums[m]: ## If l to m is correct order
            if(nums[l]<=target<=nums[m]):
                r = m-1
            else:
                l = m+1
        else: ## 
            if(nums[r]>=target>=nums[m]):
                l = m+1
            else:
                r = m-1
    return -1