def nextGreaterElement(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    # ans = []
    # def check_greater(num):
    #     flag = False
    #     for n in nums2:
    #         if n==num:
    #             flag = True
    #         if flag and n>num:
    #             return n
    #     return -1
    # for num in nums1:
    #     ans.append(check_greater(num))
    # return ans
    greater,stack = {},[]
    for n in nums2:
        print("n: ",n)
        while stack and n > stack[-1]:
            greater[stack.pop()] = n
        stack.append(n)
        print("stack: ", stack)
    return [greater[n] if n in greater else -1 for n in nums1]
nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(nextGreaterElement(nums1, nums2))