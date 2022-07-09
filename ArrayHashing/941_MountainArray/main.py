def validMountainArray(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    increase = True
    if len(arr)<3 or arr[0]>=arr[1]:
        return False
    for i in range(1,len(arr)):
        if increase:
            if arr[i-1]>=arr[i]:
                increase = False
        if not increase:
            if arr[i-1]<=arr[i]:
                return False
    return not increase
nums = [0,1,2,4,2,1]
print(validMountainArray(nums))